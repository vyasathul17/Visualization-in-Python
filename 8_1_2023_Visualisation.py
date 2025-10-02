#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("cars (1).csv")


# In[3]:


data


# In[4]:


data.info()


# In[5]:


data['weightlbs'] = pd.to_numeric(data['weightlbs'], errors='coerce')
data['cubicinches'] = pd.to_numeric(data['cubicinches'], errors='coerce')
data


# In[6]:


data.info()


# In[7]:


data['cylinders'].value_counts()


# # Question 1
# Create scatter plots for the following data, make sure all the plots appear in the same plane with x-labels and y-labels evenly spaced.
# 
# 
# 1. ‘hp’ and ‘mpg’.
# 2. ‘hp’ and ‘time-to-60’.
# 3. ‘hp’ and ‘weightlbs’.
# 4. ‘hp’ and ‘cylinders’.
# 5. Create scatter plots with between (mpg-hp, mpg-weight), and (hp-mpg, hp-time-to-60) with respect to each brand.

# In[8]:


fig, axes = plt.subplots(2,2,figsize=(15,10))


plt.subplot(2,2,1)
sns.scatterplot(x=data['mpg'], y=data['hp'], data=data)
plt.title('MPG to HP data')
plt.xlabel("Miles per Gallon")
plt.ylabel("Horsepower")

plt.subplot(2,2,2)
sns.scatterplot(x=data['hp'], y=data['time-to-60'], data=data)
plt.title('HP to Time-to-60 data')
plt.xlabel("Horsepower")
plt.ylabel("Time-to-60")

plt.subplot(2,2,3)
sns.scatterplot(x=data['hp'], y=data['weightlbs'], data=data)
plt.title('HP to Weight Data')
plt.xlabel("Horsepower")
plt.ylabel("Weightlbs")
#plt.ylim(1500,5000)

plt.subplot(2,2,4)
sns.scatterplot(x=data['hp'], y=data['cylinders'], data=data)
plt.title('HP to Cylinders data')
plt.xlabel("Horsepower")
plt.ylabel("No of Cylinders")

plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()


# In[9]:


fig, axes = plt.subplots(2,2, figsize=(20,10))


plt.subplot(2,2,1)
sns.scatterplot(x=data['mpg'], y=data['hp'],hue=data['brand'], data=data)

plt.subplot(2,2,2)
sns.scatterplot(x=data['hp'], y=data['time-to-60'], hue=data['brand'], data=data)

plt.subplot(2,2,3)
sns.scatterplot(x=data['hp'], y=data['mpg'], hue=data['brand'], data=data)

plt.subplot(2,2,4)
sns.scatterplot(x=data['mpg'], y=data['weightlbs'], hue=data['brand'], data=data)


# # Question 2
# Create bar plots for the following, make sure all the plots appear in the same plane with x-labels and y-labels evenly spaced.
# 
# 1. Cylinders and Horsepower, Cylinders and miles per gallon, Cylinders and weight.
# 2. Year and time-to-60, Year and miles per gallon, Year and horsepower.
# 3. Create a bar plot that shows the visual representation of hp, mpg, weight, time-to-60 with respect to the number of cylinders for each of the brands.
# 4. Create a bar plot that shows the visual representation of hp, mpg, weight and time-to-60 with respect to the years, for each brand.

# In[10]:


fig, axes = plt.subplots(3,2, figsize=(20,10))
x1 = data['hp']
x2 = data['mpg']
x3 = data['weightlbs']
x4 = data['time-to-60']
x5 = data['cylinders']
x6 = data['year']
x7 = data['brand']
x8 = data['cubicinches']

plt.subplot(3,2,1)
plt.bar(x5,x1)
plt.title('Cylinders to HP data')
plt.xlabel("No of Cylinders")
plt.ylabel("Horsepower")

plt.subplot(3,2,2)
plt.bar(x5, x2)
plt.title("Cylinders to MPG Data")
plt.xlabel("Number of Cylinders")
plt.ylabel("Miles Per Gallon")

plt.subplot(3,2,3)
plt.bar(x5, x3)
plt.title("Cylinders to Weight Data")
plt.xlabel("Number of Cylinders")
plt.ylabel("Weight")

plt.subplot(3,2,4)
plt.bar(x6, x4)
plt.title("Year to time-to-60")
plt.xlabel("Year of Make")
plt.ylabel("time-to-60")

plt.subplot(3,2,5)
plt.bar(x6, x1)
plt.title("Year to Horsepower")
plt.xlabel("Year of Make")
plt.ylabel("Horsepower")

plt.subplot(3,2,6)
plt.bar(x6,x2)
plt.title("Year to Miles per Gallon")
plt.xlabel("Year of Make")
plt.ylabel("Miles Per Gallon")

plt.subplots_adjust(hspace=0.5)
plt.show()


# In[11]:


fig, axes = plt.subplots(2,2, figsize=(20,10))


plt.subplot(2,2,1)
sns.barplot(x=data['cylinders'], y=data['hp'], hue=data['brand'])
plt.title("Cylinders to HP")
plt.xlabel("Number of Cylinders")
plt.ylabel("Horsepower")

plt.subplot(2,2,2)
sns.barplot(x=data['cylinders'], y=data['mpg'], hue=data['brand'])
plt.title("Cylinders to MPG")
plt.xlabel("Number of Cylinders")
plt.ylabel("Miles Per Gallon")

plt.subplot(2,2,3)
sns.barplot(x=data['cylinders'], y=data['weightlbs'], hue=data['brand'])
plt.title("Cylinders to Weightlbs")
plt.xlabel("Number of Cylinders")
plt.ylabel("Weightlbs")

plt.subplot(2,2,4)
sns.barplot(x=data['cylinders'], y=data['time-to-60'], hue=data['brand'])
plt.title("Cylinders to time-to-60")
plt.xlabel("Number of Cylinders")
plt.ylabel("time-to-60")

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()


# In[12]:


fig, axes = plt.subplots(2,2, figsize=(25,15))


plt.subplot(2,2,1)
sns.barplot(x=data['year'], y=data['hp'], hue=data['brand'])
plt.title("Year to Miles per Gallon")
plt.xlabel("Year of Make")
plt.ylabel("Horsepower")

plt.subplot(2,2,2)
sns.barplot(x=data['year'], y=data['mpg'], hue=data['brand'])
plt.title("Year to Miles per Gallon")
plt.xlabel("Year of Make")
plt.ylabel("Miles Per Gallon")

plt.subplot(2,2,3)
sns.barplot(x=data['year'], y=data['weightlbs'], hue=data['brand'])
plt.title("Year to Weight")
plt.xlabel("Year of Make")
plt.ylabel("Weightlbs")

plt.subplot(2,2,4)
sns.barplot(x=data['year'], y=data['time-to-60'], hue=data['brand'])
plt.title("Year to Time to 60")
plt.xlabel("Year of Make")
plt.ylabel("Time to 60")

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()


# # Question 3
# Create box plots for the following:
# 
# 1. Create box plots for the columns hp, mpg, time-to-60, and weight lbs.
# 2. Create box plots for the columns in the step1 with respect to the number of cylinders and brand respectively.

# In[13]:


fig, axes = plt.subplots(2,2, figsize=(20,10))

plt.subplot(2,2,1)
sns.boxplot(data['hp'])
plt.title("Horsepower")

plt.subplot(2,2,2)
sns.boxplot(data['mpg'])
plt.title("Miles Per Gallon")

plt.subplot(2,2,3)
sns.boxplot(data['weightlbs'])
plt.title("Weightlbs")


plt.subplot(2,2,4)
sns.boxplot(data['time-to-60'])
plt.title("time-to-60")

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()


# In[14]:


fig, axes = plt.subplots(2,2, figsize=(20,10))


plt.subplot(2,2,1)
sns.boxplot(x=data['cylinders'], y=data['hp'], hue=data['brand'])
plt.title("Cylinders to Horsepower")
plt.xlabel("Number of cylinders")
plt.ylabel("Horsepower")

plt.subplot(2,2,2)
sns.boxplot(x=data['cylinders'], y=data['mpg'], hue=data['brand'])
plt.title("Cylinders to MPG")
plt.xlabel("Number of Cylinders")
plt.ylabel("Miles per gallon")

plt.subplot(2,2,3)
sns.boxplot(x=data['cylinders'], y=data['weightlbs'], hue=data['brand'])
plt.title("Cylinders to weightlbs")
plt.xlabel("Number of cylinders")
plt.ylabel("Weightlbs")

plt.subplot(2,2,4)
sns.boxplot(x=data['cylinders'], y=data['time-to-60'], hue=data['brand'])
plt.title("Cylinders to time-to-60")
plt.xlabel("Number of cylinders")
plt.ylabel("Time to 60")

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()


# # Question 4
# Create pair plots for the entire data to study various patterns in the data.
# 
# Create pair plots with respect to brand, number of cylinders, year, etc.

# In[15]:


sns.pairplot(data)


# In[16]:


sns.pairplot(data, hue='brand')


# In[17]:


sns.pairplot(data, hue='year')


# In[18]:


sns.pairplot(data, hue='cylinders')


# # Question 5
# Create a heatmap for the entire data to study correlation between each of the columns.

# In[19]:


#heatmap for correlation 
corr = data.corr()
sns.heatmap(corr)


# # Question 6
# Create a histogram for the following:
# 
# 1. Each column in the data to understand the distribution of the data.
# 2. Create histograms for hp, mpg, time-to-60, weight lbs, cubic inches, year, with respect to brand.

# In[20]:


fig, axes = plt.subplots(4,2, figsize=(20,10))


plt.subplot(4,2,1)
plt.hist(data['hp'])
plt.title("Horse Power")

plt.subplot(4,2,2)
plt.hist(data['mpg'])
plt.title('Miles Per Gallon')

plt.subplot(4,2,3)
plt.hist(data['time-to-60'])
plt.title('Time to 60')

plt.subplot(4,2,4)
plt.hist(data['cylinders'])
plt.title('Number of Cylinders')

plt.subplot(4,2,5)
plt.hist(data['weightlbs'])
plt.title('WeightLbs')

plt.subplot(4,2,6)
plt.hist(data['cubicinches'])
plt.title('Size in Cubic Inches')
plt.xlim(65, 460)

plt.subplot(4,2,7)
plt.hist(data['year'])
plt.title('Make Year')

plt.subplot(4,2,8)
plt.hist(data['brand'])
plt.title('Brand')

plt.subplots_adjust(hspace=0.5)
plt.show()


# In[21]:


fig, axes = plt.subplots(3,2, figsize=(20,10))


plt.subplot(3,2,1)
sns.histplot(x=data['hp'], hue=data['brand'])

plt.subplot(3,2,2)
sns.histplot(x=data['mpg'], hue=data['brand'])

plt.subplot(3,2,3)
sns.histplot(x=data['weightlbs'], hue=data['brand'])

plt.subplot(3,2,4)
sns.histplot(x=data['time-to-60'], hue=data['brand'])

plt.subplot(3,2,5)
sns.histplot(x=data['cubicinches'], hue=data['brand'])
plt.xlim(60,460)

plt.subplot(3,2,6)
sns.histplot(x=data['year'], hue=data['brand'])

plt.subplots_adjust(hspace=0.5)
plt.show()


# # Question 7
# Create line plots for the following:
# 
# 1. Create a line plot for the columns hp, mpg, time-to-60, weight lbs in a single plot, where each line is a different color. [red, green, blue, orange].
# 2. Line plot between hp-mpg, hp-(time-to-60), mpg-(time-to-60), hp-weight lbs, mpg-weight lbs, cubic inches-weight lbs.

# In[28]:


new_weight = data['weightlbs'].div(600)

sns.distplot(data['hp'], hist=False, color='Red')
sns.distplot(data['mpg'], hist=False, color='Green')
sns.distplot(data['time-to-60'], hist=False, color='Blue')
sns.distplot(new_weight, hist=False, color='Orange')


# In[29]:


fig, axes = plt.subplots(2,2, figsize=(20,10))


plt.subplot(2,2,1)
sns.lineplot(data= data, x='hp', y='mpg')

plt.subplot(2,2,2)
sns.lineplot(data= data, x='hp', y='time-to-60')

plt.subplot(2,2,3)
sns.lineplot(data= data, x='mpg', y='time-to-60')

plt.subplot(2,2,4)
sns.lineplot(data= data, x='hp', y='weightlbs')

plt.subplots_adjust(hspace=0.5)
plt.show()


# # Question 8
# Create a pie chart for the following columns and their distribution in the data:
# 
# Brands
# 
# Cylinders

# In[31]:


data_us = data.loc[(data['brand'] == ' US.')]
data_eu = data.loc[(data['brand'] == ' Europe.')]
data_jap = data.loc[(data['brand'] == ' Japan.')]

count_us = data_us['brand'].count()
count_eu = data_eu['brand'].count()
count_jap = data_jap['brand'].count()

x = [count_us, count_eu, count_jap]
y = ['USA', 'Europe', 'Japan']
plt.figure(figsize=(20,10))
plt.pie(x=x, labels=y, startangle=90)


# In[32]:


cylinder_1 = data.loc[(data['cylinders'] == 1.0)]
cylinder_2 = data.loc[(data['cylinders'] == 2.0)]
cylinder_3 = data.loc[(data['cylinders'] == 3.0)]
cylinder_4 = data.loc[(data['cylinders'] == 4.0)]
cylinder_5 = data.loc[(data['cylinders'] == 5.0)]
cylinder_6 = data.loc[(data['cylinders'] == 6.0)]
cylinder_7 = data.loc[(data['cylinders'] == 7.0)]
cylinder_8 = data.loc[(data['cylinders'] == 8.0)]

cyl_1 = cylinder_1['cylinders'].count()
cyl_2 = cylinder_2['cylinders'].count()
cyl_3 = cylinder_3['cylinders'].count()
cyl_4 = cylinder_4['cylinders'].count()
cyl_5 = cylinder_5['cylinders'].count()
cyl_6 = cylinder_6['cylinders'].count()
cyl_7 = cylinder_7['cylinders'].count()
cyl_8 = cylinder_8['cylinders'].count()


x = [cyl_1, cyl_2, cyl_3 ,cyl_4, cyl_5, cyl_6, cyl_7, cyl_8]
y = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
plt.figure(figsize=(20,10))
plt.pie(x=x, labels=y, startangle=90)


# # Question 9
# Create violin plots for the following:
# 
# hp, mpg, time-to-60, with respect to the number of cylinders for each brand.
# 
# hp, mpg, time-to-60, with respect to make year for each brand.

# In[33]:


fig, axes = plt.subplots(3,2, figsize=(20,10))


plt.subplot(3,2,1)
sns.violinplot(data= data, x='cylinders', y='mpg', hue='brand')

plt.subplot(3,2,3)
sns.violinplot(data= data, x='cylinders', y='hp', hue='brand')

plt.subplot(3,2,5)
sns.violinplot(data= data, x='cylinders', y='time-to-60', hue='brand')

plt.subplot(3,2,2)
sns.violinplot(data= data, x='year', y='time-to-60', hue='brand')

plt.subplot(3,2,4)
sns.violinplot(data= data, x='year', y='time-to-60', hue='brand')

plt.subplot(3,2,6)
sns.violinplot(data= data, x='year', y='time-to-60', hue='brand')

plt.subplots_adjust(hspace=0.5)
plt.show()


# # Question 10
# Create categorical plots for the following:
# 
# Hp, mpg, time-to-60, weight, cubic inches, with respect to each brand for various numbers of cylinders.

# In[34]:


sns.catplot(x='cylinders', y='hp', hue='brand', data=data)


# In[35]:


sns.catplot(x='cylinders', y='mpg', hue='brand', data=data)


# In[36]:


sns.catplot(x='cylinders', y='time-to-60', hue='brand', data=data)


# In[37]:


sns.catplot(x='cylinders', y='cubicinches', hue='brand', data=data)


# In[38]:


sns.catplot(x='cylinders', y='weightlbs', hue='brand', data=data)


# # Question 11
# In the Barplots created in step 2, do the following:
# 
# 1. Keep the color combination distinct for each of the bars in the plot.
# 2. Change the size of the plots to - (20, 15)
# 3. Change the font color to Red and Font size to 28 in the plots.

# In[39]:


plt.figure(figsize=(20,15))
sns.barplot(x='cylinders', y='hp', data=data)
plt.xlabel("Number of Cylinders in the Car", fontsize=28, color='Red')
plt.ylabel("Horsepower", fontsize=28, color='Red')
plt.show()


# # Question 12
# Create the area charts for the following:
# 
# 1. Mpg with respect to each brand of the car
# 2. Hp with respect to each brand of the car
# 3. Time-to-60 with respect to each brand of the car

# In[40]:


sns.histplot(data, x="mpg", hue="brand", element="poly")


# In[41]:


sns.histplot(data, x="mpg", hue="brand", element="bars")


# In[42]:


sns.histplot(data, x="mpg", hue="brand", element="step")


# In[43]:


sns.histplot(data, x="hp", hue="brand", element="poly")


# In[44]:


sns.histplot(data, x="time-to-60", hue="brand", element="poly")


# # Question 13
# Create Doughnut plots to represent the following:
# 
# 1. The year wise cars data.
# 2. The cars are based on various counts of cylinders.
# 3. The car brand data.

# In[45]:


y71 = data.loc[(data['year'] == 1971)]
y72 = data.loc[(data['year'] == 1972)]
y73 = data.loc[(data['year'] == 1973)]
y74 = data.loc[(data['year'] == 1974)]
y75 = data.loc[(data['year'] == 1975)]
y76 = data.loc[(data['year'] == 1976)]
y77 = data.loc[(data['year'] == 1977)]
y78 = data.loc[(data['year'] == 1978)]
y79 = data.loc[(data['year'] == 1979)]
y80 = data.loc[(data['year'] == 1980)]
y81 = data.loc[(data['year'] == 1981)]
y82 = data.loc[(data['year'] == 1982)]
y83 = data.loc[(data['year'] == 1983)]

year71 = y71['year'].count()
year72 = y72['year'].count()
year73 = y73['year'].count()
year74 = y74['year'].count()
year75 = y75['year'].count()
year76 = y76['year'].count()
year77 = y77['year'].count()
year78 = y78['year'].count()
year79 = y79['year'].count()
year80 = y80['year'].count()
year81 = y81['year'].count()
year82 = y82['year'].count()
year83 = y83['year'].count()


# In[46]:


x = [year71, year72, year73, year74, year75, year76, year77, year78, year79, year80, year81, year82, year83]
y = ['1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983']
plt.figure(figsize=(20,10))
plt.pie(x=x, labels=y, startangle=90)
circle = plt.Circle((0,0), 0.6, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.show()


# In[47]:


x = [cyl_1, cyl_2, cyl_3 ,cyl_4, cyl_5, cyl_6, cyl_7, cyl_8]
y = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
plt.figure(figsize=(20,10))
plt.pie(x=x, labels=y, startangle=90)
circle = plt.Circle( (0,0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)

plt.show()


# In[48]:


x = [count_us, count_eu, count_jap]
y = ['USA', 'Europe', 'Japan']
plt.figure(figsize=(20,10))
plt.pie(x=x, labels=y, startangle=90)
circle = plt.Circle( (0,0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.show()


# In[ ]:




