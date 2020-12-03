#!/usr/bin/env python
# coding: utf-8

# # DAY 11 TASK

# In[1]:


# Task 1
nums1 = [34, 32, 55, 234, 546]
nums2 = [45, 675, 32]
zipped_list = list(zip(nums1, nums2))  
print(zipped_list)


# In[2]:


# Task 2
nums = [x for x in range(1, 8)]
nums1 = [34, 32, 55, 234, 546, 45, 675, 32]
zipped_list = list(zip(nums, nums1))
print(zipped_list)


# In[3]:


# Task 3
print(sorted(nums1))


# In[4]:


# Task 4
odd_nums = list(filter(lambda x:x%2!=0, nums1))
print(odd_nums)


# In[ ]:




