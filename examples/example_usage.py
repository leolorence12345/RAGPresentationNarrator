"""
Example usage of the RAG Presentation Narrator
"""

from src.pipeline.rag_pipeline import RAGPipeline
from src.agents.narrative_agent import NarrativeAgent


def example_basic_pipeline():
    """Example: Basic pipeline usage"""
    print("Initializing RAG Pipeline...")
    pipeline = RAGPipeline(
        documents_path="data/presentations/",
        cache_enabled=True
    )
    
    # Load documents
    print("Loading documents...")
    documents = pipeline.load_documents()
    print(f"Loaded {len(documents)} documents")
    
    # Create vector store
    print("Creating vector store...")
    pipeline.create_vector_store(documents)
    
    # Generate narrative
    query = "Explain the key concepts from the machine learning presentation"
    print(f"Generating narrative for query: {query}")
    narrative = pipeline.generate_narrative(query)
    print(f"\nNarrative:\n{narrative}")


def example_agent_usage():
    """Example: Using the narrative agent"""
    print("Initializing Narrative Agent...")
    agent = NarrativeAgent(
        prompt_template="src/prompts/narrative_template.txt",
        cache_enabled=True
    )
    
    # Generate narrative
    narrative = agent.create_narrative(
        presentation_id="ml_intro_2024",
        context="machine learning basics",
        query="What are the main concepts?"
    )
    print(f"\nGenerated Narrative:\n{narrative}")


if __name__ == "__main__":
    print("=" * 50)
    print("RAG Presentation Narrator - Example Usage")
    print("=" * 50)
    
    # Run examples
    # example_basic_pipeline()
    # example_agent_usage()
    
    print("\nNote: Uncomment the example functions to run them")
    print("Make sure to:")
    print("1. Add presentation files to data/presentations/")
    print("2. Configure config.yaml with your API keys")
    print("3. Install all dependencies: pip install -r requirements.txt")

