#!/usr/bin/env python
# coding: utf-8

# In[21]:


year = int(input('Введите год: '))
if year % 4 != 0:
    print('Обычный год')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный')
    else:
        print('Обычный год')
else:
    print('Обычный год')


# In[24]:


a= int(input("Номер билета:"))
b1=a%10
b2=a%100//10
b3=a%1000//100
Sum1=b1+b2+b3
b4=a%10000//1000
b5=a%100000//10000
b6=a%1000000//100000
Sum2=b4+b5+b6
if Sum1==Sum2:
    print("Счастливый билет")
else:
    print("Несчастливый билет")

