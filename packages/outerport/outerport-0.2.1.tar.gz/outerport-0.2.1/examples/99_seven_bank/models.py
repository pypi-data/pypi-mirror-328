#============================================================
# データベース操作(バックエンド)
#============================================================
# from flask import jsonify, request
import logging
#from dotenv import load_dotenv
from datetime import datetime
# from openai import AzureOpenAI, BadRequestError
from outerport import OuterportClient

# envファイルから環境変数を取得
#load_dotenv()

# JSTタイムゾーンを設定
# jst = timezone('Asia/Tokyo')

#============================================================
# 初期化
#============================================================
# ロガー
logger = logging.getLogger("NBB")

# Outerportクライアント
client = OuterportClient(api_key="asdfghjkl", base_url="http://localhost:8080")


#============================================================
# クラス定義(データ操作関係)
#============================================================
# ChatMessageクラス(プロンプト、応答結果を保持)
class ChatMessage:
    # コンストラクタ
    def __init__(self, id, user_id, thread_id, role, message, action_at, conversation_id,
                 hate_filtered, sexual_filtered, violence_filtered, self_harm_filtered):
        self.id = id # ランダムに生成される識別ID
        self.user_id = user_id # ユーザーID
        self.thread_id = thread_id #スレッド番号（旧：id）
        self.role = role # user/assistant
        self.message = message # message内容
        self.action_at = action_at # アクション日時
        self.conversation_id = conversation_id # mssage往復数
        
        # プロンプトフィルタリング結果（フィルター反応：True、問題なし：False）
        self.hate_filtered = hate_filtered # 憎悪
        self.sexual_filtered = sexual_filtered # 性的
        self.violence_filtered = violence_filtered # 暴力
        self.self_harm_filtered = self_harm_filtered # 自傷


# ChatThreadクラス(スレッド情報を保持)
class ChatThread:
    # コンストラクタ
    def __init__(self, user_id, thread_id, thread_name, created_at,
                 last_updated_at, is_clipped, is_deleted):
        
        self.user_id = user_id # ユーザーID
        self.thread_id = thread_id #スレッド番号（旧：id）
        self.thread_name = thread_name # スレッド名（旧：name）
        self.created_at = created_at # スレッド作成日時
        self.last_updated_at = last_updated_at # 最後に会話した日時
        self.is_clipped = is_clipped # クリップ有：True、クリップ無：False
        self.is_deleted = is_deleted # スレッド削除：True、未削除：False

    # 並べ替え判定
    def __lt__(self, other):
        # お気に入り設定がされていたら優先
        if self.is_clipped and not other.is_clipped:
            return True
        # お気に入り設定されていなかったら劣後
        elif not self.is_clipped and other.is_clipped:
            return False
        # お気に入り設定が同じであれば直近利用の新しい方を優先
        else:
            return self.last_updated_at > other.last_updated_at


# ChatFavoriteTemplate(お気に入りテンプレートを保持)
class ChatFavoriteTemplate:
    # コンストラクタ
    def __init__(self, template_owner, is_system_template, template_no, is_favorite, last_updated):
        self.template_owner = template_owner # "System" or テンプレート所有者
        self.is_system_template = is_system_template #システムテンプレートかどうか
        self.template_no = template_no #テンプレート番号
        self.is_favorite = is_favorite #一度登録されたら物理削除しないので
        self.last_updated = last_updated #最終更新日

    # 並べ替え判定
    def __lt__(self, other):
        # カスタムテンプレートを優先
        if not self.is_system_template and other.is_system_template:
            return True
        # システムテンプレートは劣後
        if self.is_system_template and not other.is_system_template:
            return False
        # オーナーが同じ場合は新しいものを優先
        else:
            return self.last_updated > other.last_updated


# InternalCustomSearchDocument(カスタム検索用ドキュメントを保持)
class InternalCustomSearchDocument:
    # コンストラクタ
    def __init__(self, doc_owner, doc_id, doc_name, last_use_date, is_clipped):
        self.doc_owner = doc_owner #ドキュメント所有者
        self.doc_id = doc_id #ドキュメントID
        self.doc_name = doc_name #ドキュメント名
        self.last_use_date = last_use_date #最終利用日
        self.is_clipped = is_clipped #クリップ有無
 
    # 並べ替え判定
    def __lt__(self, other):
        # お気に入り設定がされていたら優先
        if self.is_clipped and not other.is_clipped:
            return True
        # お気に入り設定されていなかったら劣後
        elif not self.is_clipped and other.is_clipped:
            return False
        # お気に入り設定が同じであれば直近利用の新しい方を優先
        else:
            return self.last_use_date > other.last_use_date
 
# InternalSearchResult(社内情報検索結果を保持)
class InternalSearchResult:
    # コンストラクタ
    def __init__(self, user_id, doc_id, message, evidences_and_reasons):
        self.user_id = user_id
        self.doc_id = doc_id #ドキュメントID(カスタム検索の場合)
        self.message = message #検索結果メッセージ
        self.evidences_and_reasons = evidences_and_reasons #エビデンスと理由のリスト(assistantの場合)、[[e1, r1], [e2, r2], ....]


# AnalysisResult(データ分析結果データを保持)
class AnalysisResult:
    # コンストラクタ
    def __init__(self, sql_status, sql_message, data_status, data_message, graph_status, graph_message, insight_status, insight_message):
        self.sql_status = sql_status
        self.sql_message = sql_message
        self.data_status = data_status
        self.data_message = data_message
        self.graph_status = graph_status
        self.graph_message = graph_message
        self.insight_status = insight_status
        self.insight_message = insight_message


#============================================================
# 社内情報検索機能
#============================================================
# 社内情報検索のプロンプト実行・応答結果取得
def exec_internal_search_prompt(user_id, prompt_message):
    logger.info(f"開始(user_id={user_id}, prompt_message=*)")
 
    ### 暫定処理 ###
    internal_search_result = InternalSearchResult(user_id, None, prompt_message + "を検索した結果、以下が見つかりました。この情報で希望は満たされているでしょうか？追加で検索したい場合はこのまま検索したい文言を入力してください。", [["検索した情報はこの社内規程のここに書かれています", "質問の内容からしてここに記載された情報は正しいと思われます。"], ["他にもこんなエビデンスもあります。", "だから回答は正しいと思います。"]])
 
    logger.info("終了")
    return internal_search_result
 
 
# 社内情報カスタム検索のプロンプト実行・応答結果取得
def exec_internal_custom_search_prompt(user_id, doc_id, prompt_message):
    logger.info(f"開始(user_id={user_id}, doc_id={doc_id} prompt_message=*)")
 
    ### 暫定処理 ###
    doc_name =""
    for doc in client.documents.list():
        if doc.id == doc_id:
            doc_name = doc.name
            break

    question = client.questions.create(
        document_ids=[doc_id],
        question=prompt_message,
        user_id=user_id
    )

    message = doc_name + "で検索しています。" + prompt_message + "を検索した結果、以下が見つかりました。この情報で希望は満たされているでしょうか？追加で検索したい場合はこのまま検索したい文言を入力してください。"

    evidences_and_reasons = [(pair.evidence, pair.reasoning) for pair in question.evidences]

    internal_custom_search_result = InternalSearchResult(
        user_id=user_id, 
        doc_id=doc_id, 
        message=message,
        evidences_and_reasons=evidences_and_reasons
    )

    logger.info("終了")
    return internal_custom_search_result
 
exec_internal_custom_search_prompt(1, 128, "Arxivに役員が論文を出したい場合の決裁権限")

# 社内情報カスタム検索のドキュメント一覧取得
def get_internal_custom_search_doc_list(user_id):
    logger.info(f"開始(user_id={user_id})")
 
    ### 暫定処理 ###
    # 自分のドキュメント一覧を作成
    internal_custom_search_doc_list = list(filter(lambda doc: doc.doc_owner == user_id , client.documents.list()))
 
    logger.info("終了")
    return internal_custom_search_doc_list
 
 
# 社内情報カスタム検索のクリップされたドキュメント一覧取得
def get_internal_custom_search_clipped_doc_list(user_id):
    logger.info(f"開始(user_id={user_id})")
 
    ### 暫定処理 ###
    # クリップ設定された自分のドキュメント一覧を作成
    internal_custom_search_clipped_doc_list = list(filter(lambda doc: doc.doc_owner == user_id and doc.is_clipped, dummy_internal_custom_search_doc_list))
 
    logger.info("終了")
    return internal_custom_search_clipped_doc_list
 
 
# 社内情報カスタム検索のドキュメント名の取得
def get_internal_custom_search_doc_name(user_id, doc_id):
    logger.info(f"開始(user_id={user_id}, doc_id={doc_id})")
 
    ### 暫定処理 ###
    doc_name =""
    for doc in dummy_internal_custom_search_doc_list:
        if doc.doc_owner == user_id and doc.doc_id == doc_id:
            doc_name = doc.doc_name
            break
 
    logger.info(f"終了(doc_name={doc_name})")
    return doc_name
 
 
# 社内情報カスタム検索のドキュメント追加(doc_objectはファイルそのもの)
def add_internal_custom_search_doc(user_id, doc_name, doc_object):
    logger.info(f"開始(user_id={user_id}, doc_name={doc_name})")
 
    ### 暫定処理 ###
    now = datetime.now()
    doc_id = now.strftime('%Y%m%d%H%M%S')
 
    # ドキュメント追加
    new_doc = InternalCustomSearchDocument(user_id, str(doc_id), doc_name, "2025/2/9", False)
    doc_file = doc_object.read()
    client.documents.create(file=doc_file, file_name=doc_name)
 
    logger.info("終了")
 
 
# 社内情報カスタム検索のドキュメントのクリップ設定/解除
def clip_internal_custom_search_doc(user_id, doc_id, is_clipped):
    logger.info(f"開始(user_id={user_id}, doc_id={doc_id}, is_clipped={is_clipped})")
 
    ### 暫定処理 ###
    for doc in dummy_internal_custom_search_doc_list:
        if doc.doc_owner == user_id and doc.doc_id == doc_id:
            doc.is_clipped = is_clipped
 
    logger.info("終了")
 
 
# 社内情報カスタム検索のドキュメント削除
def delete_internal_custom_search_doc(user_id, doc_id):
    logger.info(f"開始(user_id={user_id}, doc_id={doc_id})")
 
    client.documents.delete(doc_id)
 
    logger.info("終了")

