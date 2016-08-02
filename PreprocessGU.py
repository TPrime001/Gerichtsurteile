import nltk
import nltk.stem.snowball as snow
from nltk.corpus import stopwords
import re


# tokenize creates list of words
def tokenize(text):
    new_text = nltk.word_tokenize(text)
    new_text1 = []
    for item in new_text:
        new_text1 += (re.findall('([\w]+)^(\<a.+\\a>)|(\<[^\>]+\>)', item))

    return new_text1

(\<a.+\\a>)|(\<[^\>]+\>)
# stemming
def stemming(new_text2):
    stemmer = snow.GermanStemmer()
    new_list = []
    for elements in new_text2:
        new_list.append(stemmer.stem(elements))
    return new_list


# stopword removal
def stoppwords(new_list2):
    stop = stopwords.words('german')
    new_words = [word for word in new_list2 if word not in stop]
    return new_words


def preprocesss(data):
    tokens = tokenize(data)
    stemmed = stemming(tokens)
    finaltokens = stoppwords(stemmed)
    return finaltokens
#sd