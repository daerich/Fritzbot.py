import io

class filereader:

    def __init__(self, path):
        self.__path = path

    def read(self):
        try:
            with open(self.__path, "r") as f:
                content = f.readlines()

            self.content = [x.strip() for x in content] 
            return self.content
        except:
            print("An error ocurred!")