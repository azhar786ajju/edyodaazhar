#!/usr/bin/env python
# coding: utf-8

# In[2]:


def find_pair(array,number):
    
    for i in range(len(array)-1):
        
        for j in range(i+1,len(array)):
        
            if array[i]+array[j]==number:
                print("Pair found",(array[i],array[j]))
                return
                      
    print("Pair not found")
                      
                      
array = [8, 7, 2, 5, 3, 1]
number = 12
                      
find_pair(array,number)

