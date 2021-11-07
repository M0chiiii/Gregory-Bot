#mario party bot
#most points win, leaderboard thing
#person who starts the games decides when to start
#games: hangman,tick-tack-toe, would you rather, and type writer game
import discord
import os
from discord.ext import commands
from webserver import keep_alive
from random import choice
import random
import time

###############################################################################################

class color:
  white = 0xffffff

###############################################################################################

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "?", intents = intents, help_command = None)

@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "Use ?help <command> for extended information on a command.", color = color.white)
  
  em.add_field(name = "🕹Mini-games", value = "Create, Minigames, RPC")
  em.add_field(name = "📃Miscellaneous", value= "Test")

  await ctx.send(embed = em)



''' Events'''
###############################################################################################
@client.event
async def on_ready():
  game = discord.Game("🙈🙉")
  await client.change_presence(activity=game)
  print("Gregory-Bot is ready!")



''' Command Errors '''
###############################################################################################

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("This is a invalid command.")
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("This command is missing an argument.")
  if isinstance(error, commands.BadArgument):
    await ctx.send("This command has an invalid argument.")



''' Test Command '''
###############################################################################################

@help.command()
async def test(ctx):
  em = discord.Embed(title = "Test", description = "A testing command.", color = color.white)
  em.add_field(name = "**Syntax**", value = "?test")
  await ctx.send(embed = em)

@client.command()
async def test(ctx):
  await ctx.send("Test works!")



''' Minigames Command '''
###############################################################################################

@help.command()
async def minigames(ctx):
  em = discord.Embed(title = "🕹Minigames", description = "A list of all the playable minigames.", color = color.white)
  em.add_field(name = "**Syntax**", value = "?minigames")
  await ctx.send(embed = em)

@client.command()
async def minigames(ctx):
  em = discord.Embed(title = "🕹Minigames", description = "Tic-Tac-Toe\nTypeRacer 2.0\nHangman\nRock Paper Scissors", color = color.white)
  await ctx.send(embed = em)



''' Create Command '''
###############################################################################################
@help.command()
async def create(ctx):
  em = discord.Embed(title = "Create", description = "Host a minigame room.", color = color.white)
  em.add_field(name = "**Syntax**", value = "?create <Number of Players>")
  await ctx.send(embed = em)

@client.command()
async def create(ctx, pcount = 4):
  if pcount > 4:
    await ctx.send("Too many players!")
  elif pcount < 2:
    await ctx.send("Too few players!")
  else:
    em = discord.Embed(title = f"{ctx.message.author}'s Room", description = "", color = color.white)
    em.add_field(name = f"**Players**[{pcount}]", value = "_____ \n" * pcount + "React below to join!")
    msg = await ctx.send(embed = em)
    await msg.add_reaction("🎮")



''' Rock Paper Scissors '''
###############################################################################################
@help.command()
async def rpc(ctx):
  em = discord.Embed(title = "Rock Paper Scissors", description = "Play Rock Paper Scissors with a bot.", color = color.white)
  em.add_field(name = "**Syntax**", value = "?rpc")
  await ctx.send(embed = em)

@client.command()
async def rpc(ctx):
  possible_actions = ["🪨", "✂", "🧻"]
  computer_action = random.choice(possible_actions)
  em = discord.Embed(title = "Rock Paper Scissors", description = "Enter a choice - rock, paper, or scissors: ", color = color.white)
  msg = await ctx.send(embed = em)
  await msg.add_reaction("🪨")
  await msg.add_reaction("🧻")
  await msg.add_reaction("✂")
  @client.event
  async def on_reaction_add(reaction, user):
    if not user.id == 906680182696448020:
      if msg.id == reaction.message.id:
        if reaction.emoji == "🪨" or "✂" or "🧻":
          user_action = reaction.emoji
          message = reaction.message
          new_em = discord.Embed(title = "Rock Paper Scissors", description = f"You chose {user_action}!\nThe computer chose {computer_action}!", color = color.white)
          await msg.edit(embed = new_em)
          await reaction.remove(user)
          time.sleep(2)
          if user_action == computer_action:
            result = f"Both players selected {user_action}.\n\n😶 It's a tie! 😶"
          elif user_action == "🪨":
            if computer_action == "✂":
                result = "🪨 smashes ✂!\n\n👑 You win! 👑"
            else:
                result = "🧻 covers 🪨!\n\n😢 You lose. 😢"
          elif user_action == "🧻":
            if computer_action == "🪨":
                result = "🧻 covers 🪨!\n\n👑 You win! 👑"
            else:
                result = "✂ cuts 🧻!\n\n😢 You lose. 😢"
          else:
              if computer_action == "🧻":
                  result = "✂ cuts 🧻!\n\n👑 You win! 👑"
              else:
                  result = "🪨 smashes ✂!\n\n😢 You lose. 😢"
          new_em = discord.Embed(title = "Rock Paper Scissors", description = f"{result}", color = color.white)
          await msg.edit(embed = new_em)



''' Run the bot '''
###############################################################################################

keep_alive()
client.run(os.environ['TOKEN'])
