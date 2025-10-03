#!/usr/bin/env python
# coding: utf-8

# # Scatter plot

# In[2]:


import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[5]:


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label = "skitscat",color= "k",marker = "X",s = 500)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph")
plt.legend()
plt.show()


# # pie chart

# In[8]:


days = [1,2,3,4,5]
sleeping = [6,7,8,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.figure(figsize = (10,6))
slices = [7,2,2,13]
activities = ["sleeping","eating","working","playing"]
cols = ["c","m","r","b"]

plt.pie(slices,labels = activities, colors = cols, startangle = 90,shadow = True, 
        explode = (0,0.1,0,0),autopct = "%1.1f%%")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph")
plt.legend()
plt.show()


# # Stack	Plot

# In[10]:


days =	[1,2,3,4,5]
sleeping = [6,7,8,11,7]
eating = [2,3,4,3,2]
working	= [7,8,7,2,2,]
playing	=[8,5,7,8,13]

plt.figure(figsize = (8,8))
plt.plot([],[],color = "m",label = "sleeping",linewidth = 5)
plt.plot([],[],color = "c",label= "eating",linewidth = 5)
plt.plot([],[],color = "r",label = "working",linewidth = 5)
plt.plot([],[],color = "k",label = "playing	",linewidth = 5 )
plt.stackplot(days,sleeping,eating,working,playing,colors = ["m","c","r","k"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph")
plt.legend()
plt.show()


# In[ ]:




