#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fname = input('file name: ')
try:
    fhandle = open(fname)
except:
    print(f'File can be opened: {fname}')
    exit()

numbers = []

for line in fhandle:
    try:
        numbers.append(float(re.findall('^New Revision: (\d+)', line)[0]))
    except: continue
print(f'Average: {sum(numbers)/len(numbers):.2f}')

