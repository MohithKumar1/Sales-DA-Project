#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# In[2]:


#os is the operating system and if we want create, delete or make any changes in the directory it is used.


# In[3]:


files = [file for file in os.listdir('C:/Sales DA project/5-Sales Data Analysis/Sales_Data')]
for file in files:
    print(file)


# In[4]:


path = 'C:/Sales DA project/5-Sales Data Analysis/Sales_Data'
all_data = pd.DataFrame()

for file in files:
    current_df = pd.read_csv(path+'/'+file)
    all_data = pd.concat([all_data,current_df])
    
print(all_data)


# In[5]:


all_data.shape


# In[6]:


all_data.to_csv('C:/Sales DA project/5-Sales Data Analysis/Sales_Data/all_data.csv',index = False)

#all_data csv file is created in the directory


# In[7]:


all_data.head()


# In[8]:


all_data.isnull().sum()


# In[9]:


all_data = all_data.dropna(how = 'all')
all_data.shape


# What is the best month for sale?

# In[10]:


'04/19/19 08:46'.split('/')[0]


# In[11]:


def Month(x):
    return x.split('/')[0]


# In[12]:


all_data['Month'] = all_data['Order Date'].apply(Month)


# In[13]:


all_data.head()


# In[14]:


all_data.dtypes


# In[15]:


all_data['Month'].unique()


# In[16]:


filter = all_data['Month']=='Order Date'
all_data = all_data[~filter]
all_data


# In[17]:


all_data['Month']=all_data['Month'].astype(int)


# In[18]:


all_data.dtypes


# In[19]:


all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype(int)
all_data['Price Each'] = all_data['Price Each'].astype(float)


# In[20]:


all_data.dtypes


# In[21]:


all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']


# In[22]:


all_data.head()


# In[23]:


all_data.groupby('Month')['Sales'].sum()


# In[24]:


months = range(1,13)
plt.bar(months,all_data.groupby('Month')['Sales'].sum())
plt.xticks(months)
plt.xlabel('Month')
plt.ylabel('Sales in USD')

###

Ticks are the value on the axis to show the coordinates on the graph. It is the value on the axes by which we can visualize where will a specific coordinate lie on a graph. Whenever we plot a graph, ticks values are adjusted according to the data, which is sufficient in common situations, but it is not ideal whenever we plot data on a graph.
# In[25]:


all_data.head()


# Which city has maximum orders?

# In[26]:


'917 1st St, Dallas, TX 75001'.split(',')[1]


# In[27]:


def City(x):
    return x.split(',')[1]


# In[28]:


all_data['City'] = all_data['Purchase Address'].apply(City)


# In[29]:


all_data.head()


# In[30]:


all_data.groupby('City')['City'].count().plot.bar()


# At what time sales of product purchase is maximum?

# In[31]:


all_data['Order Date'].dtype


# In[32]:


all_data['Hour'] = pd.to_datetime(all_data['Order Date']).dt.hour


# In[33]:


all_data.head()


# In[34]:


keys=[]
hour=[]
for key,hour_df in all_data.groupby('Hour'):
    keys.append(key)
    hour.append(len(hour_df))


# In[35]:


keys


# In[36]:


hour


# In[37]:


plt.plot(keys,hour)
plt.grid()


# What product sold the most and why?

# In[38]:


all_data.groupby('Product')['Quantity Ordered'].sum()


# In[39]:


all_data.groupby('Product')['Quantity Ordered'].sum().plot(kind = 'bar')


# In[40]:


all_data.groupby('Product')['Price Each'].mean()


# In[41]:


products = all_data.groupby('Product')['Quantity Ordered'].sum().index
quantity = all_data.groupby('Product')['Quantity Ordered'].sum()
prices = all_data.groupby('Product')['Price Each'].mean()


# In[42]:


fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(products,quantity,color = 'g')
ax2.plot(products,prices)
ax1.set_xticklabels(products,rotation = 'vertical', size = 8)


# What products are most often sold together?

# In[43]:


all_data.head()


# In[44]:


df = all_data['Order ID'].duplicated(keep = False)
df


# In[48]:


df2 = all_data[df]
df2.head()


# In[49]:


df2['Grouped'] = df2.groupby('Order ID')['Product'].transform(lambda x:','.join(x))


# In[50]:


df2.head()


# In[51]:


df2 = df2.drop_duplicates(subset = ['Order ID'])
df2.head()


# In[59]:


X = df2['Grouped'].value_counts()
X


# In[57]:


X[0:5].plot.pie()


# In[ ]:




