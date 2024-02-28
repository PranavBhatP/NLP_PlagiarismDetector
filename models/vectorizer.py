from model import getData
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import chromadb
from model import Res_Paper
import os

# Initialize NLTK resources
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Load your dataset using your getData function
dataset = getData('./models/data')

# Define the name of the embedding model
embedding_model_name = "all-mpnet-base-v2"

# Path to the directory for ChromaDB persistent storage
chromadb_dir = "./models/chromadb_document_store"

# Create the directory if it doesn't exist
if not os.path.exists(chromadb_dir):
    os.makedirs(chromadb_dir)

# Connect to the local ChromaDB instance with PersistentClient
client = chromadb.PersistentClient(path=chromadb_dir)

# Create a ChromaDB collection
collection = client.get_or_create_collection("new_collection")

# Function to vectorize and store the data into ChromaDB
def vectorize_and_store(dataset, collection):
    for paper_no, paper in enumerate(dataset, 1):
        words = word_tokenize(paper.text)
        lemmatized_words = [lemmatizer.lemmatize(w) for w in words if w.lower() not in stop_words]
        document = " ".join(lemmatized_words)
        metadata = {"title": paper.title, "number": paper.number}
        id_ = f"id{paper_no}"
        collection.add(documents=[document], metadatas=[metadata], ids=[id_])

# Vectorize and store the dataset into ChromaDB
vectorize_and_store(dataset, collection)

print("Data vectorization and storage completed.")
