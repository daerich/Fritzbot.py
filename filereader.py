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
            print("An error ocurred!Code FR")
    
    def readbetween(self, start, end):
        self.commands=[]
        try:
            with open(self.__path, "r") as f:
                copy=False
                for line in f:
                    if(line.startswith(start)):
                        copy=True
                        continue
                    elif(line.startswith(end)):
                        copy=False
                        break
                    elif(copy):
                        self.commands.append(line)
                        continue
        except:
            print("An error occurred!Code FRB")