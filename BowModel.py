from sklearn.feature_extraction.text import CountVectorizer
#一个语料库
corpus = [
    'This the the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = CountVectorizer(ngram_range=(2,2))

X = vectorizer.fit_transform(corpus)
print("词汇：索引",vectorizer.vocabulary_)
print("句子的向量：")
print(X.toarray())#元素为每个词出现的次数
