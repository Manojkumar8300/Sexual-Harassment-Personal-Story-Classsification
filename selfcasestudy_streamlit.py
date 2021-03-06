# -*- coding: utf-8 -*-
"""SelfCaseStudy_Streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UbILHJkkCjOQEa47ARjNeEhmHVuzY6_Y
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing Librarires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

import seaborn as sns
import nltk
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from skmultilearn.problem_transform import LabelPowerset
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

import pickle
from tqdm import tqdm
import os
# %matplotlib inline

preprocessed_data_train=pd.read_csv("preprocessed_data_train.csv")#loading preprocessed data into panda Dataframe
preprocessed_data_train=preprocessed_data_train.dropna()#removing the nan values
y_train=preprocessed_data_train[['commenting','ogling','groping']]

# https://gist.github.com/sebleier/554280
# we are removing the words from the stop words list: 'no', 'nor', 'not'
stopwords= ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"]

lemmatizer=WordNetLemmatizer()
def preprocessing(text_data):
    text = re.sub('[^A-Za-z0-9]+', ' ', text_data)#replacing characters other than alphabets and numbers with space
    text = ' '.join([word.lower() for word in text.split()])#lowering all the words
    text = [word for word in text.split() if word not in stopwords]#removing the stopwords
    text = ' '.join([lemmatizer.lemmatize(word) for word in text])#lemmatizing the words
    return text

vectorizer=TfidfVectorizer(ngram_range=(1,5),max_features=5000)
vectorizer.fit(preprocessed_data_train['cleaned_text'].values)#fitting training points
X_train=vectorizer.transform(preprocessed_data_train['cleaned_text'].values)#transforming training points

classifier = LabelPowerset(LogisticRegression())
classifier.fit(X_train, y_train)


import streamlit as st
from PIL import Image

st.title("SEXUAL HARRASMENT PERSONAL STORIES CLASSIFICATION")
image=Image.open("FINAL.jpg")
st.image(image)
st.sidebar.subheader("InputText")
text = st.sidebar.text_area("Enter the Personal Story in the text box given below:",height=300)
button_was_clicked = st.sidebar.button("SUBMIT")

def function3(X):
    preprocessed_text=preprocessing(X)
    
    vect=vectorizer.transform([preprocessed_text])
    
    predictions=classifier.predict(vect)
    predictions=predictions.toarray()
    return predictions
predictions=function3(text)

pred=[]
if predictions[0][0]==1:
    pred.append('Commenting')
if predictions[0][1]==1:
    pred.append('Ogling')
if predictions[0][2]==1:
    pred.append('Groping')
if sum(predictions[0])==0:
    predicted_output="The Personal story doesnot belong to any of the Class."
predicted_output="The Personal story is Categorized as:"+ ",".join(pred)

if button_was_clicked:
    st.subheader("Prediction:")
    if predictions[0][0]==1:
        st.success("Commenting")
    else:
        st.warning("Commenting")
    if predictions[0][1]==1:
        st.success("Ogling")
    else:
        st.warning("Ogling")
    if predictions[0][2]==1:
        st.success("Groping")
    else:
        st.warning("Groping")
    st.write(predicted_output)

