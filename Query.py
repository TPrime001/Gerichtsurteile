import pickle
from PreprocessGU import preprocesss
from collections import defaultdict
from Query_IBSearch import filteroutput, filtershortcuts, info
import re
#sa = input ("Geben sie eie Suchanfrage ein\n ")

def suche(sa):
    if re.findall('.*\".*', sa):
        filtershortcuts(sa)
        sa=sa[0:re.match(re.compile('[^"]+"'),sa).span()[1]-1]
    qtokens = preprocesss(sa)
    with open("index/index.pickle", "rb") as f:
        index = pickle.load(f)
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

    #return (resultdict)
    #resultlist = set(resultlist)
    filteroutput(resultdict)

    ranked = sorted(resultdict, key = resultdict.get, reverse=True)

    urlfile=open("index/urls.pickle","rb")
    url=pickle.load(urlfile)
    urlfile.close()

    rankedkeys=[]
    rankedurls = []
    rankedidfs = []
    for key in ranked:
        rankedkeys.append(key)
        rankedidfs.append(resultdict[key])
        rankedurls.append(url[key])

    return (rankedkeys, rankedurls, rankedidfs)
