
# coding: utf-8

# In[40]:


import requests
import json
import pandas as pd
import numpy as np
import meghana_client_ID
import time
import datetime
from pprint import pprint


# In[41]:


client_ID = meghana_client_ID.meghana
topgames_base_url =f"https://api.twitch.tv/kraken/games/top/?client_id={client_ID}&limit=30"


# In[42]:
loops = np.arange(0,240,1)
for loop in loops:
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



    # In[44]:


    top_games_df = pd.DataFrame({"Timestamp": timestamps,
                                 "Game Rank": game_ranks,
                                 "Game": game_names,
                                 "Giantbomb ID": game_giantbombs,
                                 "Total Viewers": game_viewers,
                                 "Total Channels": game_channels})
    top_games_df


    # In[47]:


    top_games_df.to_csv(f"game {timestamps[0]}.csv", index = False)
    #Print loop number
    print(f'On loop {loop}')
    print('----------------')
    #Sleep 3600 seconds/1 hour
    time.sleep(3600)

