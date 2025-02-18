PYTHON_MAIN_COGS = """import discord
from discord.ext import commands
import os
{db_imports}
{token_line}

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.default())

async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and file != "__init__.py":
            await bot.load_extension(f"cogs.{{file[:-3]}}")

@bot.event
async def on_ready():
    print(f'Logged in as {{bot.user}}')
    {db_on_ready}

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
"""

PYTHON_MAIN_NO_COGS = """import discord
from discord.ext import commands
import os
{db_imports}
{token_line}

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'Logged in as {{bot.user}}')
    {db_on_ready}

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)
"""

CONFIG_PY = """TOKEN = 'YOUR_BOT_TOKEN'
PREFIX = '!'
"""

ENV_FILE = """TOKEN=YOUR_BOT_TOKEN
PREFIX=!
"""

COG_EXAMPLE = """from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

async def setup(bot):
    await bot.add_cog(Example(bot))
"""

# Database templates
SQLITE_SETUP = """import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def setup_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, balance INTEGER)''')
    conn.commit()

setup_db()
"""

POSTGRES_SETUP = """import psycopg2
import os

conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cursor = conn.cursor()

def setup_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, balance INTEGER)''')
    conn.commit()

setup_db()
"""

MONGODB_SETUP = """from pymongo import MongoClient
import os

client = MongoClient(os.getenv('MONGO_URI'))
db = client['bot_database']

def setup_db():
    if 'users' not in db.list_collection_names():
        db.create_collection('users')

setup_db()
"""