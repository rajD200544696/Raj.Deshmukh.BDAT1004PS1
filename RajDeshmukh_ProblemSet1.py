#!/usr/bin/env python
# coding: utf-8

# # 1. What data type is each of the following?

# In[1]:


import math
print(type(5))
print(type(5.0))
print(type(5 > 1))
print(type('5'))
print(type(5 * 2))
print(type('5' * 2))
print(type('5' + '2'))
print(type(5 / 2))
print(type(5 % 2))
print(type({5, 2, 1}))
print(type(5 == 3))
print(math.pi)


# # 2.Write (and evaluate) C# expressions that answer these questions:
# a. How many letters are there in 'Supercalifragilisticexpialidocious'?
# 

# b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? 

# c. Which of the following words is the longest:
# Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or
# Bababadalgharaghtakamminarronnkonn?

# d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian',
# 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

# # 3.Implement function triangleArea(a,b,c) that takes as input the lengths of the 3
# sides of a triangle and returns the area of the triangle. By Heron's formula, the area
# of a triangle with side lengths a, b, and c is
# s(s - a)(s -b)(s -c)
# , where
# s = (a+b+c)/2.
# >>> triangleArea(2,2,2)
# 1.7320508075688772
# 

# In[2]:


import math
def triangleArea(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
areaoftriangle = triangleArea(2,2,2)
print(str(areaoftriangle)+ " is the area of triangle")


# # 4. Write a program in C# Sharp to separate odd and even integers in separate arrays.
# Go to the editor

# Test Data :

# Input the number of elements to be stored in the array :5

# element - 0 : 25

# element - 1 : 47 

# element - 2 : 42  

# element - 3 : 56

# element - 4 : 32

# Expected Output:

# The Even elements are:

# 42 56 32

# The Odd elements are :

# 25 47

# In[3]:


arr_len = int(input("Enter the number of elements to be put in array: "))
array = []
for x in range(arr_len):
    array.append(int(input("Enter the element - "+str(x)+": ")))

even_array = []
odd_array = []
for x in range(arr_len):
    if array[x]%2 == 1:
        odd_array.append(array[x])
    if array[x]%2 == 0:
        even_array.append(array[x])
        
print("The even elements are: ")
print(even_array)
print("The odd elements are: ")
print(odd_array)


# # 5. Solve

# a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False
# depending on whether the point (x,y) lies in the rectangle with lower left
# corner (x1,y1) and upper right corner (x2,y2).
# >>> inside(1,1,0,0,2,3)
# True
# >>> inside(-1,-1,0,0,2,3)
# False

# b. Use function inside() from part a. to write an expression that tests whether
# the point (1,1) lies in both of the following rectangles: one with lower left
# corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower
# left corner (0.5, 0.2) and upper right corner (1.1, 2). 

# In[7]:


def inside(x,y,x1,y1,x2,y2):
    if (x > x1 and x < x2) and (y > y1 and y < y2):
        print("True")
    else:
        print("False")
 
x = int(input("Enter the first point: "))
y = int(input("Enter the second point: "))
inside(x,y,0,0,2,3)
inside(1,1,0.3,0.5,1.1,0.7)
inside(1,1,0.5,0.2,1.1,2)


# # 6.You can turn a word into pig-Latin using the following two rules (simplified):

# If the word starts with a consonant, move that letter to the end and append
# 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'

# If the word starts with a vowel, simply append 'way' to the end of the word.
# For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For
# our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# Write a function pig() that takes a word (i.e., a string) as input and returns its pigLatin form. Your function should still work if the input word contains upper case
# characters. Your output should always be lower case however. 

# In[9]:


def pig(word):
    lengthofword = len(word)
    array = []
    for x in range(lengthofword):
        array.append(word[x])
    if array[0] != 'a':
        if array[0] != 'e':
            if array[0] != 'i':
                if array[0] != 'o':
                    if array[0] != 'u':
                        flag = array[0]
                        array.remove(array[0])
                        array.append(flag)
                        array.append('a')
                        array.append('y')
                    else:
                        array.append('w')
                        array.append('a')
                        array.append('y')
                else:
                    array.append('w')
                    array.append('a')
                    array.append('y')
            else:
                array.append('w')
                array.append('a')
                array.append('y')
        else:
            array.append('w')
            array.append('a')
            array.append('y')
    else:
        array.append('w')
        array.append('a')
        array.append('y')
    finalstring = ""
    for x in array:
        finalstring += x
    return finalstring
word = str(input("Enter the word: "))
finalword = pig(word)
print(finalword)


# # 7.File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.

# Write a function bldcount() that reads the file with name name and reports (i.e.,
# prints) how many patients there are in each bloodtype

# In[10]:


file = open("bloodtype1.txt", "r")
list = file.readlines()
for i in list:
    content = i.split()
bA = content.count('A')
bB = content.count('B')
bAB = content.count('AB')
bO = content.count('O')
bOO = content.count('OO')
print("There are" ,bA, "patients with blood group A")
print("There are" ,bB, "patients with blood group B")
print("There are" ,bAB, "patients with blood group AB")
print("There are" ,bO, "patients with blood group O")
print("There are" ,bOO, "patients with blood group OO")


# # 8. Write a function curconv() that takes as input:
# 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or
# 'EUR' for the Euro)

# 2. an amount

# In[11]:


def curconv(currency, amount):
    if currency == 'AUD':
        print(amount*1.0345157)
    if currency == 'CHF':
        print(amount*1.0237414)
    if currency == 'CNY':
        print(amount*0.1550176)
    if currency == 'DKK':
        print(amount*0.1651442)
    if currency == 'EUR':
        print(amount*1.2296544)
    if currency == 'GBP':
        print(amount*1.5550989)
    if currency == 'HKD':
        print(amount*0.1270207)
    if currency == 'INR':
        print(amount*0.0177643)
    if currency == 'JPY':
        print(amount*0.01241401)
    if currency == 'MXN':
        print(amount*0.0751848)
    if currency == 'MYR':
        print(amount*0.3145411)
    if currency == 'NOK':
        print(amount*0.1677063)
    if currency == 'NZD':
        print(amount*0.8003591)
    if currency == 'PHP':
        print(amount*0.0233234)
    if currency == 'SEK':
        print(amount*0.148269)
    if currency == 'SGD':
        print(amount*0.788871)
    if currency == 'THB':
        print(amount*0.0313789)
    
currency = str(input("Enter the currency: "))
amount = int(input("Enter the amount: "))
curconv(currency, amount)


# # 9.Each of the following will cause an exception (an error). Identify what type of exception each will cause.

# In[12]:


6 + 'a'


# In[13]:


test_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(list[11])


# In[14]:


import math
math.sqrt(-1.0)


# In[16]:


print(p)


# In[18]:


f = open("nofile.txt")


# # 10. Encryption is the process of hiding the meaning of a text by substituting letters in the message with other letters, according to some system. If the process is successful, no one but the intended recipient can understand the encrypted message. Cryptanalysis refers to attempts to undo the encryption, even if some details of the encryption are unknown (for example, if an encrypted message has been intercepted). The first step of cryptanalysis is often to build up a table of letter frequencies in the encrypted text. Assume that the string letters is already defined as 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a string as its only parameter, and returns a list of integers, showing the number of times each character appears in the text. Your function may ignore any characters that are not in letters. 

# In[19]:


def frequencies(sentence):
    random = "abcdefghijklmnopqrstuvwqyz"
    c = []
    for letter in random:
        count = sentence.count(letter)
        c.append(count)
    print(c)  

frequencies("The quick red fox got bored and went home.")
frequencies("apple")


# In[ ]:




