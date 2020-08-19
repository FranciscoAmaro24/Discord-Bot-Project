import discord
import asyncio
from discord.ext import commands
import datetime
import random
from random import randint
import os
import json


client = discord.Client()
client = commands.Bot(command_prefix=".")
client.remove_command('help')
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

@client.event
async def on_ready():
    print('Adivinhem quem tá on suas putas!')
    await client.change_presence(activity=discord.Streaming(name = ".help" , url='https://www.twitch.tv/fantasma_k'))

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )
    
    embed.set_author(name = 'Help')
    embed.add_field(name = '.example', value = 'Dá te um exemplo de como usar todos os comandos.', inline = False)
    embed.add_field(name = '.hello', value = 'Repete tudo o que dizes.', inline = False)
    embed.add_field(name ='.time', value = 'Diz te as horas', inline = False)
    embed.add_field(name ='.number', value = 'Dá-te um número randomizado de 0 ao número que escolheste', inline = False)
    embed.add_field(name ='.chose', value = 'Escolhe-te uma palavra de uma lista dada', inline = False)
    embed.add_field(name ='.chapada', value = 'Dá uma chapada ao membro indicado', inline = False)
    embed.add_field(name ='.ppt', value = 'Joga ao Pedra, Papel, Tesoura contigo já que não tens amigos', inline = False)
    embed.add_field(name = '.love', value = 'Dá a probabilidade de mamares a outra pessoa', inline = False)
    embed.add_field(name = '.gay', value = 'Dá a probabilidade de seres gay', inline = False)
    await ctx.send(author, embed=embed)


@client.command(pass_context = True)
async def example(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    
    embed.set_author(name = 'Examples')
    embed.add_field(name = '.hello', value = '.hello im very happy', inline = False)
    embed.add_field(name ='.time', value = '.time', inline = False)
    embed.add_field(name ='.number', value = '.number 30', inline = False)
    embed.add_field(name ='.chose', value = '.chose Miguel João André Kiko', inline = False)
    embed.add_field(name ='.chapada', value = '.chapada @Sombra', inline = False)
    embed.add_field(name ='.ppt', value = '.ppt Pedra', inline = False)
    embed.add_field(name = '.love', value = '.love André Fifa', inline = False)
    embed.add_field(name = '.gay', value = '.gay Mendes', inline = False)
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
    user = ('@%s'%(ctx.author))
    t = ['https://giphy.com/gifs/uqSU9IEYEKAbS', 'https://giphy.com/gifs/uqSU9IEYEKAbS', 'https://gph.is/1haNrcj','http://gph.is/16Q8alO','https://gph.is/28ZsTdG','https://gph.is/2d08G50']
    
    
    await ctx.send('Levaste uma chapada do %s e por causa disso considera-te um merdas %s!'%(user,arg1))
    await ctx.send(random.choice(t))




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

@client.command(pass_context = True)
async def love(ctx, arg1, arg2):
    n = random.randint(0,100)
    n2 = '%'
    dumb = 'Bot calculated that %s and %s are %s%s connected'%(arg1,arg2,n,n2) 
    embed = discord.Embed(     
        colour = discord.Colour.red()
    )
    embed.add_field(name = 'love', value = dumb, inline = False)
    await ctx.send(embed=embed)


@client.command(pass_context = True)
async def gay(ctx, arg1):
    n = random.randint(0,100)
    n2 = '%'
    dumb = '%s is %s%s gay'%(arg1,n,n2)
    dumbidum = '%s is %s%s homossexual'%(arg1,n,n2)
    paneleiro = '%s is %s%s paneleiro'%(arg1,n,n2)
    stupid = (dumb,dumbidum,paneleiro)
    embed = discord.Embed(          
        colour = discord.Colour.purple()
    )
    embed.add_field(name = 'gay', value = random.choice(stupid), inline = False)
    embed.set_image(url='https://i.imgur.com/3B0bx2n.gif')
    accept_decline = await ctx.send(embed = embed)
    await accept_decline.add_reaction(emoji="👨‍❤️‍👨")
    await accept_decline.add_reaction(emoji="🏳️‍🌈")
    await accept_decline.add_reaction(emoji='🟥')   
    await accept_decline.add_reaction(emoji='🟧')
    await accept_decline.add_reaction(emoji='🟨')
    await accept_decline.add_reaction(emoji='🟩')
    await accept_decline.add_reaction(emoji='🟦')
    await accept_decline.add_reaction(emoji='🟪')

@client.command(pass_context = True)
async def emoji(ctx):
    await ctx.send('<:loler:735658861830340608>') 



@client.command(pass_context = True)
async def coinflip(ctx):
    p = ['Heads', 'Tails']
    computer = p[randint(0,1)]
    if computer == 'Heads':
        embed = discord.Embed(
        colour = discord.Colour.gold()
        )
        embed.add_field(name = 'Heads!', value = '------------------------------------------------------------------------------', inline = False)
        embed.set_image(url='https://media.giphy.com/media/mBjulVQHWumozyk6O2/giphy.gif')
        await ctx.send(embed = embed)
    else :
        embed = discord.Embed(
        colour = discord.Colour.greyple()
        )
        embed.add_field(name = 'Tails!', value = '-------------------------------------------------------', inline = False)
        embed.set_image(url='https://media.giphy.com/media/XyDehxKiXnRkEjrcMC/giphy.gif')
        await ctx.send(embed = embed)
        
    
os.chdir('c:/Programming/Bot')

@client.command()
async def balance(ctx):
    
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]['Wallet']    
    bank_amt = users[str(user.id)]['Bank']   
    gay = random.randrange(101)
    n2 = '%'
    mgay = '%s%s'%(gay,n2)


    embed = discord.Embed(title = f"{ctx.author.name}'s cokkie balance 🍪",
        color = discord.Colour.dark_red()
        )
    embed.add_field(name = 'Wallet balance', value = wallet_amt)
    embed.add_field(name = 'Bank balance', value = bank_amt)
    embed.add_field(name = 'Gay', value = mgay, inline=False)
    await ctx.send(embed = embed)

    
@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()
    
    earnings = random.randrange(101)

    await ctx.send(f'Someone gave you {earnings} cokkies 🍪!!')
    
    users[str(user.id)]['Wallet'] += earnings
    
    with open ('Bank.json', 'w') as f:
        json.dump(users,f)
    return True


@client.command()
async def withdraw(ctx, amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send('Please enter the amount')
        return
    
    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
        await ctx.send('You don´t have that much cokkies :(')
        return
    if amount<0:
        await ctx.send('Amount must be positive')
        return
        
    await update_bank(ctx.author, amount)
    await update_bank(ctx.author,-1*amount, 'bank')

    await ctx.send(f'You withdrew {amount} of cokkies')


@client.command()
async def deposit(ctx, amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send('Please enter the amount')
        return
    
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send('You don´t have that much cokkies :(')
        return
    if amount<0:
        await ctx.send('Amount must be positive')
        return
        
    await update_bank(ctx.author, -1*amount)
    await update_bank(ctx.author, amount,'bank')

    await ctx.send(f'You deposited {amount} of cokkies')

async def open_account(user):
    
    users = await get_bank_data()

    with open ('Bank.json', 'r') as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['Wallet'] = 0
        users[str(user.id)]['Bank'] = 0

    with open ('Bank.json', 'w') as f:
        json.dump(users,f)
    return True




async def get_bank_data():
    with open ('Bank.json', 'r') as f:
        users = json.load(f)
    return users

async def update_bank(user,change = 0, mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('Bank.json','w') as f:
        json.dump(users,f)


 



@client.command(pass_context = True)
async def emojify(ctx, *message): 
    teste = ''
    for x in str(message):
        for l in str(x):
            if l in abc:
                emoji = (':regional_indicator_' + l + ':') 
                teste = teste + str(emoji)

            elif l == '0' :
                await ctx.send(':zero:')
            elif l == '1' :
                await ctx.send(':one:')
            elif l == '2' :
                await ctx.send(':two:')
            elif l == '3' :
                await ctx.send(':three:')
            elif l == '4' :
                await ctx.send(':four:')        
            elif l == '5' :
                await ctx.send(':five:')
            elif l == '6' :
                await ctx.send(':six:')   
            elif l == '7' :
                await ctx.send(':seven:')
            elif l == '8' :
                await ctx.send(':eigth:')
            elif l == '9' :
                await ctx.send(':nine:')
            # elif l == "'":
                #return
            #elif l == '(':
                #return
            #elif l ==')':
                #return
            #elif l =='[':
                #return
            #elif l ==']':
                #return
            #elif l ==',':
                #return
        print (teste)                
        await ctx.send(teste)
        
        
        
        #else : 
            #await ctx.send('O teu texto não é válido')           
            #break
        
        
        #arg = str
        #i = 0 
        #while(i < len(arg)):
            #await ctx.send(':regional_indicator_' + args[i] + ':')
            #i +=1


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user = message.author.name  
    keywords = ['burros', 'Ric', 'olá', 'Tiagovski', 'vai', 'sombra', 'simple', 'bot', 'andre', 'mendes', 'merda', 'caralho', "fds"]
    channel = message.channel
    for keyword in keywords: 
        if keyword.lower() in message.content.lower():
          response = f'Quem é que disse {keyword.lower()}!? Só por causa dessa vai comer bolachas maria {user}!' 
    await client.process_commands(message)
    await channel.send(response)



client.run('NzM1Mjc5OTI2NDQ5NTM3MTA1.Xxd8yw.DpDordwtYbHv9cq8qQzBVwzGVSI')


#'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'