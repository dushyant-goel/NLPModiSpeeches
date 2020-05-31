# import pandas as pd
# import matplotlib.pyplot as plt

# import numpy as np
# import seaborn as sns
# import warnings
# warnings.filterwarnings('ignore')
# import re
# import pandas as pd
# from time import time
# from collections import defaultdict

# import spacy
# from gensim.models import Word2Vec
# import logging
# logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
# from sklearn.manifold import TSNE
# from numpy import dot
# from numpy.linalg import norm

# # Create the list of list formate of the custom corpus for gensim modeling
# sent = []
# file = "./english_speeches.txt"
# file_pointer = open(file,"r")
# file_text = file_pointer.read()
# sent.append(file_text.split())

# import gensim

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)
stopwords.add('wa')
import operator

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1,
	    collocations=False
    ).generate(str(data))

    sorted_d = sorted(wordcloud.words_.items(), key=operator.itemgetter(1), reverse=True)              
    plt.bar(*zip(*sorted_d[:15]))
    plt.show()


    # fig = plt.figure(1, figsize=(12, 12))
    # plt.axis('off')
    # if title: 
    #     fig.suptitle(title, fontsize=20)
    #     fig.subplots_adjust(top=2.3)

    # plt.imshow(wordcloud)
    # plt.show()

file = "./english_speeches.txt"
file_pointer = open(file,"r")
file_text = file_pointer.read()

show_wordcloud(file_text)
