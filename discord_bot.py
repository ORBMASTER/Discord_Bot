import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import asyncio
import json
import youtube_dl

intents = discord.Intents.default()
intents.members = True 
queues= {}



def check_queue(ctx,id):
    if queues[id]!=[]:
        voice=ctx.guild.voice_client
        source=queues[id].pop(0)
        player=voice.play(source)


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#client=commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_message(message):
    # Check if the message content is "hi" and handle it
    if message.content == "hi":
        await message.delete()
        await message.channel.send("Don't send that again.")
    else:
        # Process commands manually if the message doesn't start with the prefix
        await client.process_commands(message)

# The rest of your bot's code...


@client.event
async def on_ready():
    print("the bot is ready")
    print("--------------------")



@client.command()
async def killwhale(ctx):
    await ctx.send("whales shall be killed")

@client.command()
async def bestplayer(ctx):
    await ctx.send("ORBMASTER")
    

@client.command()
async def hello(ctx):

    await ctx.send("i am a youtube bot")


@client.command()
async def killflash(ctx):
    await ctx.send("https://tenor.com/view/yamcha-yamcha-death-pose-yamcha-dead-yamcha-on-the-ground-yamcha-sleeping-gif-15816799")

@client.command()
async def frog(ctx):
    await ctx.send("You have turned into a frog")

@client.command()
async def babywhale(ctx):
    await ctx.send("https://tenor.com/view/whale-cute-blow-water-close-eyes-swimming-gif-16556295")



@client.command()
async def amen(ctx):
    await ctx.send("https://www.youtube.com/watch?v=LrfCSv0g8iE&list=RDLrfCSv0g8iE&start_radio=1")

@client.command()
async def deadwhale(ctx):
    await ctx.send("https://tenor.com/view/ohwhale-sploosh-hazardwhale-whalehazard-burst-gif-13702657")


@client.command()
async def joke(ctx):
    jokeurl = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
	"X-RapidAPI-Key": "955d5fc43bmsh6cd7cbb4e4b6866p188b10jsn50f59501de8d",
	"X-RapidAPI-Host": "joke3.p.rapidapi.com"
    }

    response = requests.get(jokeurl, headers=headers)

    await ctx.send(response.content)

@client.event
async def on_member_join(member):
    
    jokeurl = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
	"X-RapidAPI-Key": "955d5fc43bmsh6cd7cbb4e4b6866p188b10jsn50f59501de8d",
	"X-RapidAPI-Host": "joke3.p.rapidapi.com"
    }

    response = requests.get(jokeurl, headers=headers)

   
    channel= client.get_channel(1223345494353248320)
    await channel.send("hello")
    await channel.send(json.loads(response.json())['content'])
    #print("hello"+member)
   # await member.send("test")
    print("--------------------")

@client.event
async def on_member_remove(member):
    channel= client.get_channel(1223345494353248320)
    await channel.send("goodbye")
    #print("hello"+member)
   # await member.send("test")
    print("--------------------")

@client.command(pass_content= True)
async def join(ctx):
    if(ctx.author.voice):
        channel=ctx.message.author.voice.channel
        voice = await channel.connect()
        source=FFmpegPCMAudio('60.mp3')
        player= voice.play(source)
    else:
        await ctx.send("Youre not in the voice channel for the command to work")

@client.command(pass_content= True)
async def leave(ctx):
    if(ctx.voice_client):
        
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice chat")
    else:
        
        await ctx.send("i am not in a voice channel")


@client.command(pass_content= True)
async def pause(ctx):
    voice= discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        
        voice.pause()
    else:
        
        await ctx.send("At the moment theres no sound playing")



@client.command(pass_content= True)
async def resume(ctx):
    voice= discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_paused():
        
        voice.resume()
    else:
        
        await ctx.send("At the moment theres no song is paused")


@client.command(pass_content= True)
async def stop(ctx):
    voice= discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()

@client.command(pass_content= True)
async def play(ctx,arg):
    if 1 <= int(arg) <= 60:
        voice=ctx.guild.voice_client
        source=FFmpegPCMAudio(arg+'.mp3')
        player= voice.play(source,after=lambda x=None:check_queue(ctx,ctx.message.guild.id))
    
    else:
        await ctx.send("The variable is not between 1 and 60.")



@client.command(pass_content= True)
async def start2(ctx,arg):
    if 1 <= int(arg) <= 60:
        voice= discord.utils.get(client.voice_clients,guild=ctx.guild)
        if(ctx.voice_client):
            await ctx.send("already joined the voice channel")
            if voice.is_playing():
            
                await ctx.send("running more music")
                voice.stop()
                voice=ctx.guild.voice_client
                source=FFmpegPCMAudio(arg+'.mp3')
                player= voice.play(source)
            else:
                voice=ctx.guild.voice_client
                source=FFmpegPCMAudio(arg+'.mp3')
                player= voice.play(source)
                
            return
        else:
            await ctx.send("first time joining the voice channel")
            channel=ctx.message.author.voice.channel
            voice = await channel.connect()
            await ctx.send("running music")

            voice=ctx.guild.voice_client
            source=FFmpegPCMAudio(arg+'.mp3')
            player= voice.play(source)

           
          
              
        
        
    else:
        await ctx.send("The variable is not between 1 and 60.")


@client.command(pass_context=True)
async def start(ctx, arg):
    if 1 <= int(arg) <= 60:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.stop()
            await ctx.send("Changing song.")
            source = FFmpegPCMAudio(arg + '.mp3')
            voice.play(source)
            return
        elif voice and voice.is_connected():
            await ctx.send("New Song.")
            source = FFmpegPCMAudio(arg + '.mp3')
            voice.play(source)
            return

        channel = ctx.message.author.voice.channel
        if channel:
            voice = await channel.connect()
        else:
            await ctx.send("You're not in a voice channel for the command to work.")
            return

        source = FFmpegPCMAudio(arg + '.mp3')
        voice.play(source)
        await ctx.send("Playing music...")

    else:
        await ctx.send("The variable is not between 1 and 60.")



@client.command(pass_context=True)
async def startsongs(ctx, *args):
    songs = args
    if not songs:
        await ctx.send("No songs provided.")
        return
    
    for song in songs:
        if 1 <= int(song) <= 60:
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            if voice and voice.is_playing():
                voice.stop()
                await ctx.send("Already playing music.")
            elif voice and voice.is_connected():
                
                print("song ended")
                
            channel = ctx.message.author.voice.channel
            if channel:
                if not voice:
                    voice = await channel.connect()
                else:
                    if voice.channel != channel:
                        await voice.move_to(channel)
            else:
                await ctx.send("You're not in a voice channel for the command to work.")
                return

            source = FFmpegPCMAudio(song + '.mp3')
            voice.play(source)
            await ctx.send(f"Playing music '{song}'.")
            
            # Wait for the song to finish
            while voice.is_playing():
                await asyncio.sleep(1)
        else:
            await ctx.send(f"The duration of the song '{song}' is not between 1 and 60.")


@client.command(pass_context=True)
async def play_all(ctx):
    all_songs = [str(i) for i in range(1, 60)]  # Generate a list of song names from 1 to 60
    await startsongs(ctx, *all_songs)

@client.command(pass_context=True)
async def next(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.stop()
        await ctx.send("Skipping the current song.")
    else:
        await ctx.send("No song is currently playing.")

@client.command(pass_context=True)
async def previous(ctx):
    
    await ctx.send("Not implemented")
    




@client.command(pass_content= True)
async def queue(ctx,arg):
    voice=ctx.guild.voice_client
    source=FFmpegPCMAudio(arg+'.mp3')
    
    guild_id= ctx.message.guild.id
    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id]=[source]
    await ctx.send("added to queue")


async def play_youtube(ctx, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        # Join the voice channel
        voice = await voice_channel.connect()
        # Download audio from the YouTube link
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'verbose': True  # Add this line for detailed output
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            except youtube_dl.utils.DownloadError as e:
                await ctx.send(f"Error: {e}")
                return
        # Play the downloaded audio
        source = discord.FFmpegPCMAudio(filename)
        voice.play(source)
    else:
        await ctx.send("You are not in a voice channel.")


@client.command(pass_content= True)
async def sr(ctx, url):
    await play_youtube(ctx, url)


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'user {member}has been kicked')


@kick.error
async def kick_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You dont have permissions to ban")


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'user {member}has been banned')


@ban.error
async def ban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You dont have permissions to ban people")

# The rest of your bot's code...

@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Dog",url="https://www.google.com/",description="love dog",color=0x4fdd4d)
    embed.set_author(name=ctx.author.display_name,url="https://www.youtube.com/",icon_url= ctx.author.avatar.url)
    embed.set_thumbnail(url="https://static.scientificamerican.com/sciam/cache/file/3C413E35-54FB-4690-AB17A213F928E090_source.jpg?w=1200")
    embed.add_field(name="Labrador",value="perrito que ladra",inline=True)
    embed.add_field(name="Chihuahua",value="cheese",inline=True)
    embed.set_footer(text="Bye bye")
    await ctx.send(embed=embed)
#client.run('Your key')

