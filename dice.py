#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
def dice():
    list=[1,2,3,4,5,6,7,8,9]
    print([random.choice(list),random.choice(list)])
    roll()
def roll():
    print('Do you want to roll a dice?')
    choice=input('Yes - Y No - N')
    if choice=='Y' or choice=='y':
        dice()
    elif choice=='N' or choice=='n':
        print('Have a good day')
    else:
        print('Invalid Input')
print('🎲Welcome to Dice World🎲')
print('\n')
roll()


# In[ ]:




