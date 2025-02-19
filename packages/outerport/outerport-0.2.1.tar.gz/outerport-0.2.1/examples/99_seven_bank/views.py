#============================================================
# 表示コンテンツを制御
#============================================================
from flask import Flask, Blueprint, render_template, g, request, session, current_app
import requests # 【変更】2025/1/10 ユーザー情報取得
import sys, traceback # 【変更】2025/1/10 エラー処理追加
import logging
import copy
import markdown #【変更】2025/1/9
import re
from .models import *

flask_app = Flask

#============================================================
# 関数定義(表示関係)
#============================================================
# ユーザー情報を取得
def get_user_id():
    try:
        logger.info("開始")
        
        # 【変更】2025/1/10 ユーザー情報取得
        if "user_id" in session:
            user_id = session["user_id"]
        else:
            logger.info("ユーザー情報取得")
            # user_id = "iXXXX"
            # url = "https://entchat-test.azurewebsites.net/.auth/me" # 暫定URL entachat-test
            # user_id = requests.get(url).json()[0]["user_id"]
            user_id = request.headers.get('X-MS-CLIENT-PRINCIPAL-NAME') # MS認証のuser_idを取得

            # user_idがNoneかつデバッグモードがTrueの場合、user_idをiXXXXに設定
            if user_id is None and current_app.debug:
                logger.info("デバッグモードなので、暫定ユーザー情報を使用")
                user_id = "iXXXX"
            elif user_id is None:
                logger.error("認証情報取得NG")
                raise Exception("認証情報が取得できませんでした。")

            session.permanent = True # セッション情報有効化
            session["user_id"] = user_id # セッション情報にuser_idを設定
        logger.info("終了(user_id=%s)" % user_id)
        return user_id

    except Exception as e:
        raise e


# テンプレートリストを作成
def create_template_list():
    logger.info("開始")
    
    # システムテンプレートリスト取得
    system_prompt_template_list = get_chat_system_prompt_template_list(g.user_id)

    # カスタムテンプレートリスト取得
    custom_prompt_template_list = get_chat_custom_prompt_template_list(g.user_id)

    # お気に入りテンプレートのインデックスリスト取得
    favorite_prompt_template_index_list = sorted(get_chat_favorite_prompt_template_list(g.user_id))

    # お気に入りテンプレート抽出
    favorite_prompt_template_list = []
    for favorite_prompt_template_index in favorite_prompt_template_index_list:
        # お気に入りテンプレートの場合
        if favorite_prompt_template_index.is_favorite:
            # お気に入りテンプレートがシステムテンプレートの場合
            if favorite_prompt_template_index.is_system_template:
                for system_prompt_template in system_prompt_template_list:
                    if system_prompt_template.no == favorite_prompt_template_index.template_no:
                        favorite_prompt_template_list.append(system_prompt_template)
                        system_prompt_template_list.remove(system_prompt_template)
                        break
            # お気に入りテンプレートがカスタムテンプレートの場合
            elif not favorite_prompt_template_index.is_system_template:
                for custom_prompt_template in custom_prompt_template_list:
                    if custom_prompt_template.no == favorite_prompt_template_index.template_no:
                        favorite_prompt_template_list.append(custom_prompt_template)
                        custom_prompt_template_list.remove(custom_prompt_template)
                        break
    
    # お気に入り以外のテンプレートリスト作成
    prompt_template_list = sorted(system_prompt_template_list + custom_prompt_template_list)
    
    logger.info("終了")
    return favorite_prompt_template_list, prompt_template_list


# 共通のエラー処理(エラー情報をログ出力して画面にも表示)
def common_error_handling():
    logger.info("ErrorLog開始")
    err_type, err_value, err_traceback = sys.exc_info()
    logger.error(traceback.format_exc())
    error_message = f"{err_type.__name__} : {err_value}"
    if "user_id" not in g:
        clipped_thread_list = []
    else:
        clipped_thread_list = get_chat_clipped_thread_list(g.user_id)
    logger.info("ErrorLog終了")
    return render_template('error.html', clipped_thread_list = clipped_thread_list, error_message = error_message)
        

#============================================================
# 初期化
#============================================================
# ブループリント生成
app = Blueprint("views", __name__)

# ロガー
logger = logging.getLogger("NBB")


#============================================================
# フィルター(【変更】2025/1/9)
#============================================================
# 改行コードを<br>に変換するフィルター
@app.app_template_filter('cr')
def cr(message):
    # ChatMessageクラスの場合
    if hasattr(message, 'message'):
        return message.message.replace('\r', '<br>')
    # 辞書型の場合
    elif isinstance(message, dict):
        return message.get('content', '').replace('\r', '<br>')
    # 文字列の場合
    elif isinstance(message, str):
        return message.replace('\r', '<br>')
    # それ以外の場合
    return str(message)


# MarkdownをHtmlに変換するフィルター
@app.app_template_filter("markdown2html")
def markdown2html(message):
    # メッセージ内容を取得
    if hasattr(message, 'message'):
        content = message.message
    elif isinstance(message, dict):
        content = message.get('content', '')
    elif isinstance(message, str):
        content = message
    else:
        content = str(message)

    html = markdown.markdown(content, extensions=[
        'tables',
        'fenced_code'
    ])

    # コードブロック抽出
    md_pattern = r"```.*?\n(.*?)```"
    md_matches = re.findall(md_pattern, content, re.DOTALL)

    # html変換後のコードブロック抽出
    html_pattern = r"(<pre><code.*?</code></pre>)"
    html_matches = re.findall(html_pattern, html, re.DOTALL)
    
    # クリップボードにコピーボタン追加
    md_matches_len = len(md_matches)
    html_matches_len = len(html_matches)
    if md_matches_len > 0 and md_matches_len == html_matches_len:
        for i in range(md_matches_len):
            copy_html = f"""
<div class="code_copy_container">
<div class="code_text">{md_matches[i]}</div>
<button class="code_copy_btn">copy</button>
</div>
                        """
            html = html.replace(html_matches[i], html_matches[i] + copy_html)
    return html


#============================================================
# ルーティング
#============================================================
# リクエストの前処理
@app.before_request
def before_request():
    try:
        logger.info("開始")
        # ユーザー情報取得("g"はグローバル変数)
        g.user_id = get_user_id()
        
    except Exception as e:
        return common_error_handling()

# トップ画面
@app.route('/', methods=['GET'])
def top():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "top", request.path, request.method)

        # トップ画面を表示
        logger.info("終了")
        return render_template('top.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = None, message_list = [], prompt = "", thread_name="")

    except Exception as e:
        log_user_action(g.user_id, "chat", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# チャット画面
@app.route('/chat', methods=['GET'])
def chat():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "chat", request.path, request.method)
        # 新規スレッドの場合はthread_idにNone設定
        new_thread_id = None
        
        # チャット画面を表示
        logger.info("終了")
        return render_template('chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = None, message_list = [], prompt = "", thread_name="")

    except Exception as e:
        log_user_action(g.user_id, "chat", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# チャット画面(スレッド付き)
@app.route('/chat_with_thread/<int:thread_id>', methods=['GET'])
def chat_with_thread(thread_id):
    try:
        logger.info(f"開始(thread_id={thread_id})")
        log_user_action(g.user_id, f"chat_with_thread(thread_id={thread_id})", 
                       request.path, request.method)
        
        # メッセージ履歴を取得
        message_list = get_chat_message_history(g.user_id, thread_id)
        # スレッド名を取得
        thread_name = get_chat_thread_name(g.user_id, thread_id)
        
        # メッセージ履歴を設定してチャット画面を表示
        logger.info("終了")
        return render_template('chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = thread_id, message_list = message_list, prompt = "", thread_name = thread_name)

    except Exception as e:
        log_user_action(g.user_id, f"chat_with_thread(thread_id={thread_id})", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# チャット画面(プロンプトテンプレート利用)
@app.route('/chat_with_prompt_template/<string:is_system_template>/<int:prompt_template_no>', methods=['GET'])
def chat_with_prompt_template(is_system_template, prompt_template_no):
    try:
        logger.info(f"開始(is_system_template={is_system_template}, prompt_template_no={prompt_template_no})")
        log_user_action(g.user_id, f"chat_with_prompt_template(no={prompt_template_no})", 
                        request.path, request.method)
        
        if is_system_template == "True":
            # システムプロンプトテンプレートを取得    
            prompt = get_chat_system_prompt_template(g.user_id, prompt_template_no)
        else:
            # カスタムプロンプトテンプレートを取得    
            prompt = get_chat_custom_prompt_template(g.user_id, prompt_template_no)            

        # プロンプトテンプレートを設定してチャット画面を表示
        logger.info("終了")
        return render_template('chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = None, message_list = [], prompt = prompt, thread_name = "")

    except Exception as e:
        log_user_action(g.user_id, f"chat_with_prompt_template(no={prompt_template_no})", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# チャット画面でスレッド名変更
@app.route('/chat_change_thread_name', methods=['POST'])
def chat_change_thread_name():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "chat_change_thread_name", request.path, request.method)

        # スレッド名の入力チェック
        new_thread_name = request.form.get("thread_name").strip()
        if new_thread_name == "":
            thread_id_str = request.form.get("hidden_thread_id")
            if thread_id_str == "None":
                thread_id = None
                message_list = []
                thread_name = ""
            else:
                thread_id = int(thread_id_str)
                # メッセージ履歴を取得
                message_list = get_chat_message_history(g.user_id, thread_id)
                # スレッド名を取得
                thread_name = get_chat_thread_name(g.user_id, thread_id)
            logger.info("終了(スレッド名未入力)")
            return render_template('chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = thread_id, message_list = message_list, prompt = "", thread_name = thread_name)
            
        # スレッドが未作成の場合は新規作成
        thread_id_str = request.form.get("hidden_thread_id")
        if thread_id_str == "None":
            thread_id = create_chat_thread(g.user_id, new_thread_name)
        # スレッドが存在する場合はスレッド名変更
        else:
            thread_id = int(thread_id_str)
            change_chat_thread_name(g.user_id, thread_id, new_thread_name)

        # メッセージ履歴を取得
        message_list = get_chat_message_history(g.user_id, thread_id)

        # スレッド名を取得
        thread_name = get_chat_thread_name(g.user_id, thread_id)

        logger.info("終了")
        return render_template('chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = thread_id, message_list = message_list, prompt = "", thread_name = thread_name)

    except Exception as e:
        log_user_action(g.user_id, "chat_change_thread_name", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# チャット画面でプロンプト送信
@app.route('/chat_exec_prompt', methods=['POST'])
def chat_exec_prompt():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "chat_exec_prompt", request.path, request.method)

        # プロンプトの入力チェック
        # 未入力の場合は何もしない(スレッド付きの場合は、スレッドのメッセージ履歴・名前セット)
        prompt = request.form.get("chat_prompt").strip()
        if prompt == "":
            thread_id_str = request.form.get("hidden_thread_id")
            if thread_id_str == "None":
                thread_id = None
                message_list = []
                thread_name = ""
            else:
                thread_id = int(thread_id_str)
                # メッセージ履歴を取得
                message_list = get_chat_message_history(g.user_id, thread_id)
                # スレッド名を取得
                thread_name = get_chat_thread_name(g.user_id, thread_id)
            logger.info("終了(プロンプト未入力)")
            return render_template('chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = thread_id, message_list = message_list, prompt = "", thread_name = thread_name)

        # スレッドが未作成の場合は新規作成(スレッド名はプロンプトの先頭20文字)
        thread_id_str = request.form.get("hidden_thread_id")
        current_time = datetime.now(jst).isoformat()  # 現在時刻を取得
        
        if thread_id_str == "None":
            thread_id = create_chat_thread(g.user_id, request.form.get("chat_prompt")[0:20])
        else:
            thread_id = int(thread_id_str)
        
        # プロンプト実行
        result_message = exec_chat_prompt(g.user_id, thread_id, request.form.get("chat_prompt"))
        
        # スレッドの最終更新日時を更新
        update_thread_last_updated(g.user_id, thread_id, current_time)
        
        # メッセージ履歴を取得
        message_list = get_chat_message_history(g.user_id, thread_id)
        # スレッド名を取得
        thread_name = get_chat_thread_name(g.user_id, thread_id)

        # メッセージ履歴を設定してチャット画面を表示
        logger.info("終了")
        return render_template('chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_id = thread_id, message_list = message_list, prompt = "", thread_name = thread_name)
    
    except Exception as e:
        log_user_action(g.user_id, "chat_exec_prompt", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()

# チャット履歴画面
@app.route('/chat_history', methods=['GET'])
def chat_history():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "chat_history", request.path, request.method)

        # スレッドリストを取得（すでにソート済みなのでsortedは不要）
        thread_list = get_chat_thread_list(g.user_id)
        
        # スレッドリストを設定してチャット履歴画面を表示
        logger.info("終了")
        return render_template('chat_history.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_list = thread_list)

    except Exception as e:
        log_user_action(g.user_id, "chat_history", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()

# チャット履歴画面でクリップ設定した場合
@app.route('/chat_history_clip_thread', methods=['POST'])
def chat_history_clip_thread():
    try:
        logger.info("開始)")

        # リクエストデータの取得
        thread_id = int(request.form.get("hidden_thread_id"))
        log_user_action(g.user_id, f"chat_history_clip_thread(thread_id={thread_id})", 
                       request.path, request.method)

        if request.form.get("hidden_is_clipped") == "True":
            is_clipped = True
        else:
            is_clipped =False
        
        # クリップの設定/解除
        clip_chat_thread(g.user_id, thread_id, is_clipped)
        # スレッドリストを取得
        thread_list = get_chat_thread_list(g.user_id)
        # スレッドリストを設定してチャット履歴画面を表示
        logger.info("終了")
        return render_template('chat_history.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_list = thread_list)

    except Exception as e:
        log_user_action(g.user_id, f"chat_history_clip_thread(thread_id={thread_id})", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# チャット履歴画面でスレッド削除
@app.route('/chat_history_del_thread', methods=['POST'])
def chat_history_del_thread():
    try:
        logger.info("開始")
        
        # スレッド削除
        thread_id = int(request.form.get("hidden_thread_id"))
        log_user_action(g.user_id, f"chat_history_del_thread(thread_id={thread_id})", 
                       request.path, request.method)
        delete_chat_thread(g.user_id, thread_id)
        # スレッドリストを取得
        thread_list = get_chat_thread_list(g.user_id)
        
        # スレッドリストを設定してチャット履歴画面を表示
        logger.info("終了")
        return render_template('chat_history.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), thread_list = thread_list)    

    except Exception as e:
        log_user_action(g.user_id, f"chat_history_del_thread(thread_id={thread_id})", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# プロンプトテンプレート画面
@app.route('/chat_prompt_template', methods=['GET'])
def chat_prompt_template():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "chat_prompt_template", request.path, request.method)
        
        # テンプレートリストを作成
        favorite_prompt_template_list, prompt_template_list = create_template_list()
        
        # プロンプトテンプレートリストを設定してプロンプトテンプレート画面表示
        logger.info("終了")
        return render_template('chat_prompt_template.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), favorite_prompt_template_list = favorite_prompt_template_list,  prompt_template_list = prompt_template_list)

    except Exception as e:
        log_user_action(g.user_id, "chat_prompt_template", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# プロンプトテンプレート画面でお気に入り登録
@app.route('/chat_prompt_template_favorite/<string:is_system_template>/<int:prompt_template_no>/<string:is_favorite>', methods=['GET'])
def chat_prompt_template_favorite(is_system_template, prompt_template_no, is_favorite):
    try:
        logger.info(f"開始(is_system_template={is_system_template}, prompt_template_no={prompt_template_no}, is_favorite={is_favorite})")
        log_user_action(g.user_id, "chat_prompt_template_favorite", request.path, request.method)

        if is_system_template == "True":
            bln_is_system_template = True
        else:
            bln_is_system_template = False
            
        if is_favorite == "True":
            bln_is_favorite = True
        else:
            bln_is_favorite = False
        favorite_prompt_template(g.user_id, bln_is_system_template, prompt_template_no, bln_is_favorite)
        
        # テンプレートリストを作成
        favorite_prompt_template_list, prompt_template_list = create_template_list()

        # テンプレートリストを設定してプロンプトテンプレート画面表示
        logger.info("終了")
        return render_template('chat_prompt_template.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), favorite_prompt_template_list = favorite_prompt_template_list,  prompt_template_list = prompt_template_list)

    except Exception as e:
        log_user_action(g.user_id, "chat_prompt_template_favorite", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# カスタムプロンプトテンプレートを追加
@app.route('/chat_prompt_template_add', methods=['POST'])
def chat_prompt_template_add():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "chat_prompt_template_add", request.path, request.method)
        
        # カスタムテンプレート追加
        template_category = "カスタム"
        template_name = request.form.get("hidden_template_name")
        template_description = ""
        prompt_message = request.form.get("hidden_prompt_message")
        add_custom_prompt_template(g.user_id, template_category, template_name, template_description, prompt_message)

        # テンプレートリストを作成
        favorite_prompt_template_list, prompt_template_list = create_template_list()

        # テンプレートリストを設定してプロンプトテンプレート画面表示
        logger.info("終了")
        return render_template('chat_prompt_template.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), favorite_prompt_template_list = favorite_prompt_template_list,  prompt_template_list = prompt_template_list)

    except Exception as e:
        log_user_action(g.user_id, "chat_prompt_template_add", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# カスタムプロンプトテンプレート削除
@app.route('/chat_custom_prompt_template_delete', methods=['POST'])
def chat_custom_prompt_template_delete():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "chat_custom_prompt_template_delete", request.path, request.method)
        
        # カスタムテンプレート削除
        template_no = int(request.form.get("hidden_prompt_template_no"))
        delete_custom_prompt_template(g.user_id, template_no)

        # テンプレートリストを作成
        favorite_prompt_template_list, prompt_template_list = create_template_list()

        # テンプレートリストを設定してプロンプトテンプレート画面表示
        logger.info("終了")
        return render_template('chat_prompt_template.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), favorite_prompt_template_list = favorite_prompt_template_list,  prompt_template_list = prompt_template_list)

    except Exception as e:
        log_user_action(g.user_id, "chat_custom_prompt_template_delete", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()
        
# 高度チャット画面
@app.route('/advanced_chat', methods=['GET'])
def advanced_chat():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "advanced_chat", request.path, request.method)
        # メッセージ履歴を取得
        message_list = get_advanced_chat_message_history(g.user_id)
        # メッセージ履歴を設定して高度チャット画面を表示
        logger.info("終了")
        return render_template('advanced_chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), message_list = message_list)

    except Exception as e:
        log_user_action(g.user_id, "advanced_chat", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# 高度チャット画面でプロンプト送信
@app.route('/advanced_chat_exec_prompt', methods=['POST'])
def advanced_chat_exec_prompt():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "advanced_chat_exec_prompt", request.path, request.method)
        
        # プロンプトの入力チェック
        # 未入力の場合は何もしない(メッセージ履歴があれば表示)
        prompt = request.form.get("advanced_chat_prompt").strip()
        if prompt == "":
            # メッセージ履歴を取得
            message_list = get_advanced_chat_message_history(g.user_id)
            logger.info("終了(プロンプト未入力)")
            return render_template('advanced_chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), message_list = message_list)

        # 新規チャットか判定
        is_new_chat = request.form.get("advanced_chat_is_new") is not None
        # プロンプト実行
        result_message = exec_advanced_chat_prompt(g.user_id, request.form.get("advanced_chat_prompt"), is_new_chat)
        # メッセージ履歴を取得
        message_list = get_advanced_chat_message_history(g.user_id)
        # メッセージ履歴を設定して高度チャット画面を表示
        logger.info("終了")
        return render_template('advanced_chat.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), message_list = message_list, prompt = "")
    
    except Exception as e:
        log_user_action(g.user_id, "advanced_chat_exec_prompt", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# AIクローン画面
@app.route('/ai_clone', methods=['GET', 'POST'])
def ai_clone():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "ai_clone", request.path, request.method)
        # メッセージ履歴を取得
        message_list = get_ai_clone_message_history(g.user_id)
        # メッセージ履歴を設定してAIクローン画面を表示
        logger.info("終了")
        return render_template('ai_clone.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), message_list = message_list)

    except Exception as e:
        log_user_action(g.user_id, "ai_clone", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# AIクローン画面でプロンプト送信
@app.route('/ai_clone_exec_prompt', methods=['POST'])
def ai_clone_exec_prompt():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "ai_clone_exec_prompt", request.path, request.method)

        # プロンプトの入力チェック
        # 未入力の場合は何もしない(メッセージ履歴があれば表示)
        prompt = request.form.get("ai_clone_prompt").strip()
        if prompt == "":
            # メッセージ履歴を取得
            message_list = get_ai_clone_message_history(g.user_id)
            logger.info("終了(プロンプト未入力)")
            return render_template('ai_clone.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), message_list = message_list)
        
        # 新規チャットか判定
        is_new_chat = request.form.get("ai_clone_is_new") is not None
        # プロンプト実行
        result_message = exec_ai_clone_prompt(g.user_id, request.form.get("ai_clone_prompt"), is_new_chat)
        # メッセージ履歴を取得
        message_list = get_ai_clone_message_history(g.user_id)
        # メッセージ履歴を設定してAIクローン画面を表示
        logger.info("終了")
        return render_template('ai_clone.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), message_list = message_list, prompt = "")
    
    except Exception as e:
        log_user_action(g.user_id, "ai_clone_exec_prompt", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# 社内情報検索画面
@app.route('/internal_search', methods=['GET'])
def internal_search():
    try:
        logger.info("開始")
        doc_name = "社内規程"
        doc_id = None
        logger.info("終了")
 
        return render_template('internal_search.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_name=doc_name, doc_id=doc_id, prompt=None, internal_search_result=None)
 
    except Exception as e:
        return common_error_handling()
 
 
# 社内情報カスタム検索画面
@app.route('/internal_custom_search/<string:doc_id>', methods=['GET'])
def internal_custom_search(doc_id):
    try:
        logger.info(f"開始(doc_id={doc_id})")
 
        # ドキュメント名を取得
        doc_name = get_internal_custom_search_doc_name(g.user_id, doc_id)
 
        # メッセージ履歴を設定してチャット画面を表示
        logger.info("終了")
        return render_template('internal_search.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_name=doc_name, doc_id=doc_id, prompt=None, internal_search_result=None)
 
    except Exception as e:
        return common_error_handling()
 
 
# 社内情報カスタム検索のドキュメント一覧画面
@app.route('/internal_custom_search_doc', methods=['GET'])
def internal_custom_search_doc():
    try:
        logger.info("開始")
 
        # 社内情報カスタム検索のドキュメント一覧を取得
        doc_list = sorted(get_internal_custom_search_doc_list(g.user_id))
 
        # ドキュメント一覧を設定してカスタム検索画面を表示
        logger.info("終了")
        return render_template('internal_custom_search_doc.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_list=doc_list)
 
    except Exception as e:
        return common_error_handling()
 
# 社内情報カスタム検索画面でクリップ設定
@app.route('/internal_custom_search_doc_upload', methods=["POST"])
def internal_custom_search_doc_upload():
    try:
        logger.info("開始)")
 
        doc = request.files.get('internal_custom_search_upload_doc')
 
        # ファイルが選択されている場合はドキュメント追加、未選択の場合は何もしない
        if doc.filename != "":
            # ドキュメント追加
            add_internal_custom_search_doc(g.user_id, doc.filename, doc)
 
        # 社内情報カスタム検索のドキュメント一覧を取得
        doc_list = sorted(get_internal_custom_search_doc_list(g.user_id))
 
        # ドキュメント一覧を設定してカスタム検索画面を表示
        logger.info("終了")
        return render_template('internal_custom_search_doc.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_list=doc_list)
 
    except Exception as e:
        return common_error_handling()
 
 
# 社内情報カスタム検索画面でクリップ設定
@app.route('/internal_custom_search_clip_doc', methods=['POST'])
def internal_custom_search_clip_doc():
    try:
        logger.info("開始)")
 
        # リクエストデータの取得
        doc_id = request.form.get("hidden_doc_id")
        if request.form.get("hidden_is_clipped") == "True":
            is_clipped = True
        else:
            is_clipped =False
 
        # クリップの設定/解除
        clip_internal_custom_search_doc(g.user_id, doc_id, is_clipped)
 
        # 社内情報カスタム検索のドキュメント一覧を取得
        doc_list = sorted(get_internal_custom_search_doc_list(g.user_id))
 
        # ドキュメント一覧を設定してカスタム検索画面を表示
        logger.info("終了")
        return render_template('internal_custom_search_doc.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_list=doc_list)
 
    except Exception as e:
        return common_error_handling()
 
 
# 社内情報カスタム検索画面でドキュメント削除
@app.route('/internal_custom_search_del_doc', methods=['POST'])
def internal_custom_search_del_doc():
    try:
        logger.info("開始")
 
        # ドキュメント削除
        doc_id = request.form.get("hidden_doc_id")
        delete_internal_custom_search_doc(g.user_id, doc_id)
 
        # 社内情報カスタム検索のドキュメント一覧を取得
        doc_list = sorted(get_internal_custom_search_doc_list(g.user_id))
 
        # ドキュメント一覧を設定してカスタム検索画面を表示
        logger.info("終了")
        return render_template('internal_custom_search_doc.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_list=doc_list)
 
    except Exception as e:
        return common_error_handling()
 
 
# 社内情報検索画面でプロンプト送信
@app.route('/internal_search_exec_prompt', methods=['POST'])
def internal_search_exec_prompt():
    try:
        logger.info("開始")
 
        # ドキュメント情報取得
        doc_name = request.form.get("hidden_doc_name")
        doc_id = request.form.get("hidden_doc_id")
        if doc_id == "None":
            doc_id = None
 
        # プロンプトの入力チェック
        # 未入力の場合は何もしない
        prompt = request.form.get("internal_search_prompt").strip()
        if prompt == "":
            logger.info("終了(プロンプト未入力)")
            return render_template('internal_search.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_name=doc_name, doc_id=doc_id, prompt=None, internal_search_result=None)
 
        if doc_id is None:
            # プロンプト実行
            internal_search_result = exec_internal_search_prompt(g.user_id, prompt)
        else:
            # カスタム検索でプロンプト実行
            internal_search_result = exec_internal_custom_search_prompt(g.user_id, doc_id, prompt)
 
        # 検索結果を設定してデータ分析画面を表示
        logger.info("終了")
        return render_template('internal_search.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), clipped_doc_list = sorted(get_internal_custom_search_clipped_doc_list(g.user_id)), doc_name=doc_name, doc_id=doc_id, prompt=prompt, internal_search_result=internal_search_result)
 
    except Exception as e:
        return common_error_handling()


# Web検索画面
@app.route('/web_search', methods=['GET', 'POST'])
def web_search():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "web_search", request.path, request.method)
        logger.info("終了")
        return render_template('web_search.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id))

    except Exception as e:
        log_user_action(g.user_id, "web_search", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()


# データ分析画面
@app.route('/analysis', methods=['GET'])
def analysis():
    try:
        logger.info("開始")
        logger.info("終了")
        return render_template('analysis.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), prompt=None, analysis_result=None)
 
    except Exception as e:
        return common_error_handling()
 
 
# データ分析画面でプロンプト送信
@app.route('/analysis_exec_prompt', methods=['POST'])
def analysis_exec_prompt():
    try:
        logger.info("開始")
 
        # プロンプトの入力チェック
        # 未入力の場合は何もしない(メッセージ履歴があれば表示)
        prompt = request.form.get("analysis_prompt").strip()
        if prompt == "":
            logger.info("終了(プロンプト未入力)")
            return render_template('analysis.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id), prompt=None, analysis_result=None)
        # プロンプト実行
        analysis_result = exec_analysis_prompt(g.user_id, prompt)
 
        # いずれかのステータスが異常な場合はエラーを発生させる
        if analysis_result.sql_status != "OK" or analysis_result.data_status != "OK" or analysis_result.graph_status != "OK" or analysis_result.insight_status != "OK":
            raise Exception(f'SQL={analysis_result.sql_message} | Data={analysis_result.data_message} | Graph={analysis_result.graph_message} | Insight={analysis_result.insight_message}')
 
        # 分析結果を設定してデータ分析画面を表示
        logger.info("終了")
        return render_template('analysis.html', clipped_thread_list = sorted(get_chat_clipped_thread_list(g.user_id)), prompt=prompt, analysis_result=analysis_result)
    except Exception as e:
        return common_error_handling()


# 画像生成画面
@app.route('/image_gen', methods=['GET', 'POST'])
def image_gen():
    try:
        logger.info("開始")
        log_user_action(g.user_id, "image_gen", request.path, request.method)
        raise ValueError("エラーのテストです。") ###暫定処理###
        logger.info("終了")
        return render_template('image_gen.html', clipped_thread_list = get_chat_clipped_thread_list(g.user_id))

    except Exception as e:
        log_user_action(g.user_id, "image_gen", request.path, request.method, 
                       status="error", error_message=str(e))
        return common_error_handling()