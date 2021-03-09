#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd


# In[48]:


import csv
with open("people.csv") as csv_file:
    csvReader = csv.reader(csv_file)
    for row in csvReader:
        print(row)


# In[49]:


from pandas import DataFrame
df = pd.read_csv("people.csv")


# <b>Displaying data</b>

# In[50]:


pd.read_csv("people.csv")


# <b>Merging data using .merge() method</b>

# In[51]:


employees = {'Name': ['Alex', 'Bert', 'Carl', 'Elly', 'Ruth'],
            'Department': ['Accounting', 'HR', 'Sales', 'Accounting', 'Sales']}
employees = pd.DataFrame(employees)
print(employees)


# In[52]:


name_department = pd.read_csv("people.csv")


# In[53]:


name_department.merge(employees)


# In[54]:


import csv
with open("DeNiro_movies.csv") as csv_file:
    csvReader = csv.reader(csv_file)
    for row in csvReader:
        print(row)


# In[55]:


from pandas import DataFrame
df = pd.read_csv("DeNiro_movies.csv")


# In[56]:


pd.read_csv("DeNiro_movies.csv")


# In[57]:


movies = pd.read_csv("DeNiro_movies.csv")


# In[63]:


movies.sort_values('Year')


# <b>Identifying NaN values using .isnull() method</b>

# In[64]:


df.isnull()


# <b>Count NaN values. There are two columns with NaN values. Each column has 5 NaN values</b>

# In[65]:


df.isnull().sum()


# <b>Total count of NaN values is 10</b>

# In[66]:


df.isnull().sum().sum()


# <b>Drop columns with NaN values using function .dropna()<b/>

# In[67]:


df.dropna(how = "all", axis = 1)


# In[77]:


import csv
with open("Zillow_1.csv") as csv_file:
    csvReader = csv.reader(csv_file)
    for row in csvReader:
        print(row)


# In[78]:


from pandas import DataFrame
df = pd.read_csv("Zillow_1.csv")


# In[79]:


pd.read_csv("Zillow_1.csv")


# <b>Sort properties by number of bedrooms and list price in ascending order. </b>

# In[80]:


properties = pd.read_csv("Zillow_1.csv")


# In[82]:


properties.sort_values(['Beds', 'List_Price'])


# <b>Determine avarage property price by a zip code</b>

# In[83]:


properties.List_Price.mean()


# In[84]:


properties.groupby('Zip').List_Price.mean()


# <b>Count number of properties in each zip code and give minimum and maximum price</b>

# In[87]:


properties.groupby('Zip').List_Price.agg(['count', 'min', 'max'])


# In[ ]:




