#Removing Punctuations
import pandas as pd
import string

exclude = string.punctuation.replace("'", "", 1)

def remove_punc(text):
    for char in exclude:
        text = str(text).replace(char," ")
    return text

chat_words = pd.read_excel("Chat Words Short.xls")
chat_words['symbol']=chat_words['symbol'].str.lower().str.rstrip(" ")
chat_words['meaning'] = chat_words['meaning'].str.lower().str.rstrip(" ")

def chat_conversion(text):
    new_text = []
    #set_words = set()
    for w in text.lower().split():
        #print(w)
        if w in chat_words['symbol'].tolist():
            #print(w)
            #set_words.add(w)
            new_text.append(chat_words[chat_words['symbol']==w]['meaning'].values[0])
        else:
            new_text.append(w)
    #print(new_text)
    #print(set_words)
    return " ".join(new_text)

#Spelling Correction:
from textblob import TextBlob

def spelling_correct(text):
    #print('------------------')
    #print(text)
    #print("\n")
    return str(TextBlob(text).correct())

#Removing stopwords
from nltk.corpus import stopwords
stopwords.words("English")

stop_words= stopwords.words("English")
stop_words.remove('not')

def remove_stopwords(text):
    new_text = []
    
    for word in text.split():
        if word in stop_words:
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    #print(x)
    new_text.clear()
    return " ".join(x)

#Handling Emojis
import re
def remove_emoji(text):
    emoji_pattern = re.compile("["
                              u"\U0001F600-\U0001F64F"
                              u"\U0001F300-\U0001F5FF"
                              u"\U0001F680-\U0001F6FF"
                              u"\U0001F1E0-\U0001F1FF"
                              u"\U00002702-\U000027B0"
                              u"\U000024C2-\U0001F251"
                              "]+", flags = re.UNICODE)
    return emoji_pattern.sub(r'',text)

#Tokenization
from nltk.tokenize import word_tokenize, sent_tokenize

def preprocess(val):
    val = str(val)
    print(val)
    #Lowercasing
    val = val.lower()
    print("Step 1")
    
    #Removing punctuations
    val = remove_punc(val)
    print("Step 2")
    
    #Removing Chat words
    val = chat_conversion(val)
    print("Step 3")
    
    #Spelling correction
    val = spelling_correct(val)
    val = val.replace('prima', 'prema')
    print("Step 4")
    
    #Remove stop words
    val = remove_stopwords(val)
    print("Step 5")
    
    #Remove emojis
    val = remove_emoji(val)
    print("Step 6")
    
    #Tokenize
    val = word_tokenize(val)
    print("Step 7")
    
    #Join
    val = " ".join(val)
    print(val)
    
    #Transform
    #val = cv3.transform(val).toarray()
    
    return val