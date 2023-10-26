from color import Colors


class FileManager(Colors):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as file:
                text = file.read().lower()
                self.print('green', f'read(): {self.path} > {text}')
                return text
        except (FileNotFoundError, Exception) as e:
            self.print('red', f'read(): {self.path}', e)
            raise
    
    def write(self, text):
        try:
            with open(self.path, 'w') as file:
                file.write(text)
                self.print('green', f'write(): {self.path} > {text}')
        except (FileNotFoundError, Exception) as e:
            self.print('red', f'write(): {self.path}', e)
            raise

