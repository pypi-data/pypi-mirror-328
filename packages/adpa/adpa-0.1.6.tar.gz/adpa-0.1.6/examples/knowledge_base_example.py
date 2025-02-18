"""
Example usage of the KnowledgeBase class.
"""
from adpa.knowledge.vectorstore import KnowledgeBase

def main():
    # Initialize knowledge base
    kb = KnowledgeBase(
        persist_directory="./data/knowledge_base",
        chunk_size=500,  # Smaller chunks for this example
        chunk_overlap=50
    )

    # Add documents from docs directory
    kb.add_documents("./docs", glob_pattern="**/*.md")

    # Example queries
    print("Querying about testing practices...")
    results = kb.query(
        "What are our testing best practices?",
        num_results=3
    )
    for doc in results:
        print(f"\nSource: {doc.metadata.get('source')}")
        print(f"Content: {doc.page_content[:200]}...")

    # Similarity search example
    print("\nFinding similar documents about API usage...")
    similar_docs = kb.similarity_search(
        "How to use the REST API?",
        k=2,
        metadata_filter={"category": "api"}
    )
    for doc in similar_docs:
        print(f"\nSource: {doc.metadata.get('source')}")
        print(f"Content: {doc.page_content[:200]}...")

if __name__ == "__main__":
    main()
