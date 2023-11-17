#!/usr/bin/env python
# coding: utf-8

# In[275]:


import numpy as np
import seaborn as sns
import pandas as pd
sns.set(color_codes=True)

from scipy import stats
import matplotlib.pyplot as plt
import os.path as path
plt.rcParams.update({'font.size': 50})
sns.set(rc={"lines.linewidth": 8})
from itertools import cycle


import PyIO
import PyPluMA

class LRPlotPlugin:
 def input(self, inputfile):
     self.myfiles = PyIO.readSequential(inputfile)
 def run(self):
     pass
 def output(self, outputfile):
  # In[364]:


  fiu_lr = pd.read_csv(PyPluMA.prefix()+"/"+self.myfiles[0], header=None, index_col=None)
  fiu_lr.columns = ['traces','trace_name', 'algo', 'hits', 'misses', 'filters', 'size',
                  'cache_size', 'method', 'Hit-rate', 'time', 'text', 'text2', 'text3', 'Learning rate']

  fig = plt.figure(figsize=(10, 8))
  labels= [0.00, 0.0, 0.25, 0.50, 0.75, 1.0]
  ax = sns.lineplot(x="Learning rate", y="Hit-rate", data=fiu_lr, color='black')
  ax.set_xlabel("Learning Rate",fontsize=20)
  ax.set_ylabel("Hit Rate (%)",fontsize=20)
  ax.tick_params(labelsize=20)
  ax.set_xticklabels(labels)

  #fig.tight_layout()
  plt.savefig(outputfile+"/fiu_webresearch3.png", dpi=100)


  # In[365]:


  msr_lr = pd.read_csv(PyPluMA.prefix()+"/"+self.myfiles[1], header=None, index_col=None)
  msr_lr.columns = ['traces','trace_name', 'algo', 'hits', 'misses', 'filters', 'size',
                  'cache_size', 'method', 'Hit-rate', 'time', 'text', 'text2', 'Learning rate']

  d1=msr_lr[msr_lr['traces']=="/scratch/msr/rsrch_0.csv"]
  d2=msr_lr[msr_lr['traces']=="/scratch/msr/stg_1.csv"]

  fig = plt.figure(figsize=(10,8))
  ax = sns.lineplot(x="Learning rate", y="Hit-rate", 
                  data=d1, color='black')
  ax.set_xlabel("Learning Rate",fontsize=50)
  ax.set_ylabel("",fontsize=50)
  ax.tick_params(labelsize=50)
  #fig.tight_layout()
  plt.savefig(outputfile+"/msr_rsrch_0.png", dpi=100)


  # In[366]:


  plt.figure(figsize=(10,8))

  ax = sns.lineplot(x="Learning rate", y="Hit-rate", 
                  data=d2, color='black')
  ax.set_xlabel("Learning Rate",fontsize=30)
  ax.set_ylabel("",fontsize=30)
  ax.tick_params(labelsize=30)
  plt.savefig(outputfile+"/msr_stg_1.png", bbox_inches="tight", dpi=100)


  # In[368]:


  cloudcache_lr = pd.read_csv(PyPluMA.prefix()+"/"+self.myfiles[2], header=None, index_col=None)
  cloudcache_lr.columns = ['traces','trace_name', 'algo', 'hits', 'misses', 'filters', 'size',
                  'cache_size', 'method', 'Hit-rate', 'time', 'text', 'text2', 'Learning rate']

  fig = plt.figure(figsize=(10,8))

  ax = sns.lineplot(x="Learning rate", y="Hit-rate", 
                  data=cloudcache_lr[cloudcache_lr['traces']=="/scratch/CloudCache/webserver-2012-11-01-1.blk"], color='black')
  ax.set_xlabel("Learning Rate",fontsize=50)
  ax.set_ylabel("",fontsize=50)
  ax.tick_params(labelsize=50)
  #fig.tight_layout()
  plt.savefig(outputfile+"/cloudcache_webserver_11-01-1.png", dpi=100)


  # In[369]:


  ax = sns.lineplot(x="Learning rate", y="Hit-rate", 
                  data=cloudcache_lr[cloudcache_lr['traces']=="/scratch/CloudCache/webserver-2012-11-15-1.blk"], color='black')

  plt.figure(figsize=(10,8))

  ax.set_xlabel("Learning Rate",fontsize=30)
  ax.set_ylabel("",fontsize=30)
  ax.tick_params(labelsize=30)
  plt.savefig(outputfile+"/cloudcache_webserver_11-15-1.png", bbox_inches="tight", dpi=100)


  # In[370]:


  cloudvps_lr = pd.read_csv(PyPluMA.prefix()+"/"+self.myfiles[3], header=None, index_col=None)
  cloudvps_lr.columns = ['traces','trace_name', 'algo', 'hits', 'misses', 'filters', 'size',
                  'cache_size', 'method', 'Hit-rate', 'time', 'text', 'text2', 'Learning rate']

  fig = plt.figure(figsize=(10,8))

  ax = sns.lineplot(x="Learning rate", y="Hit-rate", 
                  data=cloudvps_lr, color='black')
  ax.set_xlabel("Learning Rate",fontsize=50)
  ax.set_ylabel("",fontsize=50)
  ax.tick_params(labelsize=50)
  #fig.tight_layout()
  plt.savefig(outputfile+"/cloudvps_vps26020-1.png", dpi=100)


  # In[371]:


  physics_lr = pd.read_csv(PyPluMA.prefix()+"/"+self.myfiles[4], header=None, index_col=None)
  physics_lr.columns = ['traces','trace_name', 'algo', 'hits', 'misses', 'filters', 'size',
                  'cache_size', 'method', 'Hit-rate', 'time', 'text', 'text2', 'Learning rate']

  #d1=physics_lr[physics_lr['traces']=="/scratch/physics/w20_vscsi1.itrace"]
  #d2=physics_lr[physics_lr['traces']=="/scratch/physics/w40_vscsi1.itrace"]

  fig = plt.figure(figsize=(10,8))

  ax = sns.lineplot(x="Learning rate", y="Hit-rate", data=physics_lr, color='black')
  ax.set_xlabel("Learning Rate",fontsize=50)
  #ax.set_ylim([81.77,81.93])
  ax.tick_params(labelsize=50)
  ax.set_ylabel("",fontsize=50)
  #fig.tight_layout()
  plt.savefig(outputfile+"/physics_w70.png", dpi=100)


  # In[ ]:




