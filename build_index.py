from PreprocessGU import preprocesss, count_tokens, max_count_token
from collections import defaultdict
from os import path
import pickle
import math
import os

index = defaultdict(dict)

def indexing(textlist, AZ):
    N = len(AZ)
    if N != len(textlist):
        print ("Error Länge")
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
            if index[token].get(number, 0):
                index[token][number] += tf
            else:
                index[token][number] = tf
    for woerter in index:
        n = len(index[woerter])
        idf = math.log10(N/n)
        for docid in index[woerter]:
            tfidf = index[woerter][docid] * idf
            index[woerter][docid] = tfidf
        newpath="index/w/"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        with open("index/w/"+woerter+".pickle", "wb") as f:
            pickle.dump(index[woerter], f)


