#!/usr/bin/env python
# coding: utf-8

# In[3]:


CONTROL FLOW :- 
 1. IF-statement :- The if statement allows you to execute a block of code if a certain condition is true.

x = 5

if x >= 5:
  print("x is greter than 4")
  


# In[4]:


2. If-else statement :- If given statement condition is false then go for another statement.
 Example:-
age = 20
if age >= 18:
    print("You are adult")
    print("You can vote")
else:
    print("You are child")
    print("thankyou")
        
        


# In[5]:


Example :-
x = 3
if x > 2:
    print("x is positive")
else:
    print("x is negative")


# In[7]:


If-elif-else :-  The if-elif-else statement allows you to check multiple conditions in sequence.
Example :-
    

x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# In[9]:


4.Nested if-else statement :-  A nested if-else is an if-else statement inside another if or else block.

Example :-

fruit = input("Enter a fruit (apple, banana, or strawberry): ")

if fruit == "apple":
    print("Apples are usually red or green  price is 25rs.")
elif fruit == "banana":
    print("Bananas are typically yellow when ripe.")
elif fruit == "strwberry":
    color = input("Are the strawberrys red or black? ")
    if color == "red":
        print("Red strawberrys are sweet.")
    elif color == "black":
        print("Black strawberrys are tart.")
    else:
        print("Invalid color.")
else:
    print("This froot not available.") 


# In[ ]:




