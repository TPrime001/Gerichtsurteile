from index_text import indexing
from load_dataset import load_wikidata
import re
import pickle
from collections import defaultdict

filename = "" #TODO fill filename and data below
tag_text = ""
tag_title = ""
tag_sections = ""
tag_divs = ""
tag_id = ""

data_all = load_wikidata(filename)

for data_page in data_all:
    #TODO link preprocessing

    for section in data_page[tag_sections]:
        if section[tag_id] == "text":
            indexing(section, AZ)