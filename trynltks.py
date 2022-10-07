import nltk
from nltk.stem.porter import PorterStemmer 

porter_stemmer  = PorterStemmer()
text = "انتظر الطالب انتظارا منتظرا"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Stemming for {} is {}".format(w,porter_stemmer.stem(w))) 
e_words= ["انتظر", "انتظار", "سينتظر", "ينظر"]
ps =PorterStemmer()
for w in e_words:
    rootWord=ps.stem(w)
    print(rootWord)
