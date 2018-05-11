import asyncio
import discord

class TestBot(discord.Client):
    """ API Client. The provided api_key will be used as defaults
        for methods requiring this information. This can then be
        manually overridden.
    """
    def __init__(self,
                 login_token='NDQzNzI1NjY4NDYzOTM1NDg5.Ddds9w.pr8w6US8a85xEBpGYW3gvnt138g'):
        discord.Client.__init__(self)
        self.login_token = login_token

b = TestBot()
b.run()
