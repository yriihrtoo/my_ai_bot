import discord, random, os
from discord.ext import commands
from bot_logic import coins, gen_pass
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def kooin(ctx, second=1):
     await ctx.send(coins(second))

@bot.command()
async def createpass(ctx):
     await ctx.send(gen_pass(8))

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def ide_sampah(ctx):
    img_name = random.choice(os.listdir('kerajinan'))
    with open(f'kerajinan/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def zoo(ctx):
    img_name = random.choice(os.listdir('animals'))
    with open(f'animals/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def sampah_organik(ctx):
    img_name = random.choice(os.listdir('organik'))
    with open(f'organik/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def sampah_anorganik(ctx):
    img_name = random.choice(os.listdir('anorganik'))
    with open(f'anorganik/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def sampah_b3(ctx):
    img_name = random.choice(os.listdir('b3'))
    with open(f'b3/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            await file.save(f'./{file.filename}')
            await ctx.send(f'file berhasil disimpan dengan nama {file.filename}')
            hasil = get_class('keras_model.h5', 'labels.txt', file.filename)

            if hasil[0] == "butterfly\n" and hasil[1] >= 0.7:
                await ctx.send('INI ADALAH KUPU-KUPU')
                await ctx.send('Hutan merupakan habitat dari kupu-kupu seperti kebun buah-buah, kebun bunga, area pertanian, dan pinggiran sungai.')
                await ctx.send('Kupu-kupu umumnya hidup dengan mengisap madu bunga (nektar/ sari kembang).')
                await ctx.send('presentase kemiripan {:,.1f}%'.format(hasil[1]*100))
            elif hasil[0] == "moth\n" and hasil[1] >= 0.7:
                await ctx.send('INI ADALAH NGENGAT')
                await ctx.send('Ngengat dapat ditemukan baik di seluruh Afrika, Asia, maupun Eropa.')
                await ctx.send('Makanan utama mereka sama dengan kupu-kupu dan burung kolibri yaitu nektar melalui belalai mereka sebesar jerami. ')
                await ctx.send('presentase kemiripan {:,.1f}%'.format(hasil[1]*100))
            else:
                await ctx.send('GAMBAR TIDAK TERDETEKSI')
            
    else:
        await ctx.send('anda lupa mengirim gambar!')

bot.run("token bot")

