#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
import urllib.parse
import urllib.error


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

characters = 0
for line in fhand:
 
    words = line.decode()
    characters = characters + len(words)
    if characters < 3000:
        print(line.decode().strip())
print(characters)

