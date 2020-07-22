import discord
import asyncio
import os
import random 
import datetime

bot = discord.Client()


@bot.event
async def on_member_join(member):
    if member.id == bot.user:
        return
    channel = discord.utils.get(bot.guilds[0].channels, name='general')
    response = f'Bem vindo ao fucking servidor! És oficialmente gay, {member.name}.'
    await channel.send(response)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    user = message.author    
    keywords = ['Gay', 'Ric', 'olá', 'Tiagovski', 'vai', 'caralho', 'merda', 'merdas', 'andre', 'mendes']
    channel = message.channel
    for keyword in keywords: 
        if keyword.lower() in message.content.lower():
          response = f'Quem é que disse {keyword.lower()}!? Só por causa vai comer bolachas maria {user}!' 
    await channel.send(response)

@bot.event
async def pushup_reminder():
    while(True) :
        await bot.wait_until_ready()
        online_members = []
        for member in bot.get_all_members():
            if member.status != discord.Status.offline and member.id != bot.user.id:
                online_members.append(member.id)
        if len (online_members) > 0:
            user = random.choice(online_members)
            #current_time =int(datetime.datetime.now().strftime("%I"))
            channel = discord.utils.get(bot.guilds[0].channels, name="general")
            message = f"Não acham uma bela hora para ires fazer umas flexões memo à bacano <@{user}> !"
            await channel.send(message)
        await asyncio.sleep(9000)

bot.loop.create_task(pushup_reminder())

token = os.getenv('NzM1Mjc5OTI2NDQ5NTM3MTA1.Xxd9Vg.eTwCgZvyK4QeZ32gmJrBpUKlCvU')
bot.run('NzM1Mjc5OTI2NDQ5NTM3MTA1.Xxd9Vg.eTwCgZvyK4QeZ32gmJrBpUKlCvU')
