import faiss
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
import os
#os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Load the pre-trained model and tokenizer
model_name = "openai-gpt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Define your documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Generate embeddings for the documents
embeddings = []
for doc in documents:
    inputs = tokenizer(doc, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).numpy()
        embeddings.append(embedding)

# Convert the embeddings to a numpy array
embeddings = np.concatenate(embeddings)

# Build the FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Perform semantic vector search
query = "This is the second document."
query_embedding = []
inputs = tokenizer(query, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    query_embedding = outputs.last_hidden_state.mean(dim=1).numpy()

# Search for similar documents
k = 2  # Number of nearest neighbors to retrieve
D, I = index.search(query_embedding, k)

# Print the results
print("Query:", query)
print("Most similar documents:")
for i, idx in enumerate(I[0]):
    print(f"Document {i+1}: {documents[idx]}")