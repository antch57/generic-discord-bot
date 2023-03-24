import asyncio
from discord_bot import Bot

print("We are going to say hi to McLovin :wave:")

mcLovin = Bot('<DISCORD APPLICATION TOKEN HERE>')
asyncio.run(mcLovin.start())
