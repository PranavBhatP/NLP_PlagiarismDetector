from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import chromadb
from vectorizer import collection
from model import Res_Paper
import os

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

p = Res_Paper('./models/data/9354795.json')
txt = p.text
query_words = word_tokenize(txt)
lemmatized_query = [lemmatizer.lemmatize(w) for w in query_words if w.lower() not in stop_words]

# Query the ChromaDB collection
results = collection.query(query_texts=[" ".join(lemmatized_query)], n_results=3)

print(results)


