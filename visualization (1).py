#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# In[3]:


x = np.arange(1,5)
y = x ** 3
fig,ax = plt.subplots(2,2, figsize = (8,8))

ax[0,1].plot([1,2,3,4] , [1,4,9,16],"go")
ax[1,0].plot(x,y,"r")
ax[0,1].set_title("Squares")
ax[1,0].set_title("Cubes")
plt.show()


# In[5]:


sectors	=	["Sec 1"	,	"Sec 2"	,	"Sec 3"	,	"Sec 4"	,	"Sec 5"	]
sector_values	=	[23	,45	,17	,32	,29	]
plt.figure(figsize = (8,8))
plt.bar(sectors,sector_values, color = "green")
plt.title("Bar Graph")
plt.xlabel("sectors")
plt.ylabel("sector_values")
plt.show()


# Making	the	bar	graph	horizontal	is	as	easy	as	plt.barh(	).
# 
# Let’s	add	one	more	attribute	to	our	graphs	in	order	to	depict	the	amount	of	variance.

# In[7]:


sectors	=	["Sec 1"	,	"Sec 2"	,	"Sec 3"	,	"Sec 4"	,	"Sec 5"	]
sector_values	=	[23	,45	,17	,32	,29	]
varience	=	[2,4,3,2,4]
plt.figure(figsize = (8,8))
plt.barh(sectors,sector_values,xerr = varience ,color = "blue")
plt.show()
#	The	xerr=	allows	us	to	indicate	the	amount	of	variance	per	sector	value.	
#If	need	be	yerr=	is	also	an	option


# In[11]:


sectors	=	['Sec 1','Sec 2','Sec 3','Sec 4','Sec 5']
sector_values	=	[23	,45,17,32,29]
subsector_values	=	[20,40,20,30,30]
plt.figure(figsize = (8,8))
index= np.arange(5)
width = 0.30
plt.bar(index,sector_values,width,color = "green",label = "sector_values")
plt.bar(index+width,subsector_values,width,color = "blue",label = "subsector_values")
plt.title("Horizontally	Stacked	Bars")
plt.xlabel("Sectors")
plt.ylabel("sector values")
plt.xticks(index+width/2,sectors)
plt.legend(loc = "best")
plt.show()


# In[ ]:




