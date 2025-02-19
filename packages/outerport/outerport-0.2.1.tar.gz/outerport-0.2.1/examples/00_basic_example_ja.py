from outerport import OuterportClient
from halo import Halo

client = OuterportClient(api_key="my_secret_key", base_url="http://localhost:8080")

# 1. ドキュメントを作成
with Halo(text="ドキュメントをアップロード・処理中", spinner="dots") as spinner:
    with open("y03.pdf", "rb") as f:
        doc = client.documents.create(file=f, file_name="myfile.pdf")
    spinner.succeed("ドキュメントを作成しました")

print("ドキュメントID:", doc.id)

# 2. ドキュメントを再読み込みしたい場合はreload()を呼び出してください
doc.reload()

# 3. ドキュメントを一覧表示したい場合はlist()を呼び出してください
all_docs = client.documents.list()
print()
print("ドキュメント一覧（一部）：")
for d in all_docs[:3]:
    print(f"Document ID: {d.id:<10} Name: {d.name}")

question_text = "マネーロンダリングに関することを教えてください"

print()
# 4. ドキュメントに関する質問をしたい場合はcreate()を呼び出してください
with Halo(text="質問をしています", spinner="dots") as spinner:
    question = client.questions.create(
        user_id=1, document_ids=[doc.id], question=question_text
    )
    spinner.succeed("質問をしました")

print()
print("質問:", question.question_text)
print("質問への回答:", question.final_answer)
print()
print("証拠（一部）：")
for evidence in question.evidences[:2]:
    print("証拠:")
    print("    " + evidence.evidence.replace("\n", "\n    "))
    print("理由:")
    print("    " + evidence.reasoning.replace("\n", "\n    "))
print()

# 5. ドキュメントのメタデータを更新したい場合はupdate_metadata()を呼び出してください
with Halo(text="ドキュメントのメタデータを更新中", spinner="dots") as spinner:
    doc.update_metadata(name="myfile_updated.pdf")
    spinner.succeed("ドキュメントのメタデータを更新しました")

# 6. ドキュメントのファイルを更新したい場合はupdate_file()を呼び出してください
with Halo(text="ドキュメントのファイルを更新中", spinner="dots") as spinner:
    with open("y03_updated.pdf", "rb") as f:
        doc.update_file(f, file_name="myfile_updated.pdf")
    spinner.succeed("ドキュメントのファイルを更新しました")

# 7. ドキュメントを削除したい場合はdelete()を呼び出してください
with Halo(text="ドキュメントを削除中", spinner="dots") as spinner:
    response = doc.delete()
    spinner.succeed("ドキュメントを削除しました")
