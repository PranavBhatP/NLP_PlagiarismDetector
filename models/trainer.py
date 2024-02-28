import gensim 
from model import Res_Paper, getData
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import chromadb
# Load NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Load stop words
stop_words = set(stopwords.words('english'))

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load text
dataset = getData("./data")

#Load the chroma vector database.
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection") 

for paper_no in range(len(dataset)):
    words = word_tokenize(dataset[paper_no].text)
    lemmatized_words = [lemmatizer.lemmatize(w) for w in words if w.lower() not in stop_words]
    collection.add (
        documents = [" ".join(lemmatized_words)],
        metadatas = [{"title": dataset[paper_no].title, "number": dataset[paper_no].number}],
        ids = [f"id{paper_no+1}"],
    )

def check_plag(query_doc):
    words = word_tokenize(query_doc.text)
    lemmatized_words = [lemmatizer.lemmatize(w) for w in words if w.lower() not in stop_words]
    results = collection.query(
        query_texts=["".join(lemmatized_words)],
        n_results=2
    )
# # Tokenize text into words
# words = word_tokenize(txt)

# # Remove stop words and lemmatize
# lemmatized_words = [lemmatizer.lemmatize(w) for w in words if w.lower() not in stop_words]


