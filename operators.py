#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1. Arthimetic operator :- +,-,*,/,**

a = 22
b = 45
print(a + b)

print(a - b)

print(a / b)

print(a % b)

print(a ** b)
print(a // b)


# In[2]:


#''' e.g.:- 2 + 7
#Operators :- "+"
#operands :- "2", "7"'''


# In[11]:


# 2. Comparision operator:- >=, <=, ==, !=

a = 87
b = 78
if (a == b):
    print("a and b are equal")
else:
    print("a and b are not equal")


# In[12]:


a = 87
b = 78
if (a > b):
    print("a is greater than b")
else:
    print("a is not greater than b")


# In[13]:


a = 87
b = 78
if (a != b):
    print("a is not equal b")
else:
    print("a is equal b")


# In[22]:


# 3. Assignment operator :- +=, -=, *=, /=, %=, **=, //=
#a = 90
# = 25

a =- 8
print(a)

a += 8
print(a)

a *= 8
print(a)

a /= 8
print(a)

a **= 8
print(a)

a //= 8
print(a)



# In[25]:


# 4. Bitwise operator:- &, /, ^, ~, <<, >>

a = 10
b = 45
c = a & b
print(c)

c = a / b
print(c)

c = a ^ b
print(c)

c = a << b
print(c)

c = a >> b
print(c)


# In[29]:


# 5. Logical operator :- AND, OR, NOT

print(700 and 750)
print(8 or 0)
print(not 1)


# In[35]:


#6. Membership operator:- {in}    {in not}

a = 2
b = 0
list = [1, 2, 4, 5, 6]
if (a in list):
    print("a is in list")
    
if (b not in list):
    print("b is not in list")


# In[36]:


# 7. Identity operator:- {is}  {is not}

a = 2
b = 0
list = [1, 2, 4, 5, 6]
if (a in list):
    print("a is list")
    
if (b not in list):
    print("b is not  list")


# In[ ]:


''' pyathon is dynamically typed, which '''

