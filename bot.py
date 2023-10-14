# Required imports
import discord
import responses
from dotenv import load_dotenv
import os
import utils
load_dotenv()

# Main async function to send message to users query


async def send_message(message, user_message, db_GDSC):
    # To ensure error handling so program doesnt crash
    try:
        response = responses.handle_response(user_message, db_GDSC)
        # await message.author.send(response)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# Main function to run the bot


def run_bot(db_GDSC):
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # When the client is loaded
    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")

    # When the user types
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return  # prevents bot from responding to itself

        # Getting the required elements
        client_username = str(message.author)
        user_message = str(message.content)
        words = user_message.split(' ')
        if (words[0][0] == '?' and len(words[0]) > 1):
            if (utils.isDiscordUsernameOnDatabase(db_GDSC, client_username)):
                if len(words) >= 2:
                    if (utils.isHead(db_GDSC, client_username)):

                        # Format - ?add_sig sigName HeadName
                        if words[0] == "?add_sig":
                            sig_name = words[1]
                            sig_head = words[2]
                            utils.addSIG(db_GDSC, sig_name, sig_head)
                            await message.channel.send("SIG added successfully!")

                        # Format - ?add_user role username email github sig year branch phone discord_username head
                        elif words[0] == "?add_user":
                            role = words[1]
                            username = words[2]
                            email = words[3]
                            github = words[4]
                            sig = words[5]
                            year = words[6]
                            branch = words[7]
                            phone = words[8]
                            discord_username = words[9]
                            head = words[10]
                            utils.addUser(db_GDSC, role, username, email, github,
                                          sig, year, branch, phone, discord_username, head)
                            await message.channel.send("User added successfully!")

                    else:
                        await message.channel.send("You are not a head! Not authorised for such commands!")

                else:
                    # if head he is executive by default
                    if (utils.isExecutive(db_GDSC, client_username)):
                        if (user_message == "?adminHelp"):
                            if (user_message == "?adminHelp"):
                                await message.channel.send("```?add_sig sigName HeadName\n?add_user role username email github sig year branch phone discord_username\n?add_event Date Event_Name Venue Time About {Tehnical/Non-Technical(True/False)}```")
                        # Format - ?add_event Date Event_Name Venue Time About {Tehnical/Non-Technical(True/False)}
                        if (user_message == '?add_event'):
                            if (utils.isExecutive(db_GDSC, client_username)):
                                date = words[1]
                                event_Name = words[2]
                                venue = words[3]
                                time = words[4]
                                about = words[5]
                                tech_or_tech = words[6]
                                utils.addEvent(db_GDSC, date, event_Name,
                                               venue, time, about, tech_or_tech)
                                await message.channel.send("Event added successfully!")
                    else:
                        # for NEP
                        await message.channel.send("You are not authorised to use admin commands!")

            else:
                await message.channel.send("Get good to be a part of WEC you noob!")
        else:
            # irrespective of whether he is NEP member of random member
            await send_message(message, user_message, db_GDSC)

    client.run(BOT_TOKEN)
