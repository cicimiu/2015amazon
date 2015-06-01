# REMOVE STOP WORDS , convert to simple tense
#next vectorize

# to prevent memory overload ,put the output into several files
import json
import re
from nltk.corpus import stopwords
stop_words = stopwords.words("english")

from nltk.corpus import wordnet as wn
def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']

def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']
    
def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
        
    return None
    
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


reviewfile = "review.txt"
review_inwordfile="reviewword.txt"
r1="reviewword1.txt"
r2="reviewword2.txt"
with open(reviewfile,'r') as infile:
    reviews = json.load(infile)
temp=[]
cn = 0 
reviews_inword = []
for review in reviews:
    cn+=1
    if cn == 585852/2:
	break
    if cn%1000 ==0:
       print cn/1000
       temp.append(cn) 
    words = re.findall(r"[\w]+", review.lower())
    types = nltk.pos_tag(words)
    cnt=0
    temp=[]
    for word in words:
        n =penn_to_wn(types[cnt][1] )
        if word in stop_words or n== None:
           cnt +=1
        else:           
            cnt +=1
            word = lemmatizer.lemmatize(word,n)
            temp.append(word)
    words = ' '.join(temp)
    reviews_inword.append(words)
    if (cn/100000.000 ==1):
        with open(review_inwordfile , 'w') as outfile:
            json.dump(reviews_inword,outfile)
        reviews_inword =[]
    elif(cn/200000.000==1):
        with open(r1 , 'w') as outfile:
            json.dump(reviews_inword,outfile)
        reviews_inword =[]    
temp.append("finish loop")    
with open(r2 , 'w') as outfile:
    json.dump(temp,outfile)
    
print ( "prepare raw data(x) done.")

