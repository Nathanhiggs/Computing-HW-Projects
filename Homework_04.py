#!/usr/bin/env python
# coding: utf-8

# In[61]:


#Question 1:
import numpy as np

np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])


# In[62]:


#Question 2:
import numpy as np

x = np.array([1,2,3,4,5,6])
y = np.array([5,6,7,8,9,10])
print(x,y)


# In[64]:


#Question 3:
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6])
y = np.array([5,6,7,8,9,10])

plt.plot(x,y)
plt.show()


# In[65]:


#Question 4:
import matplotlib.pyplot as plt

x = np.array([2,3,5,8,13])
y1 = np.array([1,2,3,4,5])
y2 = np.array([5,7,8,9,10])
y3 = np.array([4,7,11,12,14])

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.title("Question 4")
plt.xlabel("x-label")
plt.ylabel("y-label")

plt.show()


# In[66]:


#Question 5:
import matplotlib.pyplot as plt

#plot 1:
season = np.array(["June", "July", "August", "September", "October"])
temp = np.array([75, 80, 75, 65, 55])

plt.subplot(2, 1, 1)

plt.title("Temperature by Month")
plt.xlabel("Temperature (Degrees Fahrenheit)")
plt.ylabel("Month")

plt.plot(season, temp)

#plot 2:
drown = np.array([12, 16, 11, 3, 0])

plt.subplot(2, 1, 2)

plt.title("Drownings by Month")
plt.xlabel("# of Drowning Deaths")
plt.ylabel("Month")

plt.plot(season, drown)

plt.show()

