from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader(
    "framework.pdf",
    mode="page"  
)

docs = loader.load()


# print(docs[0].page_content)


# print(docs[0].metadata)

merged_text = ""
page_offsets = {}
current_length = 0

for doc in docs:
    page_num = doc.metadata["page"]
    marker = f"\n\n[[PAGE_{page_num}]]\n\n"
    
    page_offsets[page_num] = current_length
    merged_text += marker + doc.page_content.strip()
    
    current_length = len(merged_text)


print(merged_text[:1003])
print(type(merged_text))  # should be str