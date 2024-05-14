from nextcord.ext import commands
import discord
from nextcord import FFmpegPCMAudio
import os
from nextcord.utils import get
import logging
import time
from nextcord import Interaction
import nextcord



import requests
import asyncio

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queues = {}  # Use `self.queues` to store queues
    testServerId=1223345494353248317

    @nextcord.slash_command(name="musictesting",description="introduction to slash commands",guild_ids=[testServerId])
    async def musictesting(self,interaction:Interaction):
        await interaction.response.send_message("MUSIC")


    def check_queue(self, ctx, guild_id):
        # Check if the queue is not empty
        if self.queues.get(guild_id):
            voice = ctx.guild.voice_client
            source = self.queues[guild_id].pop(0)
            voice.play(source, after=lambda e=None: self.check_queue(ctx, guild_id))

    @commands.command()
    async def bye(self, ctx):
        await ctx.send("Bye bot!")

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('10.mp3')
            voice.play(source)
        else:
            await ctx.send("You're not in the voice channel for the command to work")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice chat.")
        else:
            await ctx.send("I am not in a voice channel.")

    @commands.command()
    async def pause(self, ctx):
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.pause()
        else:
            await ctx.send("At the moment, there's no sound playing.")

    @commands.command()
    async def resume(self, ctx):
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_paused():
            voice.resume()
        else:
            await ctx.send("At the moment, there is no paused song.")

    @commands.command()
    async def stop(self, ctx):
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if voice:
            voice.stop()
        else:
            await ctx.send("I'm not playing any music right now.")

    @commands.command()
    async def play(self, ctx, arg):
        try:
            # Convert `arg` to integer and check the range
            song_number = int(arg)
            if 1 <= song_number <= 60:
                voice = ctx.guild.voice_client
                source = FFmpegPCMAudio(f"{song_number}.mp3")
                voice.play(source, after=lambda e=None: self.check_queue(ctx, ctx.message.guild.id))
            else:
                await ctx.send("The variable is not between 1 and 60.")
        except ValueError:
            await ctx.send("Invalid song number provided.")
    @commands.command()
    async def start(self, ctx, arg):
        logging.info(f"Received start command with arg: {arg}")
        start_time = time.time()
    
        try:
            song_number = int(arg)
            logging.info(f"Song number received: {song_number}")
        
            if 1 <= song_number <= 60:
                voice = get(ctx.bot.voice_clients, guild=ctx.guild)
            
            # Connect to voice if not connected
                if not voice:
                    channel = ctx.author.voice.channel
                    logging.info(f"Connecting to voice channel: {channel}")
                    voice = await channel.connect()
            
            # Load the audio file
                audio_file_path = f"{song_number}.mp3"
                if os.path.exists(audio_file_path):
                    source = FFmpegPCMAudio(audio_file_path)
                    logging.info(f"Playing song: {audio_file_path}")
                
                # Play the audio
                    voice.play(source)
                    await ctx.send("Playing music...")
                else:
                    await ctx.send("The song file does not exist.")
        
            else:
                await ctx.send("The variable is not between 1 and 60.")
    
        except ValueError:
            await ctx.send("Invalid song number provided.")
    
        end_time = time.time()
        logging.info(f"Time taken to start song: {end_time - start_time} seconds")


    @commands.command()
    async def startsongs(self, ctx, *args):
        if not args:
            await ctx.send("No songs provided.")
            return
        for song in args:
            try:
                song_number = int(song)
                if 1 <= song_number <= 60:
                    voice = get(ctx.bot.voice_clients, guild=ctx.guild)
                    if voice and voice.is_playing():
                        voice.stop()
                        await ctx.send("Already playing music.")
                    elif voice and voice.is_connected():
                        # If voice is already connected and playing
                        print("song ended")
                    channel = ctx.author.voice.channel
                    if channel:
                        if not voice:
                            voice = await channel.connect()
                        else:
                            if voice.channel != channel:
                                await voice.move_to(channel)
                    else:
                        await ctx.send("You're not in a voice channel for the command to work.")
                        return

                    source = FFmpegPCMAudio(f"{song_number}.mp3")
                    voice.play(source)
                    await ctx.send(f"Playing music '{song}'.")
                    # Wait for the song to finish
                    while voice.is_playing():
                        await asyncio.sleep(1)
                else:
                    await ctx.send(f"The song '{song}' is not between 1 and 60.")
            except ValueError:
                await ctx.send(f"Invalid song number provided for '{song}'.")

    @commands.command()
    async def play_all(self, ctx):
        # Play all songs from 1 to 60
        all_songs = [str(i) for i in range(1, 61)]
        await self.startsongs(ctx, *all_songs)

    @commands.command()
    async def next(self, ctx):
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.stop()
            await ctx.send("Skipping the current song.")
        else:
            await ctx.send("No song is currently playing.")

    @commands.command()
    async def previous(self, ctx):
        await ctx.send("Not implemented yet.")

    @commands.command()
    async def queue(self, ctx, arg):
        try:
            song_number = int(arg)
            voice = ctx.guild.voice_client
            source = FFmpegPCMAudio(f"{song_number}.mp3")
            guild_id = ctx.guild.id

            if guild_id in self.queues:
                self.queues[guild_id].append(source)
            else:
                self.queues[guild_id] = [source]

            await ctx.send("Added to queue.")
        except ValueError:
            await ctx.send("Invalid song number provided.")

def setup(client):
    client.add_cog(Music(client))
