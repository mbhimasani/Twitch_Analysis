
# coding: utf-8

# Creating Stream Channel Data Frame

# In[1]:


# Import dependencies and store twitch client id
import json
import requests
import pandas as pd
from pprint import pprint
import time
import datetime
import numpy as np

client_id = "t0md9tc73ojytjz65vuf0bd1yfyd39"


# In[2]:


# Initiliaze url and create empty string to store top game names
game_base_url = f"https://api.twitch.tv/kraken/games/top/?client_id={client_id}&limit=30"
top_game_data = requests.get(game_base_url).json()
games = []


# In[3]:


# Create for loop and create list of top 25 games
for i in range(0,25):
    game = top_game_data['top'][i]['game']['name']
    games.append(game)


# In[33]:


# Use list of top game names from previous API request to search top 10 streams per game
stream_base_url = f"https://api.twitch.tv/kraken/streams/?client_id={client_id}&limit=15&game="
display_names = []
ranks = []
viewers_list = []
followers_list = []
total_channel_views_list = []
timestamps = []
game_names = []

for game in games:
    stream_url = stream_base_url + game
    top_10_stream_data = requests.get(stream_url).json()

    for j in range(0,10):

        try:
            display_name = top_10_stream_data['streams'][j]['channel']['display_name']
            display_names.append(display_name)
            rank = j + 1

            ranks.append(rank)

            game_names.append(game)

            num_viewers = top_10_stream_data['streams'][j]['viewers']
            viewers_list.append(num_viewers)

            num_followers = top_10_stream_data['streams'][j]['channel']['followers']
            followers_list.append(num_followers)

            total_channel_views = top_10_stream_data['streams'][j]['channel']['views']
            total_channel_views_list.append(total_channel_views)

            unix_time = time.time()
            timestamp = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M')
            timestamps.append(timestamp)

        except: IndexError


# In[39]:


stream_df = pd.DataFrame({'Timestamp': timestamps,
                          'Game Title': game_names,
                          'Rank': ranks,
                          'Display Name': display_names,
                          'Viewers': viewers_list,
                          'Channel Followers': followers_list,
                          'Total Channel Views': total_channel_views_list})
stream_df


# In[53]:


# Save data frame to csv file with timestamp as name
time_stamp = time.strftime("%Y-%m-%d %H.%M")
file_path= f"CSV Files/ Stream Data {time_stamp}"
stream_df.to_csv(file_path, index = False, header = True, sep = ',', encoding = 'utf-8')


# In[17]:
