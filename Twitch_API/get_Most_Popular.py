
# coding: utf-8

# In[ ]:


#Top Streamers


# In[48]:


# Import dependencies and store twitch client id
import json
import requests
import pandas as pd
from pprint import pprint
import time
import datetime
import numpy as np


# In[49]:


client_id = "blhbgyqq0zbv08spxea5akx70afh3g"
client_secret = "ew7lxb4xaj2oza54nmfzvil03996er"


# In[50]:


# Initiliaze url and create empty string to store top game names
#Top Streamers URL
game_base_url = f"https://api.twitch.tv/kraken/games/top/?client_id={client_id}&limit=30"
#Top Games URL
topgames_base_url =f"https://api.twitch.tv/kraken/games/top/?client_id={client_id}&limit=30"
top_game_data = requests.get(game_base_url).json()
games = []


# In[51]:


# Create for loop and create list of top 25 games
for i in range(0,25):
    game = top_game_data['top'][i]['game']['name']
    games.append(game)


# In[52]:


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


# In[53]:


stream_df = pd.DataFrame({'Timestamp': timestamps,
                          'Game Title': game_names,
                          'Rank': ranks,
                          'Display Name': display_names,
                          'Viewers': viewers_list,
                          'Channel Followers': followers_list,
                          'Total Channel Views': total_channel_views_list})
stream_df


# In[54]:


# Save data frame to csv file with timestamp as name
time_stamp = time.strftime("%Y-%m-%d %H.%M")
file_path = f"Streamers CSV/ Stream Data {time_stamp}.csv"
stream_df.to_csv(file_path, index = False, header = True, sep = ',', encoding = 'utf-8')


# In[55]:


#Top Games


# In[56]:



timestamps = []
game_names = []
game_ranks = []
game_giantbombs = []
game_viewers = []
game_channels = []

topgames_data = requests.get(topgames_base_url).json()

for i in range(0,25):

    game_name = topgames_data['top'][i]['game']['name']
    game_names.append(game_name)
    game_ranks.append(i + 1)

    game_giantbomb = topgames_data['top'][i]['game']['giantbomb_id']
    game_giantbombs.append(game_giantbomb)

    game_tot_viewers = topgames_data['top'][i]['viewers']
    game_viewers.append(game_tot_viewers)

    game_tot_channels = topgames_data['top'][i]['channels']
    game_channels.append(game_tot_channels)

    unix_time = time.time()
    timestamp = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M')
    timestamps.append(timestamp)


# In[57]:


top_games_df = pd.DataFrame({"Timestamp": timestamps,
                                 "Game Rank": game_ranks,
                                 "Game": game_names,
                                 "Giantbomb ID": game_giantbombs,
                                 "Total Viewers": game_viewers,
                                 "Total Channels": game_channels})
top_games_df


# In[58]:


time_stamp = time.strftime("%Y-%m-%d %H.%M")
file_path = r"C:\Users\lucas\Desktop\Project-1\Games CSV/ Games Data" + str(time_stamp) + ".csv"
top_games_df.to_csv(file_path, index = False, header = True, sep = ',', encoding = 'utf-8')


# In[60]:


#get_ipython().system('git add .')
#get_ipython().system('git commit -m f"{time_stamp}"')
#get_ipython().system('git push ')
