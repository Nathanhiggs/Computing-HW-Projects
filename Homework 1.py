#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1: 
color = ["purple", "blue", "green"] #list of favorite colors
print(type(color)) #prints what type the list is
print(color) #prints the list


# In[8]:


#Question 2:
numbers = list(range(30,63,3)) #creates a list ranging from 30 -> 60 by count of 3
print(numbers)


# In[21]:


#Question 3:
Weather = {"Sunny": "play", "Rainy": "watching TV", "Cloudy": "walk"} #constructs dictionary with corresponding keys and values
print(Weather) #prints out a list of the keys and corresponding values

Weather.update({"Snowy": "sled"}) #adds new key and value to dictionary
print(Weather)
Weather["Snowy"] #example of calling a value from a key in the list


# In[28]:


#Question 4:
grade = 85 #insert whatever grade into here, then run code
if grade >= 90: #A is printed if grade is in range >= 90
    print("A")
elif grade >= 80: #same is applied for B and C with 80 and 70 respectively
    print("B")
elif grade >= 70:
    print("C")
else: #if none of above conditions are filled, i.e. grade is below 70, then F is assigned
    print("F")
    


# In[ ]:




