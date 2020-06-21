from filereader import filereader

class Janitor:

    ##__bannedWords = ["sex"] 
    __bannedWords = filereader("list.txt").read()

    async def delete(self, message):
        await message.delete()
    
    async def sweep(self, message): 
        for val in self.__bannedWords:
            if val in message.content and self.checkForRole(message, "YOURROLEHERE") is False:
                await self.delete(message)
                print("Message deleted!")
    
    @staticmethod
    def checkForRole(message, Role):
        for role in message.author.roles:
            if role.name == Role:
                return True
        
        return False