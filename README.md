# AI-ChatBot


## Chatbot

A chatbot is an AI-based software designed to interact with humans in their natural languages. These chatbots are usually converse via auditory or textual methods, and they can effortlessly mimic human languages to communicate with human beings in a human-like manner. A chatbot is arguably one of the best applications of natural language processing.

## 1. Retrieval-based Chatbots
A retrieval-based chatbot is one that functions on predefined input patterns and set responses. Once the question/pattern is entered, the chatbot uses a heuristic approach to deliver the appropriate response. The retrieval-based model is extensively used to design goal-oriented chatbots with customized features like the flow and tone of the bot to enhance the customer experience.

## 2. Generative Chatbots
Unlike retrieval-based chatbots, generative chatbots are not based on predefined responses – they leverage seq2seq neural networks. This is based on the concept of machine translation where the source code is translated from one language to another language. In seq2seq approach, the input is transformed into an output.


## Intents

create a JSON file named “intents.json” including these data as follows.

```
{"intents":[
        {"tag": "greeting",
         "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
         "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"]
        },
        {"tag": "goodbye",
         "patterns": ["Bye", "See you later", "Goodbye"],
         "responses": ["See you later thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
        },
        {"tag": "thanks",
         "patterns":["Thanks", "Thank you", "That's helpful"],
         "responses":["Happy to help!", "Any time!", "My pleasure" ,"You are welcome"]
        },
		{"tag":"police",
		"patterns":["Emergency" , "Police" , " I am in danger"],
        "responses":["call the police on 122"]
		},
		{"tag":"conversation",
		"patterns":["how are you ?", "sup","how it is going ?"],
		"responses":["good hope you are as well"]
		},
        {"tag": "weather",
        "patterns": ["How is the weather ?","tell me the weather forecast now","what's the forecast?","what is the weather like right now?","what's the temperature going to be tomorrow?","Is it raining?" ], 
         "responses": ["weather"]
        },   
        {"tag": "Hotel",
         "patterns": ["What is the  Hotel next to me ?", "I want to find a hotel", "I need to sleep  " , "What are the hotel  in location"],
         "responses": ["Hotel"]
        },
		{"tag":"info",
		"patterns":["tell me about topic","what do you know about topic"],
		"responses" :["info"]
		},
		{"tag":"currency",
		"patterns":["change 50  dollars to pounds","Convert 50 Euro to pound","Convert 50 dollar to pound"],
		"responses":["Currency"]
		},
		{"tag":"Restaurant",
		"patterns":["What is the  restaurant next to me ?", "I want to find a restaurant", "I need to eat ","What are the restaurant  in location"],
		"responses":["Restaurant"]
		},
		{"tag":"Clinic",
		"patterns":["What is the  Clinic next to me ?", "I want to find a Clinic", "I need a medicine " , "What are the restaurant  in location"],
		"responses":["Clinic"]
		}
   ]
   
}
```

The variable “training_sentences” holds all the training data (which are the sample messages in each intent category) and the “training_labels” variable holds all the target labels correspond to each training data.
Then we use “output()” function provided by scikit-learn to convert the target labels into a model understandable form.

## Tokenizer

we vectorize our text data corpus by using the “Tokenizer” class and it allows us to limit our vocabulary size up to some defined number. When we use this class for the text pre-processing task, by default all punctuations will be removed, turning the texts into space-separated sequences of words, and these sequences are then split into lists of tokens. They will then be indexed or vectorized. We can also add “oov_token” which is a value for “out of token” to deal with out of vocabulary words(tokens) at inference time.


## Model Training

our Neural Network architecture for the proposed model and for that we use the “Sequential” model class of Keras to classify between the input data .

## Entity Recognation 

Named-entity recognition (NER) (also known as (named) entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

Building our custom entity using spacy relatred to tourism and Egypt  called  (Visit_egypt ) which can recognize all quantity , numbers , name of anctient egyptian kings ,all places in egypt and Currencies like euro and dollar  ..  etc , send N.Class with the Entity to backend so we can pick the right answer  from our database

## Chat function

funtion which  work on load model and classify the input data  , return  random response from our database with  an entity  if there is any entity in our input like name , location , money and quantity  .. etc    in json file format .



