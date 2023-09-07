#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
print(np.__version__)


# In[36]:


a = [10.2,20.25,30.36,40,50,70,80,90]
print(a)
b = np.array(a)
print(b)
print(b+100)


# In[34]:


b.shape
b.dtype


# In[41]:


d = np.array([1,2,3,4,5,6,7,8,9,10], ndmin = 2)
print(d)

c = np.array(a, ndmin = 2)
print(c)


# In[44]:


d.shape
d.dtype


# In[49]:


d = np.array([1,2,3,4,5,6,7,8,9,10], dtype = complex)
print(d)

c = np.array(a, ndmin = 2, dtype = complex)
print(c)


# In[50]:


d.dtype


# In[53]:


a = [[10,20,30,40],[50,70,80,90]]
b = np.array(a)
print(b.shape)
print(b)


# In[54]:


a = np.array([[10,20,30,40],[50,70,80,90]])
a.shape


# In[57]:


a = np.array([[[10,20,30],[40,50,70]],[[80,90,60],[10,20,30]]])
print(a.shape)
print(a)


# In[59]:


a = np.array([[10,20,30],[40,50,70],[80,90,60],[10,20,30]])
print(a.shape)
print(a)


# In[64]:


a.shape = (3,4)
print(a.shape)
print(a)


# In[ ]:




