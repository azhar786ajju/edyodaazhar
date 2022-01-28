#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checkRotation(s1, s2): 
    temp = ''
  
   
    if len(s1) != len(s2):
        return False
  
   
    temp = s1 + s1
  
    
    if s2 in temp:
        return True
    else:
        return False
  

string1 = "CAMPUS"
string2 = "PUSCAM"

if checkRotation(string1, string2):
    print("Given Strings are rotations of each other.")
else:
    print("Given Strings are not rotations of each other.")

