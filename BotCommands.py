import discord
import asyncio
from discord.ext import commands
import datetime
import random
from random import randint


client = discord.Client()
client = commands.Bot(command_prefix=".")
client.remove_command('help')

#gif = [d,d,d,d,d,d,d,d,d,d,d]
    #p = random.choice(gif)
    #await ctx.send('Levaste uma chapada ')
    #await ctx.send(p)



@client.event
async def on_ready():
    print('Adivinhem quem tá on!')

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )
    
    embed.set_author(name = 'Help')
    embed.add_field(name = '.hello', value = 'Repete tudo o que dizes.', inline = False)
    embed.add_field(name ='.time', value = 'Diz te as horas', inline = False)
    embed.add_field(name ='.number', value = 'Dá-te um número randomizado de 0 ao número que escolheste', inline = False)
    embed.add_field(name ='.chose', value = 'Escolhe-te uma palavra de uma lista dada', inline = False)
    embed.add_field(name ='.chapada', value = 'Dá uma chapada ao membro indicado', inline = False)
    embed.add_field(name ='.ppt', value = 'Joga ao Pedra, Papel, Tesoura contigo já que não tens amigos', inline = False)

    await ctx.send(author, embed=embed)


@client.command()
async def hello(ctx, *args):
    for arg in args:    
        await ctx.send(arg)


@client.command()
async def time(ctx):
    now = datetime.datetime.now()
    time = now.strftime('%H:%M')
    #channel = discord.utils.get(ctx.channel)
    await ctx.send(time)


@client.command(pass_context = True)
async def number(ctx, arg1):
    n = random.randint(1,int(arg1))
    await ctx.send(n)


@client.command(pass_context = True)
async def chose(ctx, *args):
    await ctx.send(random.choice(args))


@client.command(pass_context = True)
async def chapada(ctx, arg1) :
    await ctx.send('Levaste uma chapada e por causa disso considera-te um merdas %s!'%(arg1))

@client.command(pass_context = True)
async def ppt(ctx, arg1):
    t = ["Pedra", "Papel", "Tesoura"]
    computer = t[randint(0,2)]
    if arg1 == computer:
        await ctx.send('Empate! O Bot escolheu %s e tu também.'%(computer))
    elif arg1 == "Pedra":
        if computer == "Papel":
            await ctx.send('Perdeste! O Bot escolheu %s e tu %s!'%(computer,arg1))
        else :
            await ctx.send('Ganhaste! O Bot escolheu %s e tu %s!'%(computer,arg1))
    elif arg1 == "Papel":
        if computer == "Tesoura":
            await ctx.send('Perdeste! O Bot escolheu %s e tu %s!'%(computer,arg1))
        else :
            await ctx.send('Ganhaste! O Bot escolheu %s e tu %s!'%(computer,arg1))
    elif arg1 == "Tesoura":
        if computer == "Pedra":
            await ctx.send('Perdeste! O Bot escolheu %s e tu %s!'%(computer,arg1))
        else :
            await ctx.send('Ganhaste! O Bot escolheu %s e tu %s!'%(computer,arg1))
    else :
        await ctx.send('A tua escolha não é válida, tenta pôr a inicial da tua escolha em maiúscula.')

@client.event
async def abs_reminder():
    while(True) :
        await client.wait_until_ready()
        online_members = []
        for member in client.get_all_members():
            if member.status != discord.Status.offline and member.id != client.user.id:
                online_members.append(member.id)
            elif member.id == client.user:
                return      
        if len (online_members) > 0:
            p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
            abdominais = p[randint(0,24)]
            user = random.choice(online_members)
            now = datetime.datetime.now()
            time = now.strftime('%H:%M')
            channel = discord.utils.get(client.guilds[0].channels, name="general")
            message = f"Já que são {time} o que achas de uns {abdominais} abdominais? Assim mesmo como quem não quer a coisa <@{user}> !"
        
            await channel.send(message)
        await asyncio.sleep(4200)

client.loop.create_task(abs_reminder())

@client.event
async def pushup_reminder():
    while(True) :
        await client.wait_until_ready()
        online_members = []
        for member in client.get_all_members():
            if member.status != discord.Status.offline and member.id != client.user.id:
                online_members.append(member.id)
            elif member.id == client.user:
                return     
        if len (online_members) > 0: 
            t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
            flexoes = t[randint(0,24)]
            user = random.choice(online_members)
            channel = discord.utils.get(client.guilds[0].channels, name="general")
            now = datetime.datetime.now()
            time = now.strftime('%H:%M')
            message = f" São {time} Não achas uma bela hora para ires fazer {flexoes} flexões memo à bacano <@{user}> !"  
            await channel.send(message)
        await asyncio.sleep(3600)
        
client.loop.create_task(pushup_reminder())


#@client.event
#async def on_message(message):
    #if message.author == client.user:
        #return
    #user = message.author    
    #keywords = ['burros', 'Ric', 'olá', 'Tiagovski', 'vai', 'sombra', 'simple', 'bot', 'andre', 'mendes', 'merda', 'caralho', "fds"]
    #channel = message.channel
    #for keyword in keywords: 
        #if keyword.lower() in message.content.lower():
          #response = f'Quem é que disse {keyword.lower()}!? Só por causa dessa vai comer bolachas maria {user}!' 
    #await channel.send(response)



client.run(TOKEN)
        