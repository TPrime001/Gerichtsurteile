import re

regex_list={'gericht':'" ?G ?= ?([0-9A-Za-z \/\.-]+) ?"','datum':'" ?D ?= ?([0-9A-Za-z \/\.-]+) ?"',
            'AZ':'" ?AZ ?= ?([0-9A-Za-z \/\.-]+) ?"','typ':'" ?T ?= ?([0-9A-Za-z \/\.-]+) ?"',
            'rechtsgebiete':'" ?R ?= ?([0-9A-Za-z \/\.-]+) ?"'}

shortcuts={}

def info():
    f=open("README_IBSearch.txt","r",encoding="UTF-8")
    print(f.read())
    f.close()

def filtershortcuts(query):
    for key, i in regex_list:
        re_code = re.compile(i)
        tempvar=re.finditer(re_code,query)
        shortcuts[key]=[]
        for j in tempvar:
            shortcuts[key].append(j.group(1))

def filteroutput(output):
    realout = []
    for az in output:
        isin = True
        for key, i in shortcuts:
            if index[key][i] != az:
                isin = False
        realout.append(az)
    return realout

info()