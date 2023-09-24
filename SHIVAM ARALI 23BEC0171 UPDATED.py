#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=float(input("ENTER DURATION IN DAYS"))
b=a
c=a*12
d=a*12*60
e=a*12*60*60
print("THE DURATION IN DAYS IS",b)
print("THE DURATION IN HOURS IS",c)
print("THE DURATION IN MINUTES IS",d)
print("THE DURATION IN SECONDS IS",e)


# In[2]:


n=float(input("ENTER NUMBER OF LOAVES OF BREADS"))
b=3.49
total=n*b
dis=(60/100)*total
print("THE TOTAL AMOUNT IS",total,"AND THE DISCOUNTED PRICE IS",dis)


# In[16]:


import math
a=float(input("ENTER NUM 1"))
b=float(input("ENTER NUM 2"))
c=float(input("ENTER NUM 3"))
m=min(float(a,b,c))
n=max(float(a,b,c))
middle=(a+b+c)-m-n
print(m,middle,n)
                     


# In[ ]:




