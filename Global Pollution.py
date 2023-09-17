#!/usr/bin/env python
# coding: utf-8

# In[1]:


#installing libraries
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import requests
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[2]:


# Identify the distribution of data in the dataset.


# In[3]:


#Loading data to DataFrame
df = pd.read_csv(r"C:\Users\bajwa\Dropbox\PC\Downloads\GlobalPollution.csv")


# In[4]:


df


# In[5]:


#Checking null values
df.isnull().sum()


# In[6]:


df['composition_food_organic_waste_percent'].fillna(0,inplace=True)


# In[7]:


df['composition_glass_percent'].fillna(0,inplace=True)


# In[8]:


df['composition_metal_percent'].fillna(0,inplace=True)


# In[9]:


df['composition_other_percent'].fillna(0,inplace=True)


# In[10]:


df['composition_paper_cardboard_percent'].fillna(0,inplace=True)


# In[11]:


df['composition_plastic_percent'].fillna(0,inplace=True)


# In[12]:


df['composition_rubber_leather_percent'].fillna(0,inplace=True)


# In[13]:


df['composition_wood_percent'].fillna(0,inplace=True)


# In[14]:


df['composition_yard_garden_green_waste_percent'].fillna(0,inplace=True)


# In[15]:


df['other_information_information_system_for_solid_waste_management'].fillna('None',inplace=True)


# In[16]:


df['other_information_national_agency_to_enforce_solid_waste_laws_and_regulations'].fillna('None',inplace=True)


# In[17]:


df['other_information_national_law_governing_solid_waste_management_in_the_country'].fillna('None',inplace=True)


# In[18]:


df['other_information_ppp_rules_and_regulations'].fillna('None',inplace=True)


# In[19]:


df['other_information_summary_of_key_solid_waste_information_made_available_to_the_public'].fillna('None',inplace=True)


# In[20]:


df['special_waste_agricultural_waste_tons_year'].fillna(0,inplace=True)


# In[21]:


df['special_waste_construction_and_demolition_waste_tons_year'].fillna(0,inplace=True)


# In[22]:


df['special_waste_e_waste_tons_year'].fillna(0,inplace=True)


# In[23]:


df['special_waste_hazardous_waste_tons_year'].fillna(0,inplace=True)


# In[24]:


df['special_waste_industrial_waste_tons_year'].fillna(0,inplace=True)


# In[25]:


df['special_waste_medical_waste_tons_year'].fillna(0,inplace=True)


# In[26]:


df['total_msw_total_msw_generated_tons_year'].fillna(0,inplace=True)


# In[27]:


#Q1: Finding correlations
df.corr()


# In[28]:


import seaborn as sns 
sns.distplot(df['composition_food_organic_waste_percent'], kde = True)


# In[29]:


import matplotlib as mpl
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.hist(df['composition_metal_percent']) 


# In[30]:


# finding outliers in the dataset as there is always outliers because in the global pollution data pollution is always higher
#than expected data as pollution is always higher than expected


# In[31]:


df_cv = pd.DataFrame(data=df['composition_metal_percent'])
df_cv.plot(kind='box', figsize=(8,6))
plt.show()


# In[32]:


df['composition_metal_percent'].dropna(axis=0,inplace=True) 
Q1,Q3=df['composition_metal_percent'].quantile(.25),df['composition_metal_percent'].quantile(.75)
IQR=Q3 - Q1
print('The Inter Quartile Range for composition_metal_percent:', IQR)


# In[33]:


upper=Q3+(IQR*1.5)
lower=Q1-(IQR*1.5)

print('Upper Bound:', upper)
print('Lower Bound:', lower)


# In[34]:


(df['composition_metal_percent']<lower) | (df['composition_metal_percent']>upper)


# In[35]:


df2 = df['composition_metal_percent'].clip(upper, lower)
df2.describe()


# In[36]:


df['composition_metal_percent'].median()


# In[37]:


# what is the highest composition_paper_cardboard_percent


# In[38]:


df['composition_paper_cardboard_percent'].max()


# In[39]:


#which country has the highest number of gdp


# In[40]:


df[['country_name','gdp']].max()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




