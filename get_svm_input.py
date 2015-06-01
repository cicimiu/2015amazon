# -*- coding: utf-8 -*-
"""
 get liblinear type svm input
 
 
@author: CICI
"""

times=0
review_size = 40000
vacabulary_size = 2000
import json
input_ ="counter.txt"
input_2 = "r0.txt"
output_ = "2000dict"
output_2 = "revtonum"
svm_input = "svm_input3"


with open(input_,'r') as infile:
    freqofwords = json.load(infile)
    
f1 = freqofwords[-vacabulary_size:]


with open(output_ ,'w') as outfile:
    json.dump(f1,outfile)

cnt=0
for l in f1:
   l[1]=cnt
   cnt +=1

''' 
f1 is like   [word, index]...  [great,1] , [hate, 2] 
'''
with open(output_,'w') as outfile:
    json.dump(f1,outfile)
    
with open(input_2,'r') as infile:
    reviews =json.load(infile)

reviews =reviews[times*review_size: (times+1)* review_size]


''' dic is numerical type of text    eg. [[1,2,66] , [44,186] ... ]'''

dic=[]
cnt=0

for review in reviews:
    review =review.split()
    temp =[]
    for word in review:
        for l in f1:
            if l[0]== word:
                temp.append( l[1] ) 
    l=len(temp)
    cnt +=1
    temp= list (set(temp ) )
    temp1 = sorted(temp )
    dic.append(temp1)

    
with open(output_2,'w') as outfile:
    json.dump(dic,outfile)

    
  
     
            
    



