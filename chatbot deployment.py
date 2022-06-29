import nltk
import numpy as np
import tensorflow as tf
import random
import keras
import spacy 
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from nltk.stem.lancaster import LancasterStemmer
import json
from tensorflow.keras.models  import load_model

nltk.download('punkt')
stemmer =  LancasterStemmer()
model_intity = keras.models.load_model('model.h5')
labels =  {0:'Clinic',1: 'Hotel',2: 'Restaurant',3: 'conversation',4: 'currency',5: 'goodbye',6: 'greeting',7: 'info',8:'police',9:'thanks',10:'weather'}


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return np.array(bag)

def net(word) :
     sentnece = [{"response": "" , "reco": ""}]
     for ent in model_entity(word).ents:
        sentnece[0]["reco"]=ent.text
     return sentnece

def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inputt =  input()
        if inputt.lower() == "quit":
            break
        bag =  bag_of_words(inputt, words)
        print(bag.shape)
        sentnece =  net(inputt) 
        results = model_intity.predict(np.array([bag]))
        print(results)
        results_index = np.argmax(results)
        tag = labels[results_index] 
        if  results_index == 3 :
             curr = sentnece[0]["reco"]
             curr =  curr.split(' ')[0]
             sentnece[0]['response'] =  int(curr) *16
             sentnece[0]["reco"] =  'Money '
             return sentnece
        else:
           sentnece[0]['response'] = random.choice(reponses[results_index])
           return sentnece
