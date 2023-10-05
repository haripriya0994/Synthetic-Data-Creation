#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from itertools import cycle


# In[2]:


given_date = datetime(2023, 9, 3) 

num_days=30
dat=[]
for _ in range(num_days):
    dat.append(given_date.strftime('%d-%m-%Y'))
    given_date += timedelta(days=1)
    
dat

dat *=100

df = pd.DataFrame({'Date':dat})


# In[3]:


camp=[]
for i in range(1,11):
    camp.append('campaign_'+str(i))
    
print(camp)


# In[4]:


from datetime import datetime, timedelta

given_date = datetime(2023, 7, 25)
num_days = 10
dat1 = []

for _ in range(num_days):
    dat1.append(given_date.strftime('%d-%m-%Y'))
    given_date += timedelta(days=10)
dat1


# In[5]:


Duration = [15,20,25]
end_dates=[]
dur_cycle=cycle(Duration)
for i in dat1:
    duration = next(dur_cycle)
    start_date = datetime.strptime(i, '%d-%m-%Y')
    end_date = start_date + timedelta(days=duration)
    end = end_date.strftime('%d-%m-%Y')
    end_dates.append(end)
end_dates


# In[6]:


camp *=300

df = pd.DataFrame({'Date':dat,'Campaign':camp,'Campaign_Start_Date':camp,'Campaign_End_Date':camp})
df


# In[7]:


l=['campaign_1', 'campaign_2', 'campaign_3', 'campaign_4', 
   'campaign_5', 'campaign_6', 'campaign_7', 'campaign_8', 'campaign_9', 'campaign_10']

m = ['25-07-2023',
 '04-08-2023',
 '14-08-2023',
 '24-08-2023',
 '03-09-2023',
 '13-09-2023',
 '23-09-2023',
 '03-10-2023',
 '13-10-2023',
 '23-10-2023']

n = ['09-08-2023',
 '24-08-2023',
 '08-09-2023',
 '08-09-2023',
 '23-09-2023',
 '08-10-2023',
 '08-10-2023',
 '23-10-2023',
 '07-11-2023',
 '07-11-2023']

camp_dict = {i:j for i,j in zip(l,m)}

date_dict = {p:q for p,q in zip(l,n)}

print(camp_dict)
print(date_dict)

df['Campaign_Start_Date'] = df['Campaign_Start_Date'].replace(camp_dict)

df['Campaign_End_Date'] = df['Campaign_End_Date'].replace(date_dict)


# In[8]:


df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Campaign_Start_Date'] = pd.to_datetime(df['Campaign_Start_Date'], format='%d-%m-%Y')
df['Campaign_End_Date'] = pd.to_datetime(df['Campaign_End_Date'], format='%d-%m-%Y')


# In[9]:


df['remaining'] = (df['Campaign_End_Date']-df['Date']).dt.days


# In[10]:


df['remaining'] 


# In[ ]:





# In[11]:


def status(x):
    if x<0:
        return "Completed"
    else:
        return "Active"
    

df['Campaign_Status'] = df['remaining'].apply(status)    
df['Campaign_Status']


# In[12]:


df

