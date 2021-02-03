#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[50]:


#Question 1:
color = ["blue", "purple", "green"]
print(color[0]) #calls the corresponding str from the list 'color'
print(color[1])
print(color[2])


# In[101]:


#Question 2:
n = 0
for n in range(0,10): #while n is in range of 0 through 10
    print(n) #prints n
    n=n+1 #adds 1 to n through each loop


# In[7]:


#Question 3:
n = 0
while n < 10: #loop continues increasing n by 1
    print(n) #prints n until n = 10
    n = n + 1


# In[9]:


#Question 4:
n = 0
while n <= 10: #loop continues increasing n by 1 until it reaches 10
    print(n) #n is printed until n > 10
    n = n + 1
else:
    print("Greater than 10")


# In[97]:


#Question 5:
sum = 0 #needed so that loop can be rerun accurately when inputting new num
nums = 30 #input last integer in range
while(nums > 0):
    sum = sum + nums #same as sum += nums, adds current sum to whatever nums is currently at
    nums = nums - 1 #same as nums -= 1, counts backwards from upper bound of range
print("sum equals", sum)


# In[ ]:





# In[66]:




