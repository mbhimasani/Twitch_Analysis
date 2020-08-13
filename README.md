# Twitch Gaming Trends
### Team: Meghana Bhimasani, Matthew Cole, Romy Robillard, Lucas Santos, Andres Gomez

Twich is a live streaming video platform that is a subsidiary of Amazon. It was founded in 2006, and officially launched in 2011. It's now the No. 1 website traffic rank in gaming category with 862.28 Million total visits and the average visit duration of 6 minutes and 21 seconds.

This project analyzes the Twitch API to distinguish trends in modern gaming platforms with the aim of gaining insights in revenue and business model improvements. The overarching questions that we want to answer are:
1) How can companies capitalize on the fact that Twitch has created a new phenomenon where people are not only playing their games but are also watching others play their games? ie as a game developer in 2019, how can Twitch help your business and increase exposure? 
2) If you are a broadcaster or content creator, how can you use Twitch to grow your personal brand? 

In our mission to create an accurate story to at least attempt to answer these questions, we used as much data from the Twitch API as was available to us. In doing so, we realized historical data would be of great importance in order to accurately depict trends. Therefore, we decided to do write a script that would run once an hour for as long as possible (which ended up being around a week). The hourly requests were made to 2 real-time endpoints: Get Top Games and Streams Data, which was dependent on the previous request. Specifically, we tracked the top 25 games and the top 10 streamers per game. The JSON formatted data that was returned to us provided us with useful information such as current viewers, etc. 

### Conclusions: 
<img src="/Charts/Average Viewers per Game PieChart.png"/>
<img src="/Charts/AverageStreamersperGameCategory.png"/>

Looking at the data during the week for the average viewers and streamers for the top 10 games, Fornite has a big chunk of the audience but also a huge surplus of streamers for the hours
As a game developer or new streamer, it would be interesting to see what platform has a large audience but amount of streamers to find not only demand for that game or category, but also where competition for viewership is less intimidating. Another interesting insight from the data was that the Sports & Fitness category only had 0.1% of streamers but pulled in ~11% of viewership. 


<img src="/Charts/avgViewersTable.png"/>
What this table is showing is that the number of cumulative average viewers that they have during the 7 day time. Developers & companies who have their own channels are doing well and are matching the streamers. If you are trying to get in the industry, an observation is that you could try to create your own channel on Twitch to gain exposure. Some of the top games being watched on Twitch have official channels that do as well or even better than the top individual streamers for that game. Great for audience interaction and marketing game for little cost.


<img src="/Charts/changesInTotViewersforTop5Cat.png"/>
Here is a figure showing the changes in total viewers for the top 5 viewed categories over the week.
Interesting tidbits - When Ninja starts his stream, viewership in Fortnite peaks. League of Legends WC shows highest peak in views for LoL 
Trends - Viewership in US games tends to peak at the same time, indicating the optimal time for a new developer to time starting their stream or for when a new streamer to have the best possibility to attract the largest audience.


<img src="/Charts/changesInTotViewersforIRLCat.png"/>
Here is a graph of changes in viewers for just streams with in the In-real-Life or IRL categories. These include channels like just chatting, Arts & Performance, and Art. This would be great to show to potential content creators that there is a huge audience for entertainment other than video games on Twitch. It also shows the flexibility of Twitch in that it can accommodate a wide array of entertainment options.


<img src="/Charts/changesInTotChforTop5Cat.png"/>
We were also interested in seeing how the number of channels for the top 5 most viewed games changed over the week. We saw a huge amount of change for fortnite channels, while the other top 4 remain rather constant. This again shows the large amount of competition for fortnite viewership, where the amount of streamers to viewers is large compared to other games. If you’re are trying to get into a popular game such as fortnite, this chart would be crucial to show you when to begin streaming, or when the number of channels is relatively low.


<img src="/Charts/SvV per Game_Grouped.png"/>
We also felt it was important to look at the streamers to viewers ratio per game. Looking at all the games and channels, there are clearly a few games that stand out. Fortnite, League of Legends, and Sports and Fitness are consistently at the top and have relatively even ratio of streamers to viewers. Comparatively, a majority of games are clumped together and have a smaller ratio, with less than 2000 streamers to 60000 viewers. But how is this useful? Well for a new twitch streamer, this could help them decide which game they want to stream for. Games that have a high streamer count, such as Fortnite, League, and World of Warcraft,  could provide a supportive community feel for an up and coming streamer, where they can look at other streamers to determine how best to format their channel and the best or most interesting content. Of course, a drawback to streaming for these games would be that they would also be competing with a large number of streamers to gain viewers. So games that have a higher viewer count to streamers, such as Dota 2, ShellShock Live, and BombTag, could provide new streamers with less competition, and the opportunity to carve out a niche and a space for themselves. BombTag for example currently has only 2 viewers, while its total average viewer count is around 30000. So if a third streamer came in and started streaming some interesting or different, there could potentially be a higher chance for this third streamer to gain a large amount of viewers. 

Fortnite, PLAYERUNKNOWN'S BATTLEGROUNDS, screencheat  - Shooter
Call of Duty, gary’s mod - first person shooter
League, Dota2  - MOBA (mass online battle arena)
Sports and Fitness, Just Chatting - Other
World of Warcraft - MMORPG (Massively multiplayer online role-playing games)
Shellshock live, BombTag - action
Hearthstone - card game
Rocket league - racing


<img src="/Charts/top25GamesbyViews.png"/>
Genres of the games are equally important. Clearly, first person shooters are the most popular type of game watched on Twitch. But it’s interesting to note that Other comes in a close second. The other category comprises of anything that does not fit into a game category. Sports and Fitness and Just Chatting are two examples that have a large amount of viewers. So as a new twitch streamer, this could help them determine which genre would provide a greater chance of obtaining viewers. As a game developer, this data could help determine what genre of game they should focus on. They could then develop games that have a high probability of becoming popular, and could cater to a certain audience. They could also steer into taking advantage of this Other category. Just as an example, With sports and Fitness, where viewers watch streamers work out, game developers could create an interactive module that creates these workouts into games. So theres a lot that can be done here by focusing on genres.


### Limitations
If we had historical data, financial data, or demographics, we would have been able extend and broaden our analysis in a way that would perhaps be even more beneficial to game developers and streamers. However, despite our limitations, we were still able to extract useful in depth analysis about streamers, the audience, and the games. Individual streamers, as well, can determine what game to stream for, what type of content to create, and when to stream. Game developers can still use our analysis to determine which games to create, what genre and audience to market to and which streamers they could potentially partner with to increase their viewer base. Just as importantly, our data highlights the importance and popularity of Twitch. Twitch is clearly more than just a video gaming streaming platform, and has expanding to include a supportive community with chatting, non gaming content, and opportunities for game developers to directly interact with its audience and cater to its market. So with Twitch there’s a lot of opportunities for growth and room to change the way we interact with each other and with developers online. 

