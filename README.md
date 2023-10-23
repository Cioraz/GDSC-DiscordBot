# GDSC-DiscordBot
Task ID: WebClub Discord ChatBot

# What it contains
- A fully functional discord bot with a help command line and a adminHelp command line to give admin/normanl commands to users
- A smart bot which can distinguish between NEP members/Intruders from Executive Members
- A fully connected MongoDB local server which can validate and check for all the data
- All required commands as given by the recruitment task
- A fully functional website to allow for adding a new user, adding a new SIG and adding a new Event.
- The website plans to be hosted but due to certain bugs is currently not begin hosted.
- Similarly I plan on using Mongo Atlas but due to certain issues currently using the local mongoDB database on system.

# Stuff to update
- Add NLP recognition ( Did install embedChain but as I ran out of credits for openAPI key wasnt able to implement it in this application )
- Fix redirection upon submitting a form
- Hosting the website along with moving the local MongoDB to mongo Atlas
- Find some google form API to use instead of hosting my own full stack app to add new sig, events or users.

 
# ScreenShots

### Website

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/018714ac-fcc7-4065-b4ee-5871edee95e4)

Similary for adding new Member and adding a new Event has been implemented. The website is responsive along with error validations. This ensures that it is very user friendly to do such tasks.

### Bot functionalities (A few)

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/f8840df1-4dff-46c6-b474-4d00d8c5414c)

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/40ae3d1e-0535-404e-8d17-dbc00319e921)

![image](https://github.com/Cioraz/GDSC-DiscordBot/assets/76161837/eb48c642-54ae-4005-8e04-248c331fa098)

There are other functionalities also but all cannot be listed here. Olease checkout the below link for a demo

# Demo of the application

https://www.youtube.com/watch?v=Jc3dSOZuM08


# Setup
- git clone https://github.com/Cioraz/GDSC-DiscordBot
- cd GDSC-DiscordBot
- pip install discord.py pymongo
- cd Website/client and npm install all dependencies
- cd Website/backend and npm install all dependencies
- Make a .env like the example .env
