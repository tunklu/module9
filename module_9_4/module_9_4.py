import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        if len(self.words) > 0:
            return choice(self.words)
        else:
            return ''

print(list(map(lambda x, y: x==y, first, second)))


def get_advanced_writer(file):
    def write_everything(*data_set):
        with open(file, 'a', encoding='utf-8') as f:
            for element in data_set:
                f.write(f'{element}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])