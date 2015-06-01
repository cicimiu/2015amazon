# -*- coding: utf-8 -*-
"""
 
@author: cici
"""
import math
import json
dic_="revtonum_400000"          
rate_= "rate_400000"
review_size =400000


with open (rate_,'r') as infile:
    rate = json.load(infile)

with open (dic_,'r') as infile:
    dic = json.load(infile)

print len(dic)
norm=[]

delete = []
def combine (times, svm_input,svm_input2 ) :
     rate1 = rate[times*review_size: (times+1)* review_size]
     dic1= dic[times*review_size: (times+1)* review_size]
     f= open (svm_input,'w')
     f1=open(svm_input2,'w')
     for i in range (0,review_size ) :
         if dic1[i] ==[]:
             delete.append(i)
         elif dic1[i] !=[]:
             normi =1/ math.sqrt ( len( dic1[i] ) )     # nornalize
             norm.append(normi)
             
             if i< review_size/2:
                 wr =f
             else:
                 wr=f1
             wr.write(str(rate1[i]) +' ')
             for s in dic1[i] :
                 wr.write(str(s+1) +':'+ str(normi) +' ')
             wr.write('\n')
         if i%1000 ==0:
             print i/1000
         



combine(0,"svm_input-test","svm_input-train")
