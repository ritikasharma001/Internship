#!/usr/bin/env python
# coding: utf-8

# # DAY 3 Task

# In[1]:


fruits={"apple":2, "orange":3, "banana":5}
vegetables={"brinjal":3, "carrot":4, "cauliflower":6}
fruits.update(vegetables)
print(fruits)


# In[5]:


myDict={'a':1, 'b':2, 'c':3}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)


# In[6]:


keys=['red', 'green', 'blue']
values=['#FF0000', '#008000', '#0000FF']
color_dictionary=dict(zip(keys, values))
print(color_dictionary)


# In[7]:


seta = set([5, 10, 3, 15, 2, 20])
print(len(seta))


# In[8]:


sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print(sn1)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(sn1-sn2)


# In[ ]:




