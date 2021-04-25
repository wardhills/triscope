#!/usr/bin/env python
# coding: utf-8

# In[1]:


focal_lenght = 600  # mm
mirror_diameter = 115  # mm


# In[2]:


import math
from matplotlib import pyplot as plt
import numpy as np


# In[3]:


# determine a, where a is the apes angle

a = math.atan((mirror_diameter/2)/focal_lenght) # rad

a   # 1/2 of the apes angle 


# In[4]:


#determine the 1/2 width of the 'focus cone' at a given hight

math.tan(a) * (focal_lenght-100) # mm


# In[7]:


x = np.arange(0,focal_lenght)
y = math.tan(a) * (focal_lenght-x)

fig=plt.figure()

ax= fig.add_axes([1,1,1,1])

ax.plot(x,y)
ax.set_xlabel('Distance from Mirror')
ax.set_ylabel('width of cone')




# In[ ]:




