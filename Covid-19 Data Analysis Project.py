#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[11]:


files=os.listdir('D:\Covid 19 Data Analysis')
files


# In[ ]:





# In[12]:


def read_data(path,filename):
    return pd.read_csv(path+'/'+filename)


# In[15]:


path='D:\Covid 19 Data Analysis'
world_data=read_data(path,'worldometer_data.csv')


# In[16]:


world_data.head()


# In[ ]:





# In[17]:


day_wise=read_data(path,files[2])


# In[18]:


group_data=read_data(path,files[3])


# In[19]:


usa_data=read_data(path,files[4])


# In[20]:


province_data=read_data(path,files[1])


# In[21]:


province_data.shape


# In[ ]:





# In[22]:


world_data.head()


# In[24]:


world_data.columns


# In[31]:


import plotly.express as px


# In[33]:


columns=['TotalCases','TotalDeaths','TotalRecovered','ActiveCases']
for i in columns:
    fig=px.treemap(world_data.iloc[0:20],values=i,path=['Country/Region'],title='Treemap represesntation of different countries with respect to their {}'.format(i))
    fig.show()


# In[34]:


day_wise.head()


# In[35]:


day_wise.columns


# In[36]:


px.line(day_wise,x='Date',y=['Confirmed', 'Deaths', 'Recovered', 'Active'],title='covid cases w.r.t to date',template='plotly_dark')


# In[ ]:





# In[39]:


world_data.head()


# In[38]:


pop_test_ratio=world_data['Population']/world_data['TotalTests'].iloc[0:20]


# In[41]:


fig=px.bar(world_data.iloc[0:20],x='Country/Region',y=pop_test_ratio[0:20],color='Country/Region',title='Population to tests done ratio')
fig.show()


# In[42]:


world_data.columns


# In[50]:


px.bar(world_data.iloc[0:20],x='Country/Region',y=['Serious,Critical','TotalDeaths','TotalRecovered','ActiveCases','TotalCases'])


# In[ ]:





# In[ ]:





# In[53]:


fig=px.bar(world_data.iloc[0:20],y='Country/Region',x='TotalCases',color='TotalCases',text='TotalCases')
fig.update_layout(template='plotly_dark',title_text='Top 20 countries in total confirmed cases')
fig.show()


# In[52]:


world_data.sort_values(by='TotalDeaths',ascending=False)


# In[54]:


fig=px.bar(world_data.sort_values(by='TotalDeaths',ascending=False)[0:20],y='Country/Region',x='TotalDeaths',color='TotalCases',text='TotalDeaths')
fig.update_layout(template='plotly_dark',title_text='Top 20 worst hit countries in total deaths')
fig.show()


# In[ ]:


world_data.columns


# In[55]:


fig=px.bar(world_data.sort_values(by='ActiveCases',ascending=False)[0:20],y='Country/Region',x='ActiveCases',color='ActiveCases',text='ActiveCases')
fig.update_layout(template='plotly_dark',title_text='Top 20 countries having maximum active cases')
fig.show()


# In[57]:


world_data.columns


# In[65]:


fig=px.bar(world_data.sort_values(by='TotalRecovered',ascending=False)[0:20],y='Country/Region',x='TotalRecovered',color='TotalRecovered',text='TotalRecovered')
fig.update_layout(template='plotly_dark',title_text='Top 20 countries having maximum recovered cases')
fig.show()


# In[ ]:





# In[72]:


labels=world_data[0:15]['Country/Region'].values
cases=['TotalCases','TotalDeaths','TotalRecovered','ActiveCases']
for i in cases:
    fig=px.pie(world_data[0:15],values=i,names=labels,hole=0.3,title=" {} recorded w.r.t WHO region of 15 worst affected countries".format(i))
    fig.show()


# In[ ]:





# In[ ]:


world_data.head()


# In[73]:


deaths_to_confirmed=world_data['TotalDeaths']/world_data['TotalCases']
deaths_to_confirmed


# In[ ]:





# In[75]:


px.bar(world_data,x='Country/Region',y=deaths_to_confirmed,title='Deaths to confirmed ratio of worst affected countries')


# In[ ]:





# In[78]:


deaths_to_recovered=world_data['TotalDeaths']/world_data['TotalRecovered']


# In[79]:


px.bar(world_data,x='Country/Region',y=deaths_to_recovered,title='Deaths to recovered ratio of worst affected countries')


# In[ ]:





# In[80]:


tests_to_confirmed=world_data['TotalTests']/world_data['TotalCases']


# In[81]:


px.bar(world_data,x='Country/Region',y=tests_to_confirmed,title='Number of tests to confirmed cases ratio of worst affected countries')


# In[ ]:





# In[83]:


world_data.head()


# In[84]:


group_data.head()


# In[ ]:





# In[ ]:





# In[94]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[104]:


def country_visualisation(df,country):
    data=df[df['Country/Region']==country]

    data2=data.loc[:,['Date','Confirmed','Deaths','Recovered','Active']]
    
    fig=make_subplots(rows=1,cols=4,subplot_titles=('confirmed','Active','Recovered','Deaths'))
    
    fig.add_trace(go.Scatter(name='Confirmed',x=data2['Date'],y=data2['Confirmed']),row=1,col=1)
    
    fig.add_trace(go.Scatter(name='Deaths',x=data2['Date'],y=data2['Deaths']),row=1,col=2)
        
    fig.add_trace(go.Scatter(name='Recovered',x=data2['Date'],y=data2['Recovered']),row=1,col=3)
            
    fig.add_trace(go.Scatter(name='Active',x=data2['Date'],y=data2['Active']),row=1,col=4)
    
    fig.update_layout(height=600,width=1000,title_text='Date vs Recorded cases of {}'.format(country),template='plotly_dark')
    fig.show()


# In[112]:


country_visualisation(group_data,'India')


# In[ ]:




