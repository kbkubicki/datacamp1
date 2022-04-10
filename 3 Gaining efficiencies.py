import pandas as pd
from numpy import NAN

# dict = {'names': names, 'primary_types': names1, 'secondary_types': names2}
# df_save = pd.DataFrame(dict)
# df_save.to_csv('data/pokemon.csv')

df_read = pd.read_csv('data/pokemon.csv', index_col=0)
names = list(df_read['names'])
primary_types = list(df_read['primary_types'])
secondary_types = list(df_read['secondary_types'])
generations = list(df_read['generations'])

# Combine the names list and the primary_types list into a new list object.
names_type1 = [*zip(names, primary_types)]
print(*names_type1[:5], sep='\n')  # * aktywuje sep=
# Combine names, primary_types, and secondary_types (in that order) using zip()
# and unpack the zip object into a new list.
names_types = [*zip(names, primary_types, secondary_types)]
print(*names_types[:5], sep='\n')
# Use zip() to combine the first five items from the names list and the first three items from the primary_types list.
differing_lengths = [*zip(names[0:5], primary_types[0:3])]
print(*differing_lengths, sep='\n')  # if you provide zip() with objects of differing lengths,
# it will only combine until the smallest lengthed object is exhausted?

# Collect the count of each primary type from the sample.
from collections import Counter
# Collect the count of each primary type from the sample.
type_count = Counter(primary_types)
print(type_count, '\n')
# Collect the count of each generation from the sample.
gen_count = Counter(generations)
print(gen_count, '\n')
# Use list comprehension to collect the first letter of each Pokémon in the names list. Save this as starting_letters.
starting_letters = [name[0] for name in names]
# Collect the count of starting letters from the starting_letters list. Save this as starting_letters_count.
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

# Import combinations from itertools
pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']
from itertools import combinations
# Create a combinations object called combos_obj that contains all possible pairs of Pokémon
# from the pokemon list. A pair has 2 Pokémon.
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')
# Unpack combos_obj into a list called combos_2.
combos_2 = [*combos_obj]
print(combos_2, '\n')
# Ash upgraded his Pokédex so that it can now store four Pokémon. Use combinations to collect
# all possible combinations of 4 different Pokémon. Save these combinations directly into a list
# called combos_4 using the star character (*).
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)

ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck',
              'Squirtle']
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck',
                'Squirtle']
brock_pokedex = ['Geodude', 'Machop', 'Zubat', 'Kabutops', 'Onix', 'Omastar', 'Tauros', 'Vulpix', 'Dugtrio', 'Golem']
# Convert both lists (ash_pokedex and misty_pokedex) to sets called ash_set and misty_set respectively.
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)
# Find the Pokémon that both Ash and Misty have in common using a set method.
both = ash_set.intersection(misty_set)
print(both)
# Find the Pokémon that are within Ash's Pokédex but are not within Misty's Pokédex with a set method.
ash_only = ash_set.difference(misty_set)
print(ash_only)
# Use a set method to find the Pokémon that are unique to either Ash or Misty (i.e., the Pokémon
# that exist in exactly one of the Pokédexes but not both).
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

# Convert Brock's Pokédex list (brock_pokedex) to a set.
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)
# Check if 'Psyduck' is in Ash's Pokédex list (ash_pokedex) and if 'Psyduck' is in Brock's Pokédex set (brock_pokedex_set).
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)
# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

names = list(df_read['names1'])
# Use the provided function to collect unique Pokémon names
def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))
# Use a set data type to collect the unique Pokémon in the names list. Save this as uniq_names_set.
uniq_names_set = set(names)
print(len(uniq_names_set))
# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))
# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')

# Using a set data type to collect unique values is much faster than using a for loop
# (like in the find_unique_items() function). Since a set is defined as a collection of distinct
# elements, it is an efficient way to collect unique items from an existing object.

poke_gens = generations
poke_names = names

gen1_gen2_name_lengths_loop = []

for name, gen in zip(poke_names, poke_gens):
    if gen < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_lengths_loop.append(poke_tuple)
# Eliminate the above for loop using list comprehension and the map() function:
# Use list comprehension to collect each Pokémon that belongs to generation 1 or generation 2.
gen1_gen2_pokemon = [name for name, gen in zip(poke_names, poke_gens) if gen < 3]
print(gen1_gen2_pokemon)
# Use the map() function to collect the number of letters in each Pokémon's name
# within the gen1_gen2_pokemon list. Save this map object as name_lengths_map.
name_lengths_map = map(len, gen1_gen2_pokemon)
print(name_lengths_map)  # <map object at 0x018C57D0>
# Combine gen1_gen2_pokemon and name_length_map into a list called gen1_gen2_name_lengths.
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]
print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

# If you're an experienced Pythonista, you may have noticed
# that you could replace the entire for loop with one list comprehension:
# [(name, len(name)) for name,gen in zip(poke_names, poke_gens) if gen < 3]

import numpy as np

names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl']
stats = np.array([[90, 92, 75, 92, 85, 60],
               [45, 92, 75, 48, 48, 60],
               [90, 45, 75, 92, 85, 60],
               [30, 16, 75, 12, 85, 21],
               [90, 92, 75, 92, 19, 60]])

poke_list = []
for pokemon,row in zip(names, stats):
    total_stats = np.sum(row)
    avg_stats = np.mean(row)
    poke_list.append((pokemon, total_stats, avg_stats))

# Replace the above for loop using NumPy:
# Create a total stats array (total_stats_np) using the .sum() method and specifying the correct axis.
total_stats_np = stats.sum(axis=1)
# Create an average stats array (avg_stats_np) using the .mean() method and specifying the correct axis.
avg_stats_np = stats.mean(axis=1)
# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]
print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

# You used NumPy's .sum() and .mean() methods with a specific axis to eliminate a for loop.

# Import Counter
from collections import Counter
# Use Counter() to collect the count of each generation from the generations list. Save this as gen_counts.
gen_counts = Counter(generations)
# Improve for loop by moving one calculation above the loop
total_count = len(generations)
for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))

pokemon_types = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost',
                 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
from itertools import combinations
# Collect all possible_pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]
# Create an empty list called enumerated_tuples
enumerated_tuples = []
# Within the for loop, append each enumerated_pair_tuple to the empty list you created in the above step.
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)
# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

# Rather than converting each tuple to a list within the loop, you used the map() function
# to convert tuples to lists all at once outside of a loop.

import pandas as pd
df = pd.read_csv('data/pokemon_zscores.csv')
names = df['names']
hps = df['hps']

poke_zscores = []
for name, hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
highest_hp_pokemon = []
for name,hp,zscore in poke_zscores:
    if zscore > 2:
        highest_hp_pokemon.append((name, hp, zscore))
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()
# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std
# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')
# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name, hp, zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')