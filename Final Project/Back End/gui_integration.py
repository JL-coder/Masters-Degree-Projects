# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 23:05:39 2021

@author: joshua levy, sreejani chatterjee, xueying zeng
"""

# libraries needed to be used. Please go through the read me for installation advices.

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
import pickle
import numpy as np
import chatbot
import re
regex = re.compile('[^a-zA-Z]')
from keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity
model = load_model('chatbot_model.h5')
import json
import random
import emoji
from googlesearch import search
from itertools import chain

# loading the intents files to be used for semantic analysis
intents = json.loads(open('fresh_intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

# global variable to pass zipcode in give_url function
user_zipcode = None
# global variable to use list of links in give_url function
search_result_list = []
# global variable to return links in give_url function
result = ""

# global variable for sentiment score to be used to look up url in give_url function
get_resp_sentiment = None
sem_resp_sentiment = None

# importing the patterns and ignore words from the chatbot.py
documents = chatbot.documents
ignore_words = chatbot.ignore_words

ignore_words = [lemmatizer.lemmatize(word.lower()) for word in ignore_words]
ignore_char = ['?', '!', '.', ':', ',']

docs = [documents[j][0] for j in range(len(documents))]
for i in ignore_char:
    for s in docs:
        if i in s:
            s.remove(i)

# Creating a list of patterns to be used later to get the response either based on the intents file or the semantic search
doc_lst = []
for i in range(len(docs)):
    doc_lst.append(" ".join(docs[i]))
doc_lst = [lemmatizer.lemmatize(word.lower()) for word in doc_lst]

#Tokenizes and lemmatizes the sentences
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
#Tokenizes pattern and returns an array of the bag of words
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

#Function filters out bot responses below a 25% threshold. Returns most likely
def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Loading the glove vector from the system
def load_glove_model(File):
    glove_model = {}
    with open(File, 'r', encoding="utf8") as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            embedding = np.array(split_line[1:], dtype=np.float64)
            glove_model[word] = embedding
    return glove_model

# the pretrained model used
glove_vectors = load_glove_model("glove.6B.50d.txt")

# creating the word vectors from the input
def get_sentence_vector(sentence):
    sent_array = []
    for word in sentence.split():
        temp = word.strip()
        temp = regex.sub('', temp)
        temp = temp.lower()
        sent_array.append(glove_vectors[temp])
    return(np.mean(sent_array, axis=0))

# Semantic analysis
def semantic_search(user_input, intents_json):
        try:
            sim_score = []
            for i in range(len(documents)):
                
                # extract the vector for user input
                doc1 = user_input
                doc1_vector = get_sentence_vector(doc1)
                
                # extract the vector for all the intents pattern
                doc2 = [doc for doc in documents[i][0] if doc not in ignore_words]
                doc2 = " ".join(doc2)
                doc2_vector = get_sentence_vector(doc2) 
                
                # compute the cosine similarity between the input and every the intents pattern
                sim_lst = cosine_similarity([doc1_vector, doc2_vector])
                
                #list of similarity score 
                sim_score.append(sim_lst[1][0])
                
            # extract the tag with the highest similarity
            tag = documents[sim_score.index(max(sim_score))][1]            
            
            # response from resulting tag will be returned
            list_of_intents = intents_json['intents']
            for i in list_of_intents:
                if(i['tag']== tag):
                    result = random.choice(i['responses'])
                    break
            return result, tag
        
        # if gibbersish or emoji is entered
        except KeyError:
            return "I am sorry can you type that again? If you are trying to use emojis we are yet to add that feature.", None
    
# Assess the severity of mental illness and provides response accordingly
def sentiment_analysis(user_input):
    scores = sid.polarity_scores(user_input)
    # only returnning the negative score for analysis
    return scores['neg']

#Based off intents file tags generates a response
def getResponse(ints, intents_json):
    tag = ints[0]['intent']    
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result, tag

#When the user enters a zip code this function is run. It will double check that the zip code is apart of the state of MA. Need to store zip code moving foreword if it is valid.
def zipsearch(user_input_zipcode):
    global user_zipcode
    #Open up a file containing all the zip codes in Massachusets and copy to a 1D list
    filename = "zipcodes.csv"
    #Open up a file containing all the zip codes in Massachusets and copy to a 1D list
    with open(filename, 'r') as csvfile:
        zip_codes = [row.strip().split(",") for row in csvfile]
        flatten_list = list(chain.from_iterable(zip_codes))
    
    # stripping the new line that is being added to the message when entering user input
    user_input_zipcode.strip('\n')
    user_input_zipcode = list(user_input_zipcode.split(" "))
    
    # this block is run when the correct MA zipcode is entered
    if user_input_zipcode[-1] in flatten_list:
        user_zipcode = user_input_zipcode[-1]
        return "Thank you for answering."
    
    # this block is run when an invalid or a non MA zipcode is entered
    else:
        return "Please enter a valid MA zip code."

#Handles the bots responses based off the input and intents file and semantic search
def chatbot_response(msg):
    global get_resp_sentiment, sem_resp_sentiment
    msg_len = len(msg)
    msg = msg[:msg_len - 2]
    for i in ignore_char:
        msg = msg.replace(i,"").lower()
    
    # this block is called when the input is from training data
    # In this block the sentiment analysis output is also returned to be used in 
    # returning url in give_url function
    if msg in doc_lst:
        ints = predict_class(msg, model)
        get_resp = getResponse(ints, intents)
        if get_resp[1] in ('Depression', 'psychosis', 'Anxiety'):
            get_resp_sentiment = sentiment_analysis(msg)
        return get_resp[0], get_resp_sentiment
    
    # this block is called when a zipcode is entered
    elif msg.startswith("my zipcode is "):
        zip_resp = zipsearch(msg)
        return zip_resp, None
    
    # this block is called when user decline's to answer a question
    elif msg.startswith("i decline"):
        decline_resp = "Understood! May I know where you live? You can give me your zip code just say \"My zip code is\" "
        return decline_resp, None
    
    # this block is called when user input is their age 
    elif msg.endswith(" years old"):
        age_response = "Thank you for answering. May I know where you live? You can give me your zip code just say \"My zip code is\" "
        return age_response, None
    
    # this clock is called when the user input is not in the training data and semantic seatrch is called.
    # In this block the sentiment analysis output is also returned to be used in returning url in give_url function
    else:
        sem_resp = semantic_search(msg, intents)
        if sem_resp[1] in ('Depression', 'psychosis', 'Anxiety'):
            sem_resp_sentiment = sentiment_analysis(msg)
        return sem_resp[0], sem_resp_sentiment
                    
def give_url(message):
    global search_result_list, result    
    sentiment_analysis_test = chatbot_response(message)[1]
    
    # this block is called when the sentiment analysis decides 
    # the user is in dire need of psychitric consultation
    if sentiment_analysis_test > 0.2:
        try:
            #Google Search query results as a Python List of URLs
            query = 'psychiatrists near ' + str(user_zipcode)
            # the bot return the psycholoyg today site which has 
            # the list of psychiatrists in the user zipcode
            for i in list(search(query)):
                if i.startswith('https://www.psychologytoday.com'):
                    url = i
            # a generic return statement with the output url
            return "Here are a list of psychiatrists in your area:" + url
        # the exception is for internet issue or user system issue
        except SystemError:
            return str("Something went wrong with your video search. Please check your internet connection and try again.")
    
    # this block is called when the sentiment analysis decides 
    # the user is having issues but watching some meditation videos is going to help
    elif 0.05 <= sentiment_analysis_test <= 0.2:
        try:
            #Google Search query results as a Python List of URLs
            query = 'meditation youtube videos'
            # we are showing the first 5 results in the list not to overwhelm the user
            for i in search(query):
                if i.startswith("https://www.youtube.com"):
                    search_result_list.append(i)
                    search_result = search_result_list[:5]
            for j in search_result[:5]:
                result += j
                result += "\n" 
            # a generic return statement with the list of output url                
            return str("Here are some calming Youtube videos for you:" + result)
        
        # the exception is for internet issue or user system issue
        except SystemError:
            return str("Something went wrong with your video search. Please check your internet connection and try again.")
    
    # the user is ok
    else:
        return "You are fine take a walk and clear your head"

