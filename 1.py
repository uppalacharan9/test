from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
print(stemmer.stem("eating"))
print(stemmer.stem("eatables"))
print(stemmer.stem("ahditive"))