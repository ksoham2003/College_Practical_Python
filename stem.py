import nltk

from nltk.stem import PorterStemmer

w = PorterStemmer()

print(w.stem("eating"))
