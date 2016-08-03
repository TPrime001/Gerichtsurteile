import pickle

def suche (query):
    with open("index.pickle", "rb") as f:
        index = pickle.load(f)
