import pickle
from PreprocessGU import preprocesss
from collections import defaultdict
#sa = input ("Geben sie eie Suchanfrage ein\n ")

def suche (sa):
    qtokens = preprocesss(sa)
    with open("index/index.pickle", "rb") as f:
        index = pickle.load(f)
    resultdict = defaultdict(float)
    results2 = []
    for token in index:
        for w in qtokens:
            if token == w:
                results2 += index[token]
                for AZ_no in results2:
                    resultdict[AZ_no]+=index[token][AZ_no]

    return (resultdict)
    #resultlist = set(resultlist)
    ranked = sorted(resultdict, key = resultdict.get, reverse=True)

    for key in ranked:
        rankedkeys+= key

    return (rankedkeys)


#print(suche("toll"))