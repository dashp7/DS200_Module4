#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as sco
import scipy.stats as scs


# In[2]:


df = pd.read_excel('./datasets/industry.xls')


# In[3]:


df


# In[4]:


#-------------------------DATA FOR SCATTERPLOT----------------------------#
all_r = np.array(df.iloc[:,3][:-1])
all_u = np.array(df.iloc[:,6][:-1])
log_r = np.log(all_r)
log_u = np.log(all_u)

reg=scs.linregress(log_r, log_u)
a=reg.slope
b=reg.intercept
fit_u=np.exp(b)*np.power(all_r,a)


# In[5]:


#--------------------------------SCATTERPLOT--------------------------------#

plt.rcParams.update({'lines.linewidth':0.75})
plt.rcParams.update({'font.size': 12})
fig, axes =plt.subplots(figsize=(6,4))


plt.subplot(1,1,1)
plt.title("Relation between rural and urban UIs")

plt.rcParams.update({'font.size': 10})
plt.grid(which='major')
plt.minorticks_on()
plt.grid(which='minor', alpha=0.2)
plt.scatter(all_r, all_u, marker = 'o', color='g',alpha=0.5, label='States')
plt.plot(all_r, fit_u, 'b', label='Best Fit($R^2$={:.2f})'.format(reg.rvalue))
plt.xscale('log')
plt.yscale('log')


plt.xlabel("No. of rural industrial units")
plt.ylabel("No. of urban industrial units")
plt.legend()
plt.tight_layout()
plt.savefig('scatterplot.jpg')
plt.show()


# In[6]:


#---------------------------DATA FOR BAR GRAPH--------------------------------#
states = np.array(df.iloc[:,0][:-1])
n = states.shape[0]
width = 0.35
index = np.arange(n)    


# In[7]:


#--------------------------------BAR GRAPH--------------------------------#
plt.rcParams.update({'lines.linewidth':1})
fig, axes =plt.subplots(figsize=(10,6))
plt.rcParams.update({'font.size': 10})
plt.subplot(1,1,1)

p1 = plt.bar(index-width/2, all_r,width, label='Rural')
p2 = plt.bar(index+width/2, all_u,width, label='Urban')

plt.xticks(index,states,rotation=90,fontsize=10)
plt.grid(which='major', alpha=0.75)
plt.minorticks_on()
plt.grid(which='minor', alpha=0.2)
plt.yscale('log')

plt.rcParams.update({'font.size': 12})
plt.xlabel("State", fontsize=12)
plt.ylabel("Number of industrial units", fontsize=12)
plt.legend()
plt.title("Distribution of unincorporated industries across states")
plt.tight_layout()
plt.savefig('bargraph.jpg')
plt.show()


# In[8]:


#---------------------------DATA FOR BOX PLOT---------------------------#
state_total = np.array(df.iloc[:,-2][:-1])
r_owa = np.array(df.iloc[:,1][:-1])/state_total
r_e = np.array(df.iloc[:,2][:-1])/state_total
u_owa = np.array(df.iloc[:,4][:-1])/state_total
u_e = np.array(df.iloc[:,5][:-1])/state_total


boxdat = np.zeros((r_owa.shape[0],4))
boxdat[:,0] = r_owa
boxdat[:,1] = r_e
boxdat[:,2] = u_owa
boxdat[:,3] = u_e
boxdat = boxdat*100
xlabs = ["Rural_OAE","Rural_E","Urban_OAE", "Urban_E"]


# In[9]:


#--------------------------------BOX PLOT--------------------------------#
plt.rcParams.update({'lines.linewidth':1})
fig, axes =plt.subplots(figsize=(6,6))

plt.rcParams.update({'font.size': 10})
plt.subplot(1,1,1)
plt.title("Distribution of unincorporated industries by ownership", fontsize=12)
plt.xlabel("Type of industrial unit", fontsize=12)
plt.ylabel("Percentage of total unincorporated industrial units", fontsize=12)
plt.grid(which='major', alpha=0.75)
plt.minorticks_on()
#plt.grid(which='minor', alpha=0.2)

plt.boxplot(boxdat, whiskerprops={'color' : 'tab:blue'}, patch_artist=True)

plt.xticks([1,2,3,4],xlabs)
plt.tight_layout()
plt.savefig('boxplot.jpg')

plt.show()


# In[ ]:




