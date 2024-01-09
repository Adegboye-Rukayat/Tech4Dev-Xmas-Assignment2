#!/usr/bin/env python
# coding: utf-8

# # 1 output of the following print statements

# In[4]:


print("\ta\tb\tc")


# In[5]:


print("\\\\")


# In[6]:


print("'")


# In[7]:


print("\"\"\"")


# In[8]:


print("C:\nin\tthe downward spiral")


# # 2 write a print statement to produce this output; / \ // \\ /// \\\

# In[9]:


print("/")
print("\\")
print("\\\\")
print("//")
print("\\\\\\")
print("///")


# # 3 what print statement will generate this output? 
# This quote is from
# Irish poet Oscar Wilde:
# "Music makes one feel so romantic
# - at least it always gets on one's nerves-
#  which is the same thing nowadays."

# In[10]:


# use of escape character \"
print("This quote is from")
print("Irish poet Oscar Wilde:")
print("\"Music makes one feel so romantic") 
print("- at least it always gets on one's nerves-")
print("which is the same thing nowadays.\"")


# # OR

# In[11]:


# when trying to use quotation marks inside a sting, use opposite quotation i.e strings containing single quotes need to use
#double quotes and strings containing double quotes need to use single quotes.
print("This quote is from")
print("Irish poet Oscar Wilde:")
print('"Music makes one feel so romantic') 
print("- at least it always gets on one's nerves-")
print(' which is the same thing nowadays."')


# # 4 what print statement will generate this output? 
# 
# A "quoted", String is
#  'much' better if you learn
# the rules of "escape sequences".
# Also, ""represents an empty String.
# Dont't forget: use " instead of "!
#  '' is not the same as "
# 

# In[12]:


# use of escape character \" 
print("A \"quoted\", String is")
print(" 'much' better if you learn")
print("the rules of \"escape sequences\".")
print( "Also, \"\"represents an empty String.")
print(" Dont\'t forget: use \" instead of \"!")
print(" '' is not the same as \" ")


# # 5 What values result from the following expressions?

# In[13]:


9/5


# In[14]:


695%20


# In[15]:


7+6*5


# In[16]:


7*6+5


# In[17]:


248%100/5


# In[18]:


6*3-9/4


# In[19]:


(5-7)*4


# In[20]:


6+(18%(17-12))


# # Exercise 3

# In[21]:


#1 Maximum value of the given list
list = [2,4,7,4,23,5,1,4,8,9]
print(max(list))


# In[22]:


#2 calculate the average value of the given list
list = [4,7,1.5,11,53,12,46,84,23]
avg = sum(list) / len(list)
print(avg)


# In[23]:


#3 prints the given list of integers in reverse order 2,6,7,45,23,53,14,45,89,5
numbers = [2,6,7,45,23,53,14,45,89,5]
print(numbers[::-1])


# In[24]:


#4 A program that accepts two lists of integers and print true if each element in the first list is less than the element 
#at the same index in the second list. the program should print false if the lists are not the same length.


def compare_lists(list1, list2):
    # Check if the lists have the same length
    if len(list1) != len(list2):
        return False
    
    # Check if each element in list1 is less than the corresponding element in list2
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False
    
    return True

list1 = [2, 6, 7, 45, 23]
list2 = [3, 8, 9, 46, 24]

result = compare_lists(list1, list2)
print(result)


# In[25]:


#5 A program that accepts a list of integers and two indexes, then swaps the elements at those indexes

my_list = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
index1 = 2
index2 = 5



def swap_elements(lst, index1, index2):
    # Check if the indexes are within the bounds of the list
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        # Swap the elements at the specified indexes
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return lst
    else:
        return "Invalid indexes"


result = swap_elements(my_list, index1, index2)
print(result)


# In[26]:


my_list = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
index1 = 0
index2 = 9

def swap_elements(lst, index1, index2):
    # Check if the indexes are within the bounds of the list
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        # Swap the elements at the specified indexes
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return lst
    else:
        return "Invalid indexes"


result = swap_elements(my_list, index1, index2)
print(result)


# In[27]:


#6 
num1 = [9,8,7,6,5,4,3,2,1]
num2 = [1,2,3,4,5,6,7,8,9]
sum_numbers = num1+num2
sum_numbers


# In[28]:


list1 =[9,8,7,6,5,4,3,2,1]
list2 =[1,2,3,4,5,6,7,8,9]

def concatenate_lists(list1, list2):
    # Concatenate the two lists
    result_list = list1 + list2
    return result_list

result = concatenate_lists(list1, list2)
print(result)


# In[29]:


#7 Python program that finds and prints the last index of a given integer value in a list

my_list = [74, 85, 102, 99, 101, 85, 56]
search_value = 85

def last_index_of_value(lst, value):
    # Check if the value is in the list
    if value in lst:
        # Find the last index of the value
        last_index = len(lst) - 1 - lst[::-1].index(value)
        return last_index
    else:
        return -1


result = last_index_of_value(my_list, search_value)
print(result)


# In[30]:


#8 Python program that calculates and prints the range of values in a list of integers:
my_list = [36, 12, 25, 19, 46, 31, 22]

def calculate_range(lst):
    # Calculate the range
    value_range = max(lst) - min(lst) + 1
    return value_range


result = calculate_range(my_list)
print(result)


# In[31]:


#8 Python program that calculates and prints the range of values in a list of integers:
my_list = [13,98,34,16,7,36,44,20,15]

def calculate_range(lst):
    # Calculate the range
    value_range = max(lst) - min(lst) + 1
    return value_range


result = calculate_range(my_list)
print(result)


# In[32]:


#9 Python program that counts how many elements in a list fall between a given minimum and maximum value (inclusive):

my_list = [14, 1, 22, 17, 36, 7, -43, 5]
min_value = 4
max_value = 17

def count_elements_between(lst, min_value, max_value):
    # Count elements between the minimum and maximum values (inclusive)
    count = sum(min_value <= element <= max_value for element in lst)
    return count



result = count_elements_between(my_list, min_value, max_value)
print(result)


# In[33]:


my_list = [-5,10,8,3,15,22,7,0]
min_value = 5
max_value = 10

def count_elements_between(lst, min_value, max_value):
    # Count elements between the minimum and maximum values (inclusive)
    count = sum(min_value <= element <= max_value for element in lst)
    return count



result = count_elements_between(my_list, min_value, max_value)
print(result)


# In[34]:


my_list = [0,1,2,3,4,5,6,7,8,9,]
min_value = 2
max_value = 8

def count_elements_between(lst, min_value, max_value):
    # Count elements between the minimum and maximum values (inclusive)
    count = sum(min_value <= element <= max_value for element in lst)
    return count



result = count_elements_between(my_list, min_value, max_value)
print(result)


# In[35]:


my_list = [90,75,-600,78,10,34,1000,360,128,792,1500,-30]
min_value = 20
max_value = 1000

def count_elements_between(lst, min_value, max_value):
    # Count elements between the minimum and maximum values (inclusive)
    count = sum(min_value <= element <= max_value for element in lst)
    return count



result = count_elements_between(my_list, min_value, max_value)
print(result)


# In[36]:


#10 Python program that checks if a list of real numbers is in non-decreasing order:

list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

def is_sorted(lst):
    # Check if the list is in sorted (non-decreasing) order
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

result1 = is_sorted(list1)
result2 = is_sorted(list2)

print(result1)  
print(result2)  


# In[37]:


list1 = [10,20,30,40,50,60,70,80]
list2 = [90,50,70,40,10]

def is_sorted(lst):
    # Check if the list is in sorted (non-decreasing) order
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

result1 = is_sorted(list1)
result2 = is_sorted(list2)

print(result1)  
print(result2) 


# # Exercises 4 1

# # 1 Write a program to produce the following output using for loop
# +----+
# \    /
# \    /
# \    /
# \    /
# \    /
# \    /
# +----+
# 

# In[38]:


arithmeticF = ["+----+","\    /", "/    \\", "\    /", "/    \\", "\    /", "/    \\", "+----+"]
for x in arithmeticF:
    print(x)


# # 2 Write a program to produce the following output using for loop
# **********
# **********
# **********
# **********
# **********
# 

# In[39]:


london = ["**********", "**********", "**********", "**********","**********"]
for i in london:
    print(i)


# # 3 complete the code for the following for loop

# In[40]:


# A
for i in range (1,7):
    print(i)


# In[41]:


#B
for i in range (1,7):
    result = i * 2
    print(result)


# In[42]:


#C
for i in range (1,7):
    result = i * 15 - 11
    print(result)


# In[43]:


#D
for i in range (3, -4, -1):
    result = i * 10
    print(result)


# In[44]:


#E
for i in range (-7, 14, 4):

    print(i)


# In[45]:


#f
for i in range (97, 79, -3):

    print(i)


# In[46]:


#G
for i in range (-4, 104, 18):

    print(i)


# # 4

# In[47]:


#Python program using a for loop to produce the specified output:

class Figure:
    # Class constant to change the number of lines
    NUM_LINES = 7

    def print_figure(self):
        for i in range(1, self.NUM_LINES + 1):
            line = str(i) * i
            print(line.ljust(self.NUM_LINES, ' '))

# Create an instance of the Figure class
figure_instance = Figure()

# Call the method to print the figure
figure_instance.print_figure()


# # 5

# In[48]:


def pay(salary_per_hour, hours_worked):
    normal_hours = min(8, hours_worked)
    overtime_hours = max(0, hours_worked - 8)

    normal_pay = salary_per_hour * normal_hours
    overtime_pay = (1.5 * salary_per_hour) * overtime_hours

    total_pay = normal_pay + overtime_pay
    return total_pay


result1 = pay(5.50, 6)
result2 = pay(4.00, 11)

print(result1)
print(result2)


# # 6

# In[49]:


#Python method named area that calculates the area of a circle given its radius:
def to_days(millis):
    return millis / 1000.0 / 60.0 / 60.0 / 24.0


milliseconds = 86400000  
days_result = to_days(milliseconds)

print(f"{milliseconds} milliseconds is equal to {days_result} days.")


# In[50]:


import math
def area(radius):
    return math.pi * radius ** 2
result = area(2.0)
print(result)


# # 7

# In[ ]:


# modified code that prompts the user for the values of low and high:
low = int(input("low? "))
high = int(input("high? "))
sum = 0
for i in range (low, high):
    sum += i
print("sum =", sum)


# In[ ]:


low = int(input("low? "))
high = int(input("high? "))
sum = 0
for i in range (low, high):
    sum += i
print("sum =", sum)


# # 8 write a program using while loop that prompts the user for numbers until the user types 0, then outputs their sum.

# In[ ]:


sum = 0
while True:
    user_input = int(input("Enter a number(type 0 to finish): "))
    if user_input == 0:
        break
        sum += user_input
    print("sum of entered numbers:", sum)


# In[ ]:


sum = 0
while True:
    user_input = int(input("Enter a number(type 0 to finish): "))
    if user_input == 0:
        break
        sum += user_input
    print("sum of entered numbers:", sum)


# # 9

# In[ ]:


sum = 0
while True:
    user_input = int(input("Enter a number(type -1 to finish): "))
    if user_input == -1:
        break
        sum += user_input
    print("sum of entered numbers:", sum)


# # 10 repl

# In[ ]:


def repl(input_str, repetitions):
    if repetitions <= 0:
        return ""
    else:
        return input_str * repetitions
result = repl("hello", 3)
print(result)


# # 11 printRange

# In[ ]:


def printRange(start, end):
    if start < end:
        for num in range(start, end + 1):
            print(num, end=" ")
    elif start > end:
            for num in range(start, end - 1,-1):
                print(num,end=" ")
    else:
                    print(start)
printRange(2, 7)

printRange(19, 11)

printRange(5, 5)


# In[ ]:


def printRange(start, end):
    if start < end:
        for num in range(start, end + 1):
            print(num, end=" ")
    elif start > end:
        for num in range(start, end - 1, -1):
            print(num, end=" ")
    else:
        print(start)

# Example usage:
printRange(2, 7)
printRange(19, 11)
printRange(5, 5)


# # 12 smallest to largest

# In[ ]:


def smallestLargest():
    num_count = int(input("How many numbers do you want to enter? "))
    
    if num_count > 0:
        num_list = []
        
        for i in range(1, num_count +1):
            num = float(input(f"Number{i}: "))
            num_list.append(num)
            
        smallest = min(num_list)
        largest = max(num_list)
            
        print(f"Smallest = {smallest}")
        print(f"Largest = {largest}")
            
smallestLargest()
        


# In[ ]:


def smallestLargest():
    num_count = int(input("How many numbers do you want to enter? "))
    
    if num_count > 0:
        num_list = []

        for i in range(1, num_count + 1):
            num = float(input(f"Number {i}: "))
            num_list.append(num)

        smallest = min(num_list)
        largest = max(num_list)

        print(f"Smallest = {smallest}")


smallestLargest()


# # 13 smallestLargest

# In[ ]:


def printAverage():
    total = 0
    count = 0

    while True:
        num = float(input("Type a number: "))
        
        if num < 0:
            if count == 0:
                print("No nonnegative numbers entered.")
            else:
                average = total / count
                print(f"Average was {average:.1f}")
            break

        total += num
        count += 1


printAverage()


# In[ ]:


def printAverage():
    total = 0
    count = 0

    while True:
        num = float(input("Type a number: "))
        
        if num < 0:
            if count == 0:
                print("No nonnegative numbers entered.")
            else:
                average = total / count
                print(f"Average was {average:.1f}")
            break

        total += num
        count += 1


printAverage()


# # 14 numUnique

# In[ ]:


def numUnique(num1, num2, num3):
    unique_numbers = set([num1, num2, num3])
    return len(unique_numbers)

# Example usage:
result1 = numUnique(18, 3, 4)
result2 = numUnique(6, 7, 6)

print(result1)
print(result2)


# In[ ]:


def numUnique(num1, num2, num3):
    unique_numbers = set([num1, num2, num3])
    return len(unique_numbers)

# Example usage:
result1 = numUnique(78, 19, 22)
result2 = numUnique(6, 6, 6)

print(result1)
print(result2)


# In[ ]:


15


# In[ ]:


import random
count = 0
def roll_dice():
    return random.randint(1,6)

def main():
    target_sum = 7
    tries = 0
    
    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        
        total = dice1 + dice2
        count += 1
        
        print(f"{dice1} + {dice2} = {total}")
        
        if total == target_sum:
            break
print(f"you won after {count} tries")

            


# In[ ]:


import random
count = 0
def roll_dice():
    return random.randint(1,6)

def main():
    target_sum = 7
    tries = 0
    
    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        
        total = dice1 + dice2
        count += 1
        
        print(f"{dice1} + {dice2} = {total}")
        
        if total == 7:
            break
print(f"you won after {count} tries")


# In[ ]:


import random
count=0
while True:
    dieA=random.randint(1,6)
    dieB=random.randint(1,6)
    alg=dieA+dieB
    count +=1
    print(f"{dieA} + {dieB} = {alg}")
    if alg ==7:
        break
print(f"you won after {count} tries")


# In[ ]:


import random
count=0
while True:
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    alg=dice1+dice2
    count +=1
    print(f"{dice1} + {dice2} = {alg}")
    if alg ==7:
        break
print(f"you won after {count} tries")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




