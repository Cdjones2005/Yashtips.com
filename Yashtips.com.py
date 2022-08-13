import discord
import requests
import json
import asyncio

client = discord.Client()

def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("https://pacific-ridge-92120.herokuapp.com/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"

    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"
        if item['is_correct']:
            answer = id
        id += 1
    return(qs, answer)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    study = ['study', 'Study']

    msg = message.content

    if message.content.startswith('$question'):
        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()
        try:
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('too late')
        if int(guess.content) == answer:
            await message.channel.send("That's right")
        else:
            await message.channel.send('Wrong')

client.run('ODQyNTMzNDA3OTMwMzE4OTA5.YJ2sYQ.WmGSQlL-hB1Iz4BpmqwlJge77Tk')
