import nltk
import nltk.stem.snowball as snow
from nltk.corpus import stopwords
import re
from load_dataset import clean_wikidata
from collections import defaultdict

# tokenize creates list of words
def tokenize(text):
    new_text = nltk.word_tokenize(text)
    new_text1 = []
    for item in new_text:
        new_text1 += (re.findall('([\w]+)', item))

    return new_text1

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


def preprocesss(text2):
    data = clean_wikidata(text2)
    tokens = tokenize(data)
    stemmed = stemming(tokens)
    finaltokens = stoppwords(stemmed)
    return finaltokens

def count_tokens(tokens):
    counter = defaultdict(int)
    for token in tokens:
        counter[token] += 1
    return counter

def max_count_token(token_counts):
     return token_counts[max(token_counts, key=token_counts.get)]
