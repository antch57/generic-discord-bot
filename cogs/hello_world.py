from discord.ext import commands

# Cog to hold everything Minecraft Server related.
class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
      await ctx.send("Hi, I'm McLovin!")

    @commands.command()
    async def hello(self, ctx):
      await ctx.send("Whaddup, I'm McLovin!")

    @commands.command()
    async def boo(self, ctx):
      await ctx.send("Boo, I should have wore the vest.")

async def setup(bot):
    await bot.add_cog(HelloWorld(bot))
