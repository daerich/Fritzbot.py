import discord

class Janitor:

    def __init__(self):
        bannedWords = ["gay", "sex", "http", "https"] 
        self.__bannedWords = bannedWords

    async def delete(self, message):
        await message.delete()
    
    async def sweep(self, message): 
        for val in self.__bannedWords:
            if val in message.content:
                await self.delete(message)
                print("Message deleted!")
