import os
import discord
import logging
import datetime
import messageparser


discord_user_email = 'email'
discord_user_password = 'password'
server_id = 'SERVER_ID'
client = discord.Client()
client.login(discord_user_email, discord_user_password)

@client.event
def on_message(message):
    if(message.content.startswith('!market')):
        print('Command not finnished.')
        client.send_message(message.channel,'Sorry, This Command is not working properly yet.')
    if message.channel.server and message.channel.server.id == server_id:
        print('Ignoreing commanads to this server' + server_id)
        return
    response = messageparser.parse(message)
    if(response is not None):
        client.send_message(message.channel, response)

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
