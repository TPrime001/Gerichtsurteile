from load_dataset import load_wikidata, clean_wikidata
from PreprocessGU import preprocesss, count_tokens, max_count_token
from collections import defaultdict
from os import path
import pickle

def indexing(textlist, AZ):
    index = defaultdict(lambda : defaultdict(int))


    for AZ_no, text in enumerate(textlist):
        tokens = preprocesss(text)

        if len(tokens) == 0:
            continue
        token_counts = count_tokens(tokens)
        max_token_count = max_count_token(token_counts)
        token_set = token_counts.keys()

        for token in token_set:
            tf = token_counts[token] / max_token_count
            number = AZ[AZ_no]
            index[token][number] += tf

    return index

    with open("index.pickle", "wb") as f:
        pickle.dump(index, f)

AZ2 = ["1tghj", "baum"]
text = ["<p>Der Versamml Antragsteller wird durch die noch im Streit stehende Beschränkung nicht in eigenen Rechten verletzt. Weder die Versammlungsfreiheit des Art. <a href=\"http://dejure.org/gesetze/GG/8.html\" rel=\"nofollow\" title=\"Art. 8 GG\">8</a> Abs. 1 GG noch andere Grundrechte - wie namentlich die Meinungsfreiheit aus Art. <a href=\"http://dejure.org/gesetze/GG/5.html\" rel=\"nofollow\" title=\"Art. 5 GG\">5</a> Abs. 1 Satz 1 Hs. 1 GG oder die" , " allgemeine Handlungsfreiheit nach Art. <a href=\"http://dejure.org/gesetze/GG/2.html\" rel=\"nofollow\" title=\"Art. 2 GG\">2</a> Abs. 1 GG - verleihen dem Veranstalter einer Versammlung - wie hier dem Antragsteller - von ihrem Schutzgehalt her einen Anspruch darauf, ausländischen Staatsoberhäuptern oder Regierungsmitgliedern die Gelegenheit zu geben, in der Bundesrepublik Deutschland im Rahmen öffentlicher Versammlungen in ihrer Funktion als Staatsoberhaupt bzw. Regierungsmitglied zu politischen Themen zu sprechen.</p>"]
print(indexing(text, AZ2))