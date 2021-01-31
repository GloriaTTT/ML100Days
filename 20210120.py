#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
array1 = np.arange(30).reshape(5, 6)
print(array1)
for row in array1.flat:
    if ((row%6)==1):
        print(row)

    


# In[ ]:





# In[ ]:




