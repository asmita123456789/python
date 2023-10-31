#!/usr/bin/env python
# coding: utf-8

# In[ ]:


age = input("enter your age")
print(type(age))


# In[ ]:


#input("enter your name")
print("my name is 10")


# In[ ]:


input("enter your name")


# In[ ]:


#variables are used to store data in a program
input("enter your name")
print("my name is py")


# In[3]:


name = "Asha"
age = 20


# In[4]:


print(type(name))


# In[ ]:


input("What is your name")
name='Asmita'
print(name)


# In[13]:


import keyword
keywords = keyword.kwlist
print(keywords)


# In[6]:


# Indentation:
if x>5:
print("x is than 5")


# In[14]:


A = 5.22
print(int(A))


# In[ ]:


# dynamic typing you have specify the type of a variable when you declare
# it . the type inferred the runtime.
x = 5 
x = "hello"


# In[ ]:


A = 5
print(float(A))


# In[ ]:


a = 50
b = 50
print(b*a)


# In[11]:


#type casting 
A = 5
print(bool(A))
print(type(A))


# In[12]:


str1 = "7"          
str2 = "3.142"
str3 = "13"
num1 = 29
num2 = 6.67

print(int(str1))
print(type(str1))
print(float(str2))
print(float(str3))
print(str(num1))
print(str(num2))


# In[13]:


str3 = "13"
print(float(str3))
print(type(str3))


# In[15]:


my_integer = 42
my_string = str(my_integer)


# In[17]:


print(type(my_string))


# In[3]:


#Arithmatic operation
A = 5
print(a*6)

print(a-6)

print(a/6)

print(a//6)

print(a**6)

print(a%6)


# In[18]:


a = {"asmita": 20}
print(type(a))


# In[19]:


bank = "22"
my_bank_int = list(bank)
print(type(my_bank_int))  
print(type(bank))


# In[22]:


bank = "345"
my_bank_int = list(bank)
print(type(my_bank_int)) 
print(type(bank))


# In[23]:


a = ["inaya"]
print(type(a))


# In[ ]:


a = ["inaya"]
print(type(a))


# In[4]:


#Relational operator 
print(4>5)
print(4<5)
print(4>=5)
print(4<=5)
print(4==5)
print(4!=5)


# In[5]:


#logical operator
print(700 and 750)
print(8 or 0)
print(not 1)


# In[6]:


#Assignment operator 
a =- 8
print(a)


# In[7]:


#membership operator
print('o' in "madras")


# In[8]:


print(6 not in [1,12,3,4,5,6])


# In[2]:


x = 6

if x>


# In[9]:


#if statement 
x = 5
if x >= 5:
    print("x is greter than 4")



# In[10]:


# if-Else : statement
x = 3
if x > 2:
    print("x is positive")
else:
    print("x is negative")


# In[ ]:


# If elif else staement
x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# In[ ]:


# Nested if-else:
fruit = input("Enter a fruit (apple, banana ,or orange): ")
if fruit == "apple":
    print("Apples are usually red or blue price is 20rs.")
elif fruit == "banana":
    print("Bananas are typically yellow when ripe.")
elif fruit == "orange":
    color = input("Are the oranges red or blue? ")
    if color == "red":
        print("Red oranges are outdated")
    elif color == "blue":
        print("Blue oranges are poisiouons.")
    else:
        print("Invalid color.")
else:
    print("This fruit not available.")


# In[ ]:


#1
a = True
b = False
result = not (a or b)
print(f"not (a or b) is {result}")



# In[ ]:


#2
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("number is divisible by 2 is even")
else:
    print("number is not divisible by 2 is odd")
    


# In[ ]:


#3
result = 15 % 8
print(f"The remainder is {result}")


# In[ ]:


#4
x = [1,2,3,4,5]
y = [1,2,3,4,5]
if x <= y:
    print("x and y are refer to the same object")
else:
    print("x and y are refer different object")
    


# In[ ]:


#5
print(a in ["hello,world!"])


# In[1]:


#8
x =- 87
y =+ 57
print(x)
print(y)


# In[5]:


# 9
x = 56
if x <= 97:
    print("x is greater than 87")
    


# In[6]:


#10
a = 10
b = 24
print(a + b)


# In[ ]:


# # Write a Python program that compares two numbers and prints whether the first number is greater,
# smaller, or equal to the second number.


# In[11]:


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")


# In[9]:


#6
x = True 
y = False
print(not y) 
print(not x)


# In[16]:


for i in range(1,18):
    for j in range(1,11):
        print(i * j,end="\t")
    print()


# In[2]:


#7
x = True
y = False
print(x or y)
print(x and y)
print(not x)


# In[8]:


while True:
    print("hello world")


# In[18]:


total = 0
for num in range(1, 19):
    total += num
print(f"The sum is {total}")


# In[19]:


for num in range(2, 11, 2):
    print(num)


# In[ ]:


num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *=

