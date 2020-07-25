import  discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.command()
async def hello(ctx, *args):
    for arg in args:    
        await ctx.send(arg)


client.run('NzM1Mjc5OTI2NDQ5NTM3MTA1.Xxec-w.VlqrQd3TRqeQA7qnPChmryZdZMI')
        