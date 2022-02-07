import discord
import random
TOKEN = 'ODg1NDE2NTAzNTU2NTc1MjM0.YTmuYA.J0BS_vxVcazxzNWRD1sO6qJwDEY'
#TOKEN = 'ODg0ODc4MzExNzg2OTUwNzA2.YTe5JQ.-bZRMA8dG5L21WAneaFp05rK8fY'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if channel == 'code':
        if user_message.lower() == '$hello':
            await user.content.send(f'Lô cc {username}!')
            print()
            return
        elif user_message.lower() == '$chui':
            await message.channel.send(f'DM {username}!')
            return
        elif user_message.lower() == '$bye':
            await message.channel.send(f'Cút {username}!')
            return
        elif user_message.lower() == '$random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return

client.run(TOKEN)
