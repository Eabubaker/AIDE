import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import PyPDF2  # For handling PDF documents
from tqdm import tqdm

# Step 1: Load and preprocess a sample document
def load_document(file_path):
    """
    Load a document (e.g., PDF or text) and return its content.
    For this example, we assume a PDF file of audit standards.
    """
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error loading document: {e}")
        return None

# Step 2: Chunk the document
def chunk_text(text, chunk_size=500, chunk_overlap=50):
    """
    Split the document into smaller chunks for processing.
    Uses LangChain's text splitter to preserve context.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return splitter.split_text(text)

# Step 3: Generate embeddings
def generate_embeddings(chunks):
    """
    Convert text chunks into numerical vectors using Sentence Transformers.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight model
    embeddings = [model.encode(chunk) for chunk in tqdm(chunks, desc="Generating embeddings")]
    return embeddings

# Step 4: Store in ChromaDB
def store_in_vector_db(chunks, embeddings, collection_name="aide_knowledge_base"):
    """
    Store chunks and their embeddings in ChromaDB for semantic search.
    """
    client = chromadb.Client()
    try:
        # Create or get collection
        collection = client.get_or_create_collection(name=collection_name)
        
        # Add chunks and embeddings
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"chunk_{i}" for i in range(len(chunks))]
        )
        print(f"Stored {len(chunks)} chunks in ChromaDB collection '{collection_name}'")
        return collection
    except Exception as e:
        print(f"Error storing in ChromaDB: {e}")
        return None

# Step 5: Query the knowledge base
def query_knowledge_base(query, collection, top_k=3):
    """
    Query the knowledge base with a question and retrieve relevant chunks.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query)
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    # Extract relevant chunks
    relevant_chunks = results['documents'][0]
    return relevant_chunks

def main():
    # Sample document path (replace with your audit standards PDF)
    file_path = "audit_standards.pdf"
    
    # Step 1: Load document
    document_text = load_document(file_path)
    if not document_text:
        return
    
    # Step 2: Chunk the document
    chunks = chunk_text(document_text)
    print(f"Created {len(chunks)} chunks")
    
    # Step 3: Generate embeddings
    embeddings = generate_embeddings(chunks)
    
    # Step 4: Store in ChromaDB
    collection = store_in_vector_db(chunks, embeddings)
    if not collection:
        return
    
    # Step 5: Test query
    sample_query = "What should the Chief Audit Executive do if the internal audit function cannot comply with standards?"
    results = query_knowledge_base(sample_query, collection)
    
    print("\nQuery Results:")
    for i, chunk in enumerate(results, 1):
        print(f"Result {i}: {chunk[:200]}...")  # Print first 200 chars of each result

if __name__ == "__main__":
    main()
