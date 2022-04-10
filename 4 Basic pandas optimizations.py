import pandas as pd
import numpy as np
data = pd.read_csv('baseball_stats.csv')
columns = ['Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', 'Playoffs']
baseball_df = data[columns].copy()

#-----1. Calculating win percentage
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)
win_perc = calc_win_perc(50, 100)
# Adding win percentage to DataFrame
# 183 ms ± 1.73 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
win_perc_list = []
for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]
    wins = row['W']
    games_played = row['G']
    win_perc = calc_win_perc(wins, games_played)
    win_perc_list.append(win_perc)
baseball_df['WP'] = win_perc_list
# Iterating with .iterrows()
# 95.3 ms ± 3.57 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
win_perc_list = []
for i,row in baseball_df.iterrows():
    wins = row['W']
    games_played = row['G']
    win_perc = calc_win_perc(wins, games_played)
    win_perc_list.append(win_perc)
baseball_df['WP'] = win_perc_list
#------------------------------
## Iterating with .iterrows()
del baseball_df['WP']
pit_df = baseball_df[(baseball_df['Team'] == 'PIT') & (baseball_df['Year'] > 2007) & (baseball_df['Year'] < 2013)].copy()
pit_df = pit_df.reset_index(drop=True)
# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():  # returns tuple:  <class 'pandas.core.series.Series'>
    print(i)
    print(row)
# Instead of using i and row in the for statement to store the output of .iterrows(),
# use one variable named row_tuple.
for row_tuple in pit_df.iterrows():
    print(row_tuple)
# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))  # <class 'tuple'>
# Remember, dot-iterrows returns each DataFrame row as a tuple of (index, pandas Series) pairs,
# so we have to access the row's values with square bracket indexing.

# Nice work! Since .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs,
# you can either split this tuple and use the index and row-values separately (as you did with for i,row
# in pit_df.iterrows()), or you can keep the result of .iterrows() in the tuple form (as you did
# with for row_tuple in pit_df.iterrows()).
#
# If using i,row, you can access things from the row using square brackets (i.e., row['Team']).
# If using row_tuple, you would have to specify which element of the tuple you'd like to access before
# grabbing the team name (i.e., row_tuple[1]['Team']).
#
# With either approach, using .iterrows() will still be substantially faster than using .iloc

## Run differentials with .iterrows()
giants_df = baseball_df[(baseball_df['Team'] == 'SFG') & (baseball_df['Year'] > 2007) & (baseball_df['Year'] < 2013)].copy()
giants_df = giants_df.reset_index(drop=True)
def calc_run_diff(runs_scored, runs_allowed):
    run_diff = runs_scored - runs_allowed
    return run_diff
# Create an empty list called run_diffs that will be used to store the run differentials you will calculate.
run_diffs = []
# Write a for loop that uses .iterrows() to loop over giants_df and collects each row's runs scored and runs allowed.
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    # Add a line to the for loop that uses the provided function to calculate each row's run differential.
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    # Add a line to the loop that appends each row's run differential to the run_diffs list.
    run_diffs.append(run_diff)
giants_df['RD'] = run_diffs
print(giants_df)

#-----2. Another iterator method: .itertuples()
columns = ['Team', 'Year', 'W']
team_wins_df = data[columns].copy()
# Iterating with .itertuples()
for row_namedtuple in team_wins_df.itertuples():
    print(row_namedtuple)  # returns namedtuple: Pandas(Index=1231, Team='WSA', Year=1962, W=60)
print(row_namedtuple.Index)  # 1231
print(row_namedtuple.Team)  # WSA
# Comparing methods
# df.iterrows(): 527 ms ± 41.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# df.itertuples(): 7.48 ms ± 243 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# The reason dot-itertuples is more efficient than dot-iterrows is due to the way each method stores
# its output. Since dot-iterrows returns each row's values as a pandas Series, there is a bit more overhead.
for row_tuple in team_wins_df.iterrows():
    print(row_tuple[1]['Team'])
for row_namedtuple in team_wins_df.itertuples():
    # print(row_namedtuple['Team'])  # TypeError: tuple indices must be integers or slices, not str
    # namedtuples don't support square brackets like a pandas Series does. When looking up an attribute
    # within a namedtuple, we must use a dot to reference the attribute.
    print(row_namedtuple.Team)
#------------------------------
## Iterating with .itertuples()
# Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple.
rangers_df = baseball_df[(baseball_df['Team'] == 'TEX')].copy()
rangers_df = rangers_df.reset_index(drop=True)
# Use .itertuples() to loop over rangers_df and print each row.
for row in rangers_df.itertuples():
    print(row)  # Pandas(Index=0, Team='TEX', League='AL', Year=2012, RS=808, RA=707, W=93, G=162, Playoffs=1)
# Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.
    i = row.Index
    year = row.Year
    wins = row.W
    print(i, year, wins)  # 0 2012 93
# Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs.
    if row.Playoffs == 1:
        print(i, year, wins)

# Remember, you need to use the dot syntax for referencing an attribute in a namedtuple.
# You can create a new variable using a row's dot reference (as you did when storing row.Index as the variable i).

## Run differentials with .itertuples()
yankees_df = baseball_df[(baseball_df['Team'] == 'NYY')].copy()
yankees_df = yankees_df.reset_index(drop=True)

run_diffs = []
# Use .itertuples() to loop over yankees_df and grab each row's runs scored and runs allowed values.
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    # Now, calculate each row's run differential using calc_run_diff(). Be sure
    # to append each row's run differential to run_diffs.
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    run_diffs.append(run_diff)
# Append a new column called 'RD' to the yankees_df that contains the run differentials you calculated.
yankees_df['RD'] = run_diffs
print(yankees_df)

#-----3. pandas alternative to looping
# Run differentials with a loop
run_diffs_iterrows = []
for i,row in baseball_df.iterrows():
    run_diff = calc_run_diff(row['RS'], row['RA'])
    run_diffs_iterrows.append(run_diff)
baseball_df['RD'] = run_diffs_iterrows
print(baseball_df)
# pandas .apply() method
    # Takes a function and applies it to a DataFrame (Must specify an axis to apply ( 0 for columns; 1 for rows)
    # Can be used with anonymous functions (lambda functions)
    # Example:
    # baseball_df.apply(
    # lambda row: calc_run_diff(row['RS'], row['RA']),
    # axis=1  # iterate over rows instead of columns. Columns = 0
    # )
#------------------------------
# Analyzing baseball stats with .apply()
rays = {
    "RS": [697, 707, 802, 803, 774],
    "RA": [577, 614, 649, 754, 671],
    "W" : [90, 91, 96, 84, 97],
    'Playoffs': [0,1,1,0,1]}
index = [2012, 2011, 2010, 2009,2008]
rays_df = pd.DataFrame(rays, index=index)
print(rays_df)

def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'

# Apply sum() to each column of rays_df to collect the sum of each column. Be sure to specify the correct axis.
# Remember that sum() should not have parentheses when used as an argument in .apply().
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)
# Apply sum() to each row of rays_df, only looking at the 'RS' and 'RA' columns, and specify the correct axis.
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)
# Convert numeric playoffs to text by applying text_playoffs()
# Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df.
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

# Great work! The .apply() method let's you apply functions to all rows or columns of a DataFrame by specifying an axis.
# If you've been using pandas for some time, you may have noticed that a better way to find these
# stats would use the pandas built-in .sum() method.
# You could have used rays_df.sum(axis=0) to get columnar sums and rays_df[['RS', 'RA']].sum(axis=1) to get row sums.
# You could have also used .apply() directly on a Series (or column) of the DataFrame. For example,
# you could use rays_df['Playoffs'].apply(text_playoffs) to convert the 'Playoffs' column to text.

# Settle a debate with .apply()
dbacks_df = baseball_df[(baseball_df['Team'] == 'ARI')].copy()
dbacks_df = dbacks_df.reset_index(drop=True)
del dbacks_df['RD']

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

# Create a pandas Series called win_percs by applying the calc_win_perc() function
# to each row of the DataFrame with a lambda function.
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')
# Create a new column in dbacks_df called WP that contains the win percentages.
dbacks_df['WP'] = win_percs
# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

# Using the .apply() method with a lambda function allows you to apply a function
# to a DataFrame without the need to write a for loop.

#-----4.
# Broadcasting allows NumPy arrays to vectorize operations, so they are performed on all elements
# of an object at once. This allows us to efficiently perform calculations over entire arrays.
# Just like NumPy, pandas is designed to vectorize calculations so that they operate on entire
# atasets at once (not just on a row by row basis). Let's explore this concept with some examples.

## pandas internals
# pandas is built on NumPy -> Take advantage of NumPy array efficiencies
wins_np = baseball_df['W'].values
print(type(wins_np))  # <class 'numpy.ndarray'>
## Power of vectorization
## Broadcasting (vectorizing) is extremely efficient!
run_diffs_np = baseball_df['RS'].values - baseball_df['RA'].values  #  <class 'numpy.ndarray'>
baseball_df['RD'] = run_diffs_np  # 124 µs ± 1.47 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
print(baseball_df['RS'] - baseball_df['RA'])  # <class 'pandas.core.series.Series'>
#------------------------------
# Replacing .iloc with underlying arrays
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)
win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]
    wins = row['W']
    games_played = row['G']
    win_perc = calc_win_perc(wins, games_played)
    win_percs_list.append(win_perc)
baseball_df['WP'] = win_percs_list

# Use the W array and G array to calculate win percentages
# Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them directly into the calc_win_perc() function.
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)
# Create a new column in baseball_df called 'WP' that contains the win percentages you just calculated.
baseball_df['WP'] = win_percs_np
print(baseball_df.head())

## Bringing it all together: Predict win percentage
def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

# Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with
# the predict_win_perc() function. Save each row's predicted win percentage as win_perc_pred
# nd append each to the win_perc_preds_loop list.
win_perc_preds_loop = []
for run in baseball_df.itertuples() :
    runs_scored = run.RS
    runs_allowed = run.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)
# Apply predict_win_perc() to each row of the baseball_df DataFrame using a lambda function.
# Save the predicted win percentage as win_perc_preds_apply.
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)
# Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df
# into predict_win_perc(). Save these predictions as win_perc_preds_np.
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

# Using NumPy arrays was the fastest approach, followed by the .itertuples() approach,
# and the .apply() approach was slowest.

# Did you notice that the .itertuples() approach beat the .apply() approach? Even though both these
# implementations can be useful, you should default to using a DataFrame's underlying arrays to perform calculations.