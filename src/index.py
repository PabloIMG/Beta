import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '<', description = "Bot destinado a pruebas para Roboc")
contador = 0

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def contar(ctx, cuentaUsuario: str):

	global contador

	if int(cuentaUsuario) != (contador + 1):
		msg = f"ERROR"
		contador = 0

	else:
		contador = contador+1
		msg = f"Vamos en el {contador}!!"

	await ctx.send(msg)

bot.run('OTQ5NzgzMjI1MjQzNDIyNzMw.YiPYjw.AevcwnPLo4XFgHkdRUPTk-SEcW0')
