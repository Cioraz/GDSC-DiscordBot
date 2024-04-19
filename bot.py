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
    BOT_TOKEN = os.environ['BOT_TOKEN']
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

        # Handling admin responses
        if (words[0][0] == '?'):
            if (utils.isDiscordUsernameOnDatabase(db_GDSC, client_username)):

                # if user is executive
                if (utils.isExecutive(db_GDSC, client_username)):
                    if (utils.isHead(db_GDSC, client_username)):
                        # if user is head
                        if words[0] == "?add_sig":
                            ADD_SIG_URL = os.environ.get('ADD_SIG_URL')
                            await message.author.send(ADD_SIG_URL)

                        elif words[0] == "?add_user":
                            ADD_USER_URL = os.environ.get('ADD_USER_URL')
                            await message.author.send(ADD_USER_URL)
                            await message.channel.send("Please check your DM for further instructions")
                        elif (user_message == "?adminHelp"):
                            await message.channel.send("```?add_sig (To add a new SIG)\n?add_user (To add a new member)\n?add_event (To add a new Event)```")
                        elif (user_message == '?add_event'):
                            ADD_EVENT_URL = os.environ.get('ADD_EVENT_URL')
                            await message.author.send(ADD_EVENT_URL)
                            await message.channel.send("Please check your DM for further instructions")

                    else:
                        if (user_message == "?adminHelp"):
                            await message.channel.send("```?add_sig (To add a new SIG)\n?add_user (To add a new member)\n?add_event (To add a new Event)```")
                        if (user_message == '?add_event'):
                            ADD_EVENT_URL = os.environ.get('ADD_EVENT_URL')
                            await message.author.send(ADD_EVENT_URL)
                            await message.channel.send("You are not a head! Not authorised for such commands!")

                else:
                    # for NEP
                    await message.channel.send("You must be an executive to perform these commands!")

            else:
                await message.channel.send("You are not on the WEC database! Contact the admin!")
        else:
            # irrespective of whether he is NEP member of random member
            await send_message(message, user_message, db_GDSC)

    client.run(BOT_TOKEN)
