from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def tfidf(data_set) :
    count_vect = CountVectorizer()
    text_data = [ (data_set[i].text) for i in range(len(data_set))]
    term_freq_matrix = count_vect.fit_transform(text_data)

    tfidf = TfidfTransformer()
    tf_idf_matrix = tfidf.fit_transform(term_freq_matrix)
    return tf_idf_matrix

