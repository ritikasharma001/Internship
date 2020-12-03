#!/usr/bin/env python
# coding: utf-8

# # DAY 9 TASK

# In[1]:


# Task 1
a = lambda x, y : x * y
print(a(2, 10))


# In[2]:


#Task 2
from functools import reduce
fibonacci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
 
print("Fibonacci series upto 10:", fibonacci(9))


# In[3]:


# Task 3
nums = [2, 4, 6, 9 , 11]
x = 2
print("The original list is", nums)
nums_updated = list(map(lambda y:y*x, nums))
print("The list after multiplying by 2 is", nums_updated)


# In[4]:


#Task 4
nums = [2, 18, 4, 36]
print("The numbers divisible by 9 are:", end=" ")
for i in nums: 
    if i % 9 == 0: 
        print(i, end=" ")


# In[5]:


#Task 5
nums = [3, 19, 4, 36]
print("The even numbers in the list are:", end=" ")
for i in nums:
    if i % 2 == 0: 
        print(i, end=" ")


# In[ ]:




