import nltk
import numpy as np
import tensorflow as tf
import random
import keras
from nltk.stem.lancaster import LancasterStemmer
import json
import spacy


model_intity = keras.models.load_model('model.h5')
model_entity = spacy.load('visit_egypt')
words =  ["'s", '50', 'a', 'about', 'am', 'anyon', 'ar', 'artifact', 'be', 'bye', 'chang', 'clin', 'convert', 'dang', 'day', 'do', 'doll', 'eat', 'emerg', 'euro', 'find', 'forecast', 'going', 'good', 'goodby', 'hello', 'help', 'hi', 'hotel', 'how', 'i', 'in', 'insight', 'is', 'it', 'know', 'lat', 'lik', 'loc', 'me', 'medicin', 'nee', 'next', 'now', 'of', 'pol', 'pound', 'rain', 'resta', 'right', 'see', 'sleep', 'sup', 'tel', 'temp', 'thank', 'that', 'the', 'ther', 'to', 'tomorrow', 'top', 'want', 'weath', 'what', 'you']
labels =  {0:'Clinic',1: 'Hotel',2: 'Restaurant',3: 'conversation',4: 'currency',5: 'goodbye',6: 'greeting',7: 'info',8:'police',9:'thanks',10:'weather'}
nltk.download('punkt')
stemmer =  LancasterStemmer()

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
     sentence = []
     for ent in model_entity(word).ents:
        sentence.append({"Name": ent.text , "Label": ent.label_})
     return sentence


def chat():
        wordbag =  bag_of_words(inp, words)
        recognation =  net(inp) 
        class_intent = model_intity.predict(np.array([wordbag]))
        class_index = np.argmax(class_intent)
        tag = labels[class_index]
        return {"tag":tag , "recognation":recognation}
