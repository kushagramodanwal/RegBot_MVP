from langchain.vectorstores import Chroma


def create_vector_store(documents, embeddings):

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    vectorstore.persist()

    return vectorstore