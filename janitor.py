import configparser
from filereader import filereader

class config:
    config = configparser.ConfigParser()
    config.read("bot.ini")

class Janitor:

    __bannedWords = filereader("list.txt").read()
    
    async def delete(self, message):
        await message.delete()
    
    async def sweep(self, message): 
        for val in self.__bannedWords:
            if val in message.content and self.checkForRole(message, config.config.get('General', 'Moderator')) is False:
                await self.delete(message)
                print("Message deleted!")
    
    @staticmethod
    def checkForRole(message, Role):
        for role in message.author.roles:
            if role.name == Role:
                return True
        
        return False