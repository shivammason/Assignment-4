#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import os



user_url = input("Enter url: ")
host_name = user_url.split("/")[2]
print(host_name)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name, 80))
cmdn='GET {} HTTP/1.0\n\n'.format(user_url).encode()
mysock.send(cmdn)

print("Please enter a valid URL")
    

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    actualdata=data.decode()
    print(data[:3000])
    
    print(len(data))

mysock.close()


# In[ ]:




