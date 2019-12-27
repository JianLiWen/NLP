#import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn
print(wn.synsets("computer"))
print(wn.synset('computer.n.01').definition())
print(wn.synset('computer.n.01').examples())
print(wn.synset('computer.n.01').lemma_names())
com = wn.synset("girl.n.01")
mac = wn.synset("woman.n.01")
print(com.path_similarity(mac))
