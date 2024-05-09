# GDSC-DiscordBot

# Features
- A fully functional discord bot with a help command line and a adminHelp command line to give admin/normal commands to users.
- A smart bot which can distinguish between NEP members/Intruders from Executive Members by accessing the MongoDB database.
- A fully connected MongoDB local server which can validate and check for all the data.
- A fully functional website to allow for adding a new user, adding a new SIG and adding a new Event for ease of Admin.
- The website plans to be hosted but due to certain bugs is currently not begin hosted.
- Similarly I plan on using Mongo Atlas but due to certain issues currently using the local mongoDB database on system.

# Future Works
- Add NLP recognition for commands.
- Fix redirection upon submitting a form.
- Hosting the website along with moving the local MongoDB to mongo Atlas.
- Find some google form API to use instead of hosting my own full stack app to add new sig, events or users.

 
# ScreenShots

### Website

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/358e293a-bb94-40c6-96c5-652d029798fa)


Similary for adding new Member and adding a new Event has been implemented. The website is responsive along with error validations. This ensures that it is very user friendly to do such tasks.

### Bot functionalities (A few)

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/4d6aed92-a912-4348-b2e0-7ad5865233ae)

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/dae3d9d3-14cf-4968-a39d-e01709c48aed)

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/cffad58c-daf6-4c10-82da-1eb6d0644730)

There are other functionalities also but all cannot be listed here. Olease checkout the below link for a demo

# Demo of the application

https://www.youtube.com/watch?v=Jc3dSOZuM08


# Setup
- ```git clone https://github.com/Cioraz/GDSC-DiscordBot```
- ```cd GDSC-DiscordBot```
- ```pip install discord.py pymongo```
- ```cd Website/client``` and ```npm install``` all dependencies.
- ```cd Website/backend``` and ```npm install``` all dependencies.
- Make a .env like the example .env with the discord bot token from discord developer tools.
