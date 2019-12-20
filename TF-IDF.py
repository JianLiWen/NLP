from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = TfidfVectorizer()
#设置小数点的位数为2
np.set_printoptions(2)
X = vectorizer.fit_transform(corpus)
#词汇表
print(vectorizer.vocabulary_)
print(X.toarray())
