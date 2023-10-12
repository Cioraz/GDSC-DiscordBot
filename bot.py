import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = "MTE2MTY1NzAzMDk2NTIwMzA1NA.GdUq_B.mpr9BTnd3982W1TU9s4Qqgj0qk0ZlnNX5EkUYM"
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
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
