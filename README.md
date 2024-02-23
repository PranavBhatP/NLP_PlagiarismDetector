# Intell_Quest_Baseline
Intell Quest hackathon challenges you to develop an innovative research paper plagiarism detection tool. This repository contains the code for the baseline model for Intell Quest Hackathon 2024. In the baseline model we have considered a limited set of documents and the algorithm used for detecting plagiarism is Term Frequency Inverse Document Frequency (TF-IDF). 

## Getting started
Clone the repostory using the command 
```
git clone https://github.com/MeherRushi/Intell_Quest_Baseline.git
```
Run ``python main.py`` and enter the input view the top 5 matching documents.

## Data format
The data is in JSON format it being

```
[ ...
    {
        "abstract": Abstract of the paper
        "articleNumber": Article Number
        "articleTitle": Article title
        "authors": [ ...
            {
                "preferredName": Preferred Name
                "normalizedName": Normalized name
                "firstName": First Name
                "lastName": Last Name
                "searchablePreferredName": Identifying on internet
                ""id": ID
            }
        ...]
        "doi": Date of issuing
        "publicationTitle":  Publication title
        "publicationYear":  Year of Publication
        "publicationVolume": Publication volume
        "publicationIssue": Publication issue
        "volume": Volume Number
        "issue": 
        "documentLink": Link of the document
        "xml": XML of the document
    }
  ...
]
```

## What we want in the hackathon
This hackathon focuses on creating a user-friendly application that effectively identifies plagiarism in IEEE research papers. You will be tasked with building a comprehensive system encompassing: <br />
### Frontend
A user-friendly interface for uploading research papers in common formats (Text file, PDF, docx, etc.).  <br />
### Backend
A robust algorithm that analyzes uploaded papers against a vast database of similar research papers to identify potential plagiarism. Key functionalities include: <br />
**Preprocessing**: Clean and tokenize the text data for efficient analysis.<br /> 
**Feature Extraction**: Extract meaningful features from the text using techniques like TF-IDF or vectorization with powerful language models from Hugging Face.  <br />
**Similarity Comparison**: Employ appropriate similarity metrics (cosine similarity, Euclidean distance, etc.) to assess the degree of resemblance between the uploaded paper and reference documents.  <br />
**Database Management**: Choose a suitable database solution (relational or vector) to store reference documents and their extracted features efficiently.   <br />
**Output**: Generate a clear and concise plagiarism score for the entire paper. Consider these additional features for improved analysis:
Chunk-level analysis: Highlight specific sections with suspected plagiarism and their potential sources.   <br />
**Visualization**: Implement a color-coding system inspired by tools like Turnitin to visually represent plagiarism severity.


### Submission Essentials
#### Core Functionality:
**Frontend**: User-friendly interface for uploading research papers. <br />
**Backend**: Robust similarity comparison against a provided dataset of research papers. <br />
**Database**: Efficient storage and retrieval of data. <br />


#### Beyond the Basics:
While the core functionalities outlined above provide a solid foundation, we encourage you to push the boundaries of innovation and explore enhancements like: <br />
**Accuracy Boosting**: Implement advanced text similarity algorithms, leverage external knowledge sources, or incorporate deep learning models for more precise plagiarism detection. <br />
**Active Learning**: Continuously improve the model by incorporating user feedback and new data. This would also mean adding the newly uploaded data into your already existing database. <br />
**Efficiency Optimization**: Utilize caching, parallel processing, and optimized data structures to improve processing time for large datasets.
**User Experience**: Design an intuitive interface with clear result interpretations and filtering options for sources, similarity thresholds, and plagiarism types. <br />

> **_NOTE:_** This hackathon will provide access to a curated dataset of research papers for training and testing purposes. [Data](http://tinyurl.com/3dpykt5d)

## References
1. [Hugging Face](https://huggingface.co/ )
2. [Qdrant](https://qdrant.tech/)
3. [Universal Sentence Encoder](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder )


