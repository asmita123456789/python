#!/usr/bin/env python
# coding: utf-8

# In[3]:


While loop :- A while loop statement executes the given statement as long as a given condition is true.

Example 1:-

count = 0
while(count < 5):
    print("count:", count)
    count = count + 1

Example 2 :- 
A = 1

while A <= 10:
    print(A)
    A += 1
    


# In[ ]:





# In[8]:


For loop :- The statement for loop allows you to iterate over a sequence and perform an action for each element.

Example :- 

fruits = ["apple", "banana", "strawberry"]
for fruit in fruits:
    print(fruit)


# In[2]:


Nested while loop :-
A nested while loop inside another loop.
Example :-
i = 1
while i <= 10:
    pratic = 1
    while pratic <= i:
        print("*",end="")
        pratic += 1
    print()
    i += 1


# In[3]:


Pass statement :- The pass statement is a no - operation statement. It's used when a statement is syntactically required but
you don't want any code to  execute.
 
    Example :-
def my_function():
    pass


# In[5]:


Nested for loop :- A nested for loop inside another loop.

Example :-

fruit = ["apple", "banana", "cherry","mango"]
colors = ["red", "yellow", "black","white"] 

for cherry in fruit:
   for color in colors:
      print(f"The {fruit} is {color}")


# In[9]:


Loop with Else :- In some languages, you can have an else block that  executes  if the loop completes without encounting a
break statement.

Example :-


i = 2

for i in range(2, num):
   if num % i == 0:
       print(f"{num} is not a prime number")
       break
       else:
           print(f"{num} is a prime number")




# In[13]:


Break :- 
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

for student in students:
    if student == 'Bob':
        break
    print(f'hey  bro how are you, {student}!')


# In[12]:


Continue :-

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

for student in students:
    if student == 'Charlie':
        print(f'Hello, {student}!')


# In[ ]:




