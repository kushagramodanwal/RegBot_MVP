def search_framework(vectorstore, query):

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )

    results = retriever.get_relevant_documents(query)

    return results