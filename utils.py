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


def operator(a, b, c):
    return b if a else c

