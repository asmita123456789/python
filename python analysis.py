#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


mk = pd.read_excel("C:/Users/Lenovo/Desktop/college marks.xlsx")


# In[29]:


print(mk)


# In[30]:


mk.tail()


# In[31]:


mk.head(6)


# In[32]:


mk.index


# In[33]:


mk.columns


# In[34]:


mk.dtypes


# In[35]:


mk.values


# In[36]:


mk.shape


# In[37]:


mk["Python"].value_counts()


# In[38]:


mk.describe()


# In[39]:


mk["Total"].value_counts


# In[40]:


mk.dropna(how="all")   


# In[41]:


mk.tail()


# In[42]:


mk.dropna(how="any")       


# In[43]:


mk.dropna(subset=["math"])


# In[18]:


mk.dropna(subset=["English"])


# In[44]:


mk.dropna(subset=["math","English"])


# In[45]:


mk["Python"].fillna(0)


# In[46]:


mk["Python"].fillna("Absent")


# In[47]:


mk['math'].fillna(0,inplace=True)
mk["Python"].fillna("none", inplace=True)
mk.tail(10)


# In[48]:


mk.info()


# In[49]:


mk["math"]


# In[50]:


mk["math"].astype("int")


# In[51]:


mk.info()


# In[52]:


mk["math"] = mk["math"].astype("int")
mk.head()


# In[53]:


mk=mk.dropna()
mk


# In[54]:


mk["S E"]= [float(str(i).replace("*", "#")) for i in mk["S E"]]


# In[55]:


mk["S E"]


# In[56]:


mk["Total"]


# In[57]:


mk.groupby(['Name'])['Java'].count()


# In[58]:


Name_counts=mk.value_counts(subset=["Java"],sort=True)


# In[59]:


Name_counts


# In[61]:


Name_counts.plot.bar()


# In[62]:


plt.figure(figsize=(15,5))
Name_counts.plot.bar();
plt.savefig('Name_from_Name.png')


# In[63]:


top_10_Name=Name_counts.iloc[:6]
plt.ylabel('Number of Java')
top_10_Name.plot.bar();

print(top_10_Name)
plt.savefig('Top_10_Name.png')


# In[45]:


plt.hist(mk["Java"])
plt.xlabel('Java')
plt.ylabel('Name')
plt.axvline(mk["Java"].mean(), color='y', linestyle='dashed', linewidth=1)
plt.plot()
plt.savefig('Java_Distribution.png')


# In[46]:


Name=mk.groupby(['Name'])["Total"].count()
Name_counts=mk.value_counts(subset=['Name'],sort=True)
plt.figure(figsize=(10,5))
Name_counts.plot.bar();
plt.savefig('Name.png')


# In[47]:


Total=mk[['Total','Name']]


# In[48]:


highest_Total=Total.iloc[:10]
top_10_highest_Total= highest_Total.iloc[:10]


# In[49]:


top_10_highest_Total.set_index('Name',inplace=True)


# In[50]:


top_10_highest_Total.plot.bar();
plt.savefig('Top_10_highest_Total.png')


# In[94]:


bins=[18,22,26,32,36,40,44]
labels = ['38-42','42-46','46-62','62-86','86-90','90-99']
mk["Total"] = pd. cut(mk["Java"], bins=bins, labels=labels, right=False)
print (mk[["Java",'Total']])


# In[95]:


Total=mk[['Java','Total']]


# In[96]:


Total
mk.set_index('Total',inplace=True)


# In[97]:


Total_category=Total.value_counts('Java',sort=False)
Total_category


# In[98]:


Total_category.plot(kind='pie',autopct='%1.1f%%');


# In[91]:


Total_category.plot.bar();
plt.ylabel('Number of Name');


# In[92]:


Total=mk["Name"].value_counts()


# In[93]:


Total.plot(kind='pie',autopct='%1.1f%%');


# In[ ]:





# In[ ]:




