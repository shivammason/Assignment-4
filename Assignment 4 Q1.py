#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re 

regexp = input('Please enter regular expression : ')
file = "mbox-short.txt"
hand = open(file)
count = 0

for line in hand:
    if re.search(regexp, line):
        count += 1
    else:
        continue
        
print(f'{file} had {count} lines matching {regexp}')


# In[ ]:




