# created by Sami Bosch on Thursday, 08 November 2018

# This file contains all functions necessary to start up the bot

import discord
from discord.ext.commands import Bot
from message_parser import init


def runbot(token):
    """Initializes the client's command handler and other non command related functionalities."""
    client = Bot(command_prefix="!")

    init(client)

    # All events unrelated to message parsing go here

    @client.event
    async def on_member_join(member):
        server = member.server
        welcome = discord.utils.get(server.channels, name="welcome")
        client.send_message(welcome, "Bonjour {} et bienvenue dans le serveur SINFO! Indique ton nom et ta section "
                                     "d'études (p.ex. 'Ingo Bot - sinf') ici pour qu'un modérateur puisse te vérifier "
                                     "et donner accès au reste du serveur.\n\nHey there and welcome {}! Please give "
                                     "your name and what studies you're following (e.g. 'Ingo Bot - sinf') so a "
                                     "moderator can verify you and give you access to the rest of the server."
                                     "".format(member.mention, member.mention))

    client.run(token)
