import discord
import responses
from dotenv import load_dotenv
import os
import utils
load_dotenv()


async def send_message(message, user_message, db_GDSC):
    try:
        response = responses.handle_response(user_message, db_GDSC)
        await message.author.send(response)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_bot(db_GDSC):
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return  # prevents bot from responding to itself
        discord_username = str(message.author)
        user_message = str(message.content)

        # ?add_sig sigName HeadName
        words = user_message.split(' ')
        if len(words) > 2:
            if words[0] == "?add_sig":
                if (utils.isHead(db_GDSC, discord_username)):
                    sig_name = words[1]
                    sig_head = words[2]
                    utils.addSIG(db_GDSC, sig_name, sig_head)
                    await message.channel.send("SIG added successfully!")
                else:
                    await message.channel.send("You do not have the permissions!")
            if words[0] == "?add_user":
                if (utils.isHead(db_GDSC, discord_username)):
                    discord_username = words[1]
                    name = words[2]
                    email = words[3]
                    utils.addUser(db_GDSC, discord_username, name, email)
                    await message.channel.send("User added successfully!")
                else:
                    await message.channel.send("You do not have the permissions!")
        else:
            user_message = words[0]
            await send_message(message, user_message, db_GDSC)

    client.run(BOT_TOKEN)
