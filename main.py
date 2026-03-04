from parser.loader import load_framework_pdf
from parser.structural_chunking import parse_framework

from rag.document_converter import clauses_to_documents
from rag.embeddings import load_embedding_model
from rag.vector_store import create_vector_store
from rag.retriever import search_framework


def main():

    # Load PDF
    pages = load_framework_pdf("data/framework.pdf")

    # Merge pages
    full_text = ""
    for page in pages:
        full_text += page.page_content + "\n\n"

    # Structural parsing
    clauses = parse_framework(full_text)

    print("Total Clauses:", len(clauses))

    # Convert to documents
    docs = clauses_to_documents(clauses)

    # Load embeddings
    embeddings = load_embedding_model()

    # Create vector database
    vectorstore = create_vector_store(docs, embeddings)

    # Test query
    query = "Can genomic data be shared internationally?"

    results = search_framework(vectorstore, query)

    print("\nTop Results:\n")

    for r in results:

        print("Text:", r.page_content)
        print("Metadata:", r.metadata)
        print("-" * 50)


if __name__ == "__main__":
    main()