import pickle
from PreprocessGU import preprocesss
from collections import defaultdict
from Query_IBSearch import filteroutput, filtershortcuts, info
import re, os
#sa = input ("Geben sie eie Suchanfrage ein\n ")

def suche (sa):
    sa = filtershortcuts(sa)
    sa=sa[0:re.match('.+"',sa).span()[1]-1]
    qtokens = preprocesss(sa)
    index = dict
    for token in qtokens:
        if os.path.exists("index/w/"+token+".pickle"):
            with open("index/"+token+".pickle", "rb") as f:
                index[token] = pickle.load(f)
    resultdict = defaultdict(float)
    results2 = []
    for w in qtokens:
        for az in index[w]:
            resultdict[az]+=index[w][az]
#    for token, val in index:
#        for w in qtokens:
#            if token == w:
#                results2 += index[token]
#                for AZ_no in results2:
#                    resultdict[AZ_no]+=index[token][AZ_no]

    return (resultdict)
    #resultlist = set(resultlist)
    ranked = sorted(resultdict, key = resultdict.get, reverse=True)

    for key in ranked:
        rankedkeys+= key

    return (rankedkeys)
