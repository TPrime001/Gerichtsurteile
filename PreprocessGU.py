import nltk
import nltk.stem.snowball as snow
from nltk.corpus import stopwords
import re
from load_dataset import clean_wikidata

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


text = "<p>Der Antragsteller wird durch die noch im Streit stehende Beschränkung nicht in eigenen Rechten verletzt. Weder die Versammlungsfreiheit des Art. <a href=\"http://dejure.org/gesetze/GG/8.html\" rel=\"nofollow\" title=\"Art. 8 GG\">8</a> Abs. 1 GG noch andere Grundrechte - wie namentlich die Meinungsfreiheit aus Art. <a href=\"http://dejure.org/gesetze/GG/5.html\" rel=\"nofollow\" title=\"Art. 5 GG\">5</a> Abs. 1 Satz 1 Hs. 1 GG oder die allgemeine Handlungsfreiheit nach Art. <a href=\"http://dejure.org/gesetze/GG/2.html\" rel=\"nofollow\" title=\"Art. 2 GG\">2</a> Abs. 1 GG - verleihen dem Veranstalter einer Versammlung - wie hier dem Antragsteller - von ihrem Schutzgehalt her einen Anspruch darauf, ausländischen Staatsoberhäuptern oder Regierungsmitgliedern die Gelegenheit zu geben, in der Bundesrepublik Deutschland im Rahmen öffentlicher Versammlungen in ihrer Funktion als Staatsoberhaupt bzw. Regierungsmitglied zu politischen Themen zu sprechen.</p>"

print (preprocesss(text))