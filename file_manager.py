class FileManager():
    def __init__(self, path):
        self.path = path

    def read(self):
        text = ""
        try:
            with open(self.path, 'r') as file:
                text = file.read().lower()
        except (FileNotFoundError, Exception) as e:
            print(e)
        return text
    
    def write(self, text):
        try:
            with open(self.path, 'w') as file:
                file.write(text)
        except (FileNotFoundError, Exception) as e:
            print(e)

