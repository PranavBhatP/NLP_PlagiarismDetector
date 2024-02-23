from getData import getData, Paper
from tfidf import tfidf
from sklearn.metrics.pairwise import cosine_similarity
import json

user_text = input(str("Enter the text content of document to check for plagiarism: "))
user_title = input(str("Enter the Title: "))
user_abstract = input(str("Enter the abstract: "))
user_articleNumber = input(str("Enter the articleNumber: "))


with open('user_text.json','w') as f:
    obj = {
    "abstract": user_abstract,
    "articleNumber": user_articleNumber,
    "articleTitle": user_title,
    "authors": [  ],
    "doi": "",
    "publicationTitle": "IEEE Access",
    "publicationYear": "",
    "publicationVolume": None,
    "publicationIssue": None,
    "volume": "",
    "issue": None,
    "documentLink": "",
    "xml": user_text
    }
    json.dump(obj,f)

data_set = getData('./data/')
data_set = data_set + [Paper('user_text.json')]

tf_idf_matrix = tfidf(data_set)
similarity_list =[]

for i in range(len(data_set)-1):
    similarity = cosine_similarity(tf_idf_matrix[len(data_set)-1], tf_idf_matrix[i])
    paper_number = data_set[i].json['articleNumber']
    similarity_list.append([similarity[0][0],paper_number])

similarity_list.sort(reverse=True)
# Print the top 5 papers with high similarity between the reference document and the documents in the dataset
for i in range(5):
    print(f'The similarity between text and paper {similarity_list[i][1]} documents is: ',similarity_list[i][0]*100,'%')
    







