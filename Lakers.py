# %%
import pandas as pd

# %%
url = "https://www.basketball-reference.com/teams/LAL/"
tables = pd.read_html(url, header=0)
data_frame = tables[0]

# %%
data_frame
won_playoffs = data_frame['Playoffs'] == 'Won Finals'
total_wins = 0
for value in data_frame.loc[0:20, 'Playoffs']:
    if value == 'Won Finals':
        total_wins = total_wins + 1

print(total_wins)
percentage = total_wins / 76
print(percentage)


