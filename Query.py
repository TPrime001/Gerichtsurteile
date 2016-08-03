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

    urlfile=open("index/urls.pickle","rb")
    url=pickle.load(urlfile)
    urlfile.close()

    if sa == "." or sa == ". ":
        for key in url:
            resultdict[key]=0
#    for token, val in index:
#        for w in qtokens:
#            if token == w:
#                results2 += index[token]
#                for AZ_no in results2:
#                    resultdict[AZ_no]+=index[token][AZ_no]

    #return (resultdict)
    #resultlist = set(resultlist)
    resultdict = filteroutput(resultdict)

    ranked = sorted(resultdict, key = resultdict.get, reverse=True)

    urlfile=open("index/urls.pickle","rb")
    url=pickle.load(urlfile)
    urlfile.close()

    ranked_azs=[]
    ranked_urls = []
    ranked_idfs = []
    for key in ranked:
        ranked_azs.append(key)
        ranked_idfs.append(resultdict[key])
        ranked_urls.append(url[key])

    return (ranked_azs, ranked_urls, ranked_idfs)
