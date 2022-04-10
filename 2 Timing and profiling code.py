# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)
# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)

import numpy as np
# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]  # %timeit
# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]  # %timeit
# What is the correct syntax when using %timeit and only using 5 runs with 25 loops per each run
# to analyze the runtime for converting this heroes list into a set. ?
# %timeit -r5 -n25 set(heroes)

# Correct! %timeit lets you specify the number of runs and number of loops you want to consider
# with the -r and -n flags. You can use -r5 and -n25 to specify 5 iterations each with 25 loops
# when calculating the average and standard deviation of runtime for your code.

# Using %timeit: formal name or literal syntax
# Create a list using the formal name
formal_list = list()  # %timeit
print(formal_list)
# Create a list using the literal syntax
literal_list = []  # %timeit
print(literal_list)
# Using Python's literal syntax to define a data structure can speed up your runtime. Consider using
# the literal syntaxes (like [] instead of list(), {} instead of dict(), or () instead of tuple()),
# where applicable, to gain some speed.

## Using cell magic mode (%%timeit)
wts = [441.0, 65.0, 90.0, 441.0, 122.0, 88.0, 61.0, 81.0, 104.0, 108.0, 90.0, 90.0, 72.0]
# List of each hero's weight in kilograms (called wts) is loaded into your session.
# You'd like to convert these weights into pounds.
# You could accomplish this using the below for loop:
# %%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)
# Or you could use a numpy array to accomplish this task:
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462
# remember that you can use %timeit to gather runtime for a single line of code (line magic mode)
# and %%timeit to get the runtime for multiple lines of code.

## Code profiling // in Python Console
heroes = ['Batman', 'Superman', 'Wonder Woman']
hts = np.array([188.0, 191.0, 183.0])
wts = np.array([ 95.0, 101.0, 74.0])

def convert_units(heroes, heights, weights):
    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
# %load_ext line_profiler
# %lprun -f convert_units convert_units(heroes, hts, wts)

def convert_units_broadcast(heroes, heights, weights):
    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
# %load_ext line_profiler
# %lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

## Code profiling for memory usage // in Python Console

