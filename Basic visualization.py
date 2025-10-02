#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

#  Matplotlib	is	a	Python	2D	plotting	library	which	produces	publication-quality	figures	in	a	variety	of	hardcopy	formats	and	interactive
#  environments	across	platforms

# In[25]:


import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[2]:


plt.plot([2,4,6,4,8])
plt.xlabel("Indices")
plt.ylabel("Numbers")
plt.title("Myplot")
plt.show()


# In[3]:


plt.plot([1,2,3,4],[1,4,8,16])
plt.ylabel("squares")
plt.xlabel("numbers")
plt.grid()
plt.show()


# In[4]:


plt.plot([1,2,3,4],[1,4,9,16],"ro")
plt.grid()
plt.show()


#  If	matplotlib	were	limited	to	working	with	lists,	it	would	be	fairly	useless	for	numeric	processing.	generally,	you	will	use	numpy	arrays.	In	fact
#  all	sequences	are	converted	to	numpy	arrays	internally

# In[6]:


import numpy as np

t = np.arange(0,5,0.2)

plt.plot(t,t ** 2 , "b--",label = "^2")
plt.plot(t,t ** 2.2, "rs", label = "^2.2")
plt.plot(t, t ** 2.5, "g^", label = "^2.5")

plt.grid()
plt.legend()
plt.show()


# In[8]:


x1 = [1,2,3,4]
y1 = [1,4,9,16]
x2 = [1,2,3,4]
y2 = [2,4,6,8]
lines = plt.plot(x1,y1,x2,y2)

plt.setp(lines[0],color = "r",linewidth = 2.0)
plt.setp(lines[1],color = "g",linewidth = 2.0)
plt.grid()


# #  Working	with	multiple	figures	&	axes

# In[15]:


fig,ax = plt.subplots(2,1, figsize = (8,8))

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0,5,0.1)
t2 = np.arange(0,5,0.02)

ax[0].plot(t1,f(t1),"b-")
ax[0].grid()


ax[1].plot(t2,np.cos(2*np.pi*t2),"r--")
ax[1].grid()
plt.show()


# # Bar	Chart	

# In[31]:


x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]

plt.figure(figsize = (8,8))
plt.bar(x,y,label = "Bar1")
plt.bar(x2,y2,label = "Bar2")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph")
plt.legend()
plt.show()


# In[32]:


population_ages	=	[22,55,62,45,21,22,34,42,42,4,99,102,110,120,
                     121,130,111,115,112,80,75,65,54,44,43,42,48]

ids = [x for x in range(len(population_ages))]
plt.figure(figsize = (8,8))
plt.bar(ids,population_ages)


# In[33]:


bins =	[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
population_ages	=	[22,55,62,45,21,22,34,42,42,4,99,102,110,120,
                     121,130,111,115,112,80,75,65,54,44,43,42,48]
plt.figure(figsize = (8,6))
plt.hist(population_ages,bins,color = "red")


# In[34]:


bins =	[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
population_ages	=	[22,55,62,45,21,22,34,42,42,4,99,102,110,120,
                     121,130,111,115,112,80,75,65,54,44,43,42,48]
plt.figure(figsize = (8,6))
plt.hist(population_ages,bins,histtype = "bar",rwidth = 0.8,color = "green")


# In[35]:


plt.figure(figsize = (8,6))
plt.hist(population_ages,	bins,	histtype='bar',rwidth=0.8,color = "green")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs')
plt.legend()
plt.show()


# In[ ]:




