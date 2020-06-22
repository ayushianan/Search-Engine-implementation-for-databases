from math import log, sqrt
#from snowballstemmer import FrenchStemmer as fs 
import sys
from nltk.corpus import stopwords
import re
import sys, os
projectpath = os.path.dirname(os.path.realpath('querying.py'))
#directory path
libpath = projectpath + '/lib'
#lib path
sys.path.append(libpath)
os.chdir(projectpath)
import parsing
import re
import time
collection = 'New Testament'
#mongo folder
# Indicate the path where relative to the collection
os.chdir(projectpath + '/data/' + collection)
files = [file for file in os.listdir('.') if os.path.isfile(file)]

def cleanQuery(string):
    frenchStopWords = stopwords.words('french')
    p = re.compile('\w+')
    words = p.findall(string)
    words = [word.lower() for word in words]
    #words = [fs().stemWord(word) for word in words]
    words = [word for word in words if word not in frenchStopWords]
    return words

def rankDocuments(index, words):
    # We rank each document based on query
    rankings = {}
    for word in words:
        for document in index[word]['document(s)'].keys():
            # Term Frequency (log to reduce document size scale effect)
            TF = index[word]['document(s)'][document]['frequency']
            if TF > 0:
                TF = 1 + log(TF)
            else:
                TF = 0
            # Store scores in the ranking dictionary
            if document not in rankings:
                rankings[document] = TF
            else:
                rankings[document] += TF
    # Order results according to the scores
    rankings = list(reversed(sorted(rankings.items(), key=lambda x: x[1])))
    return rankings

def rankDocuments1(index, words):
    # We rank each document based on query
    rankings = {}
    for word in words:
        for document in index[word]['document(s)'].keys():
            # Term Frequency (log to reduce document size scale effect)
            TF = index[word]['document(s)'][document]['position(s)']
            for file in files:
                        name = re.match('(^[^.]*)', file).group(0)
                        if name==document:
                                    data = open(file).read().splitlines()   
                                    words = parsing.clean1(data)     
            # Store scores in the ranking dictionary
            if document not in rankings:
                rankings[document] = words[TF[0]-10:TF[0]+10]
            else:
                rankings[document] += words[TF[0]-10:TF[0]+10]
            #print(rankings[document])
            #print(document)
            #print("11111111111111")
    # Order results according to the scores
    rankings = list(rankings.items())
    #print(rankings[0])
    return rankings

    
