import pandas as pd
import re

#method to remove , in data
def remove(text):
    urls = re.finditer(',', text)
    for i in urls:
        text = re.sub(i.group().strip(),'', text)
    return text

newds = pd.read_csv('cleaned.csv')
newds['genres'].apply(remove)
#converting the dataa to feature vectors
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(stop_words='english')
vect = tf.fit_transform(newds['genres'] + ' ' + newds['title'])

#getting the similiratiry between two vectors
from sklearn.metrics.pairwise import cosine_similarity
similiraty = cosine_similarity(vect)

#method to fecth similar movies
def getSimilarMovie(movie):
    index = int(newds[newds['title'] == movie].index.values[0])
    test = similiraty[index]
    similarMovies = sorted(enumerate(test), reverse=True, key= lambda x: x[1])[:20]
    for i in similarMovies:
        print(newds.iloc[i[0], 1])
