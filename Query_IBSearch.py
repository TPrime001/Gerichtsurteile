import re
import pickle

regex_list = {'gericht': '" ?G ?= ?([0-9A-Za-z \/\.-]+) ?"', 'datum': '" ?D ?= ?([0-9A-Za-z \/\.-]+) ?"',
              'AZ': '" ?AZ ?= ?(\(.*\))? ?([0-9A-Za-z \/\.-]+) ?(\(.*\))? ?"', 'typ': '" ?T ?= ?([0-9A-Za-z \/\.-]+) ?"',
              'rechtsgebiete': '" ?R ?= ?([0-9A-Za-z \/\.-]+) ?"'}

shortcuts = {}

f = open("index\\infobox.pickle", "rb")
index = pickle.load(f)
f.close()


def info():
    f = open("README_IBSearch.txt", "r", encoding="UTF-8")
    print(f.read())
    f.close()


def filtershortcuts(query):
    for key2 in regex_list:
        i=regex_list[key2]
        re_code = re.compile(i)
        tempvar = re.finditer(re_code, query)
        shortcuts[key2] = []
        for j in tempvar:
            shortcuts[key2].append(j.group(1))
#    print(shortcuts)


def filteroutput(output):
    realout = {}
    for az in output:
        isin = True
        for key in shortcuts:
            for i in shortcuts[key]:
                isin2 = False
                for az2 in index[key][i]:
                    if az2==az:
                        isin2= True
                if isin2 == False:
                    isin = False
        if isin == True:
            realout[az]=output[az]
    return realout


info()
