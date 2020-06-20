from filereader import filereader

class Janitor:

    ##__bannedWords = ["sex"] 
    __bannedWords = filereader("list.txt").read()

    async def delete(self, message):
        await message.delete()
    
    async def sweep(self, message): 
        for val in self.__bannedWords:
            if val in message.content:
                await self.delete(message)
                print("Message deleted!")
