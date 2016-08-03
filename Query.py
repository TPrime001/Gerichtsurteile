import pickle
from PreprocessGU import preprocesss
from collections import defaultdict
#sa = input ("Geben sie eie Suchanfrage ein\n ")

def suche (sa):
    qtokens = preprocesss(sa)
    with open("index.pickle", "rb") as f:
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
'''for integ in sorted(resultlist):
    dicte[integ]+=1
print(dicte)
liste=list(sorted(dicte, key=dicte.get,reverse=True))
print (liste)
if len(liste)>0:
    print("Best article ist... Art. "+str(liste[0]))
else:
    print("No entry found")'''

print(suche("toll"))