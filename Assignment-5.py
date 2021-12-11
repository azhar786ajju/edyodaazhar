#!/usr/bin/env python
# coding: utf-8

# In[5]:




class sol:
    def power(self,x,n):
        if x==0 or x==1 or n==1:
            return x
        
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        
        if n==0:
            return 1
        if n<0:
            return 1/self.power(x,-n)
        
        val = self.power(x,n//2)
        if n%2 == 0:
            return val*val
        else:
            return val*val*x
        
print(sol().power(10,2)) 

