from build_index import indexing
from load_dataset import load_wikidata
# import re
import pickle
from collections import defaultdict
import json

filename = "TestProjetCrawler2/logs/reddit/2016-08-03T07-41-13.json"

data_all = json.load(open(filename,"r"))

AZlist = []
textlist = []
urllist = {}
index = {}
keylist=[]

for key, var in data_all[1]:
    if key != "text":
        keylist.append(key)
        index[key]=defaultdict(list)

for data_page in data_all:
    az = data_page["AZ"][0]
    AZlist.append(az)
    textlist.append(data_page["text"][0])
    urllist[az] = data_page["url"][0]
    for i in keylist:
        index[i][data_page[i][0]].append(az)

save_in = open("index/infobox.pickle", "wb")
pickle.dump(index, save_in)
save_in.close()
indexing(textlist, AZlist)
