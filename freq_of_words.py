# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:05:19 2015

@author: maoxi
"""
import json
import operator
from collections import Counter
import re
# dictionary  count
review_inwordfile="reviews_b.txt"
counter_file = "counter.txt"

with open(review_inwordfile,'r') as infile:
    review_inword = json.load(infile)

#review_inword = review_inword[:2000]
cur =0
cnt = Counter()
for review in review_inword:
    words = re.findall(r"[\w]+", review)
    cur+=1
    if cur % 1000 == 0:
        print "reviews count to 1000*"
        print cur/1000
    cnt_temp =Counter(words)
    cnt += cnt_temp
 
sorted_dic = sorted(cnt.items(), key = operator.itemgetter(1))

with open(counter_file , 'w') as outfile:
    json.dump(sorted_dic , outfile)
print (" count finish")
   
    
        


