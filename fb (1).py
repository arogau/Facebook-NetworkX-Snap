
# coding: utf-8

# In[2]:

import networkx as nx
import matplotlib.pyplot as plt


# #### Let's read the data of Facebook ego nodes. 

# In[3]:

g= nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype = int) 


# ####Worried about what is your data? let's have a look at number of data points in your file. 

# In[4]:

nx.info(g)


# ##### Now lets focus on developing a spring layout. Spring layout has a fixed edge to edge distance. 

# In[5]:

sp = nx.spring_layout(g)


# ###### to delete any of the previous opened figure

# In[8]:

plt.axis('off')


# In[15]:

fig, ax = plt.subplots(figsize=(20,20))
nx.draw_networkx(g, pos=sp, with_labels=False, node_size=25, ax=ax)


# In[ ]:

plt.show()

