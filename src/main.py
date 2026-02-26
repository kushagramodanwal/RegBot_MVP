from loader import load_framework_pdf
from structuralChunking import parse_framework


def main():

    pages = load_framework_pdf("data/framework.pdf")

    full_text = ""
    for page in pages:
        full_text += page.page_content + "\n\n"

    clauses = parse_framework(full_text)

    print("Total Clauses Found:", len(clauses))
    print()

    for clause in clauses:
        print("Document:", clause.document_name)
        print("Section Number:", clause.section_number)
        print("Section Title:", clause.section_title)
        print("Subsection:", clause.subsection)
        print("Text:", clause.clause_text)
        print("-" * 60)


if __name__ == "__main__":
    main()