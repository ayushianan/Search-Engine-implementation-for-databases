import sys, os
import itertools
projectpath = os.path.dirname(os.path.realpath('main.py'))
libpath = projectpath + '/lib'
sys.path.append(libpath)
os.chdir(projectpath)
from PyQt4 import QtCore, QtGui
from browser import Ui_MainWindow
from querying import cleanQuery, rankDocuments,rankDocuments1
from pymongo import MongoClient

import parsing
import re
import time
collection = 'New Testament'
#mongo folder
# Indicate the path where relative to the collection
os.chdir(projectpath + '/data/' + collection)
files = [file for file in os.listdir('.') if os.path.isfile(file)]

# Connect to the database containing inverted indexes
client = MongoClient()
db = client.Inverted_Index
# Choose a folder containing documents
folder = 'New Testament'
collection = db[folder]


class browser(QtGui.QMainWindow):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
        # Connect the query function with the search button
		self.ui.pushButton.clicked.connect(self.query)
	def query(self):
        # Empty the list
		self.ui.listWidget.clear()
        # Get the words in the query
		words = cleanQuery(self.ui.lineEdit.text())
        # Collect the information for each word of the query
		index = {}
		for word in words:
			index[word] = collection.find({'_id' : word})[0]['info']
        # Rank the documents according to the query
		results = rankDocuments(index, words)
		results1 = rankDocuments1(index, words)
		size=len(results)
		print(size)
		#print(results1[0])
        #results1 = rankDocuments1(index, words)
		i=0
		rankings = {}
		for result in results:
			if(i<10):
				self.ui.listWidget.addItem(result[0]+' : '+str(round(result[1], 2)))
				j=0
				for j in range(size):
					if(result[0]==results1[j][0]):
						break
				self.ui.listWidget.addItem(str(" ".join(results1[j][1])))
				'''for word in words:
					for document in index[word]['document(s)'].keys():
    						# Term Frequency (log to reduce document size scale effect)
						TF = index[word]['document(s)'][document]['position(s)']
						for file in files:
							name = re.match('(^[^.]*)', file).group(0)
							if name==document:
								data = open(file).read().splitlines()   
								words = parsing.clean(data)     
            				# Store scores in the ranking dictionary
						if document not in rankings:
							rankings[document] = words[TF[0]-10:TF[0]+10]
						else:
							rankings[document] += words[TF[0]-10:TF[0]+10]
						#self.ui.listWidget.addItem(rankings[document])
						print(rankings[document])'''
			i=i+1

            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = browser()
    myapp.show()
    sys.exit(app.exec_())
