# A taste of things to come
# In this exercise, you'll explore both the Non-Pythonic and Pythonic ways of looping over a list.
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Print the list created using the Non-Pythonic approach
# Collect the names in the above list that have six letters or more.
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
# Print the list created by looping over the contents of names
# A more Pythonic approach would loop over the contents of names, rather than using an index variable. Print better_list.
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
# Print the list created by using list comprehension
# The best Pythonic way of doing this is by using list comprehension. Print best_list.
best_list = [name for name in names if len(name) >= 6]

import this

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Built-in function: range()
nums = range(0,11)  # range(11), return range object
print(list(nums))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums_list = list(range(2, 11, 2))
print(even_nums_list)  # [2, 4, 6, 8, 10]

# Built-in function: enumerate()
letters = ['a', 'b', 'c', 'd' ]
indexed_letters = enumerate(letters)  # return enumerate object
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list)  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
indexed_letters2 = enumerate(letters, start=5)
print(list(indexed_letters2))

# Built-in function: map()
nums = [1.5, 2.3, 3.4, 4.6, 5.0]
rnd_nums = map(round, nums)
print(list(rnd_nums))  # [2, 2, 3, 5, 5]
# map() with lambda (lambda - anonymous function)
sqrd_nums = map(lambda x: x ** 2, nums)
print(list(sqrd_nums))

## Built-in practice: range()
# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))
# Convert nums to a list
nums_list = list(nums)
print(nums_list)
# Create a new list called nums_list2 that starts at one, ends at eleven, and increments
# by two by unpacking a range object using the star character (*).
nums_list2 = [*range(1,12,2)]
print(nums_list2)  # [1, 3, 5, 7, 9, 11]
print([range(1,12,2)])  # [range(1, 12, 2)]

## Built-in practice: enumerate()
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Instead of using for i in range(len(names)), update the for loop to use i as the index variable
# and name as the iterator variable and use enumerate().
indexed_names = []
for i,name in enumerate(names, start=5):
    index_name = (i,name)
    indexed_names.append(index_name)
print(indexed_names)  # [(5, 'Jerry'), (6, 'Kramer'), (7, 'Elaine'), (8, 'George'), (9, 'Newman')]
# Rewrite the previous for loop using enumerate() and list comprehension to create a new list, indexed_names_comp.
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)
# Create another list (indexed_names_unpack) by using the star character (*) to unpack the enumerate
# object created from using enumerate() on names. Start the index for enumerate() at one instead of zero.
indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)

## Built-in practice: map() / map(func, names)
names_uppercase = []
for name in names:
  names_uppercase.append(name.upper())
print(names_uppercase)
# Use map() and the method str.upper() to convert each name in the list names to uppercase.
# Save this to the variable names_map.
names_map  = map(str.upper, names)
print(type(names_map))  # Note that the func argument should not contain closing parentheses.
# Unpack the contents of names_map into a list called names_uppercase using the star character (*).
names_uppercase = [*names_map]
print(names_uppercase)

## Practice with NumPy arrays
# Let's practice slicing numpy arrays and using NumPy's broadcasting concept. Remember, broadcasting refers to
# a numpy array's ability to vectorize operations, so they are performed on all elements of an object at once.
import numpy as np
nums = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# Print second row of nums
print(nums[1,:])
# Print all elements of nums that are greater than six
print(nums[nums > 6])
# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)
# Replace the third column in nums with a new column that adds 1 to each item in the original column.
nums[:,2] = nums[:,2] + 1
print(nums)
# When compared to a list object, what are two advantages of using a numpy array?
# A numpy array contains homogeneous data types (which reduces memory consumption) and provides
# the ability to apply operations on all elements through broadcasting.

# Use range() to create a list of arrival times (10 through 50 incremented by 10).
# Create the list arrival_times by unpacking the range object.
arrival_times = [*range(10,60,10)]
# You realize your clock is three minutes fast. Convert the arrival_times list into a numpy array
# (called arrival_times_np) and use NumPy broadcasting to subtract three minutes from each arrival time.
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3
# Use list comprehension with enumerate() to pair each guest in the names list to their updated arrival
# time in the new_times array. You'll need to use the index variable created from using enumerate()
# on new_times to index the names list.
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]
print(guest_arrivals)