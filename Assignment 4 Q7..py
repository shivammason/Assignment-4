#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
import urllib.parse
import urllib.error

import ssl

from bs4 import BeautifulSoup
count = 0                              
text = ssl.create_default_context()
text.check_hostname = False
text.verify_mode = ssl.CERT_NONE
url = input('Enter the url ')
html = urllib.request.urlopen(url, context=text).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('p')

for tag in tags:

    count += 1                        

print(count)


# In[ ]:




