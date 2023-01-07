#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a Python code to return your Python version
import sys
print(sys.version)


# In[14]:


#Write a Python code to declare variable id="513".
#Print the following statement "customer id =513". [Don't use print("customer id
id = "513"
str = "Customer id ="

#method1
print (str + id)

#method2
sys.stdout.write("customer id = 513")


# In[15]:


#Run the following statement, why there is an error
id=id+1


# In[48]:


#Convert the variable id into an integer, increment it by 1.
#Assign the result to variable new_id.
#Print the new_id

id = int(id)
new_id = id + 1
print (new_id)


# In[28]:


#Write a Python code to print the following string in a specific format (see the
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

print("Twinkle, twinkle, little star \n\t How I wonder what you are!\n\t\t Up above the world so high, \n\t\t\t Like a diamond in the sky.")


# In[44]:


#Givin the following string variable, # Print the first element in the string
course="Python for Data Science"

print(course[0])


# In[45]:


# Print the element on the 13th index in the string
print(course[13])


# In[33]:


# Find the length of string
len(course)


# In[43]:


# Print the last element in the string [use negative index]
print(course[-1])


# In[51]:


# Take the slice on variable course with only index 11 to index 14
course[11:15]


# In[41]:


# Get every third element in the range from index 0 to index 20
course[0:20:3]


# In[42]:


# Concatenate course string with ", AI & Development"
course + ", AI & Development"


# In[46]:


# Replace all the spaces with (_). New string should looks like"Python_for_Data_S
course.replace(" ","_")


# In[47]:


# Convert all the characters in string to upper case
course.upper()

