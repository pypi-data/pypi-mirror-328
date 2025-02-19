from outerport import OuterportClient

client = OuterportClient(api_key="my_secret_key", base_url="http://localhost:8080")

# 1. Create a Document (synchronously waits for processing to finish)
with open("y03.pdf", "rb") as f:
    doc = client.documents.create(file=f, file_name="myfile.pdf")

print("Doc ID:", doc.id)
print("Summary:", doc.summary)
print("Document:", doc)

# 2. Reload it if you want the freshest data
doc.reload()

print("Document:", doc)

# 3. List all documents
all_docs = client.documents.list()
for d in all_docs:
    print(d.id, d.name)

# 4. Ask a Question about the doc
question = client.questions.create(
    user_id=1,
    document_ids=[doc.id],
    question="Things to deal with regarding money laundering",
)
print("Answer:", question.final_answer)

import pdb

pdb.set_trace()

# 5. If you want to delete the doc
response = doc.delete()
print("Deleted doc response:", response)
