Day 2: Building the Knowledge Base

Today, we transform documents (e.g., policies, contracts, audit standards) into a smart knowledge base that AIDE can query efficiently.

Steps:





Chunking: Split documents into smaller segments (e.g., paragraphs or sentences) using langchain.text_splitter to preserve context.

from langchain.text_splitter import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(document_text)



Embedding: Convert chunks into numerical vectors using sentence-transformers.

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)



Vector Store: Store embeddings in ChromaDB for fast semantic search.

import chromadb
client = chromadb.Client()
collection = client.create_collection("aide_knowledge_base")
collection.add(embeddings=embeddings, documents=chunks, ids=[f"chunk_{i}" for i in range(len(chunks))])



Querying: Process user questions by converting them to embeddings and retrieving relevant chunks.

Next Steps: In Day 3, we’ll integrate an AI model to process queries and generate answers.
