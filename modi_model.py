import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import re
import pandas as pd
from time import time
from collections import defaultdict

import spacy
from gensim.models import Word2Vec
import logging
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
from sklearn.manifold import TSNE
from numpy import dot
from numpy.linalg import norm

# Create the list of list formate of the custom corpus for gensim modeling
sent = []
file = "./english_speeches.txt"
file_pointer = open(file,"r")
file_text = file_pointer.read()
sent.append(file_text.split())

# Train the gensim word2vec model with our own custom corpus
model = Word2Vec(sent, min_count=1, size=50, workers=3, window=3, sg=1)


print
print
print

print "TO STOP TYPE 'quit'"
print "OUTPUT FORMAT:"
print "WORD : CONTEXT SIMLARITY"
print
print


word = raw_input("Enter a word to find context: ")

while(word != "quit"):
	
		
	try:
		s = model.most_similar(word)
		for tup in s[:5]:
			print tup[0], ":", tup[1]
		print
	except:
		print word, " not found"

	word = raw_input("Enter a word to find context: ")