class Colors():
    def __init__(self):
        self.color = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m'
        }
        self.reset = '\033[0m'

    def print_color(self, color, str, exception=""):
        print(self.color[color] + str + self.reset)
        print(exception)


color = Colors()


def read_file(path):
    text = ""
    try:
        with open(path, 'r') as file:
            text = file.read().lower()
        color.print_color('green', f"read_file(): {path} > '{text}'")
    except (FileNotFoundError, Exception) as e:
        color.print_color('red', f"read_file(): No such {path} found", e)
    return text

def write_file(path, text):
    try:
        with open(path, 'w') as file:
            file.write(text)
        color.print_color('green', f"write_file(): {path} > '{text}'")
    except (FileNotFoundError, Exception) as e:
        color.print_color('red', f"read_file(): No such {path} found", e)

def operator(a, b, c):
    return b if a else c

def operator_elif(a, b, c, d, e):
    return b if a else operator(c, d, e)

