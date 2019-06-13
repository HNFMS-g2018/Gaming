#!/usr/bin/python3
import os
import json
import time
import random
import colorama

def update_marks(player, marks):
    if not marks.get(player):
        marks[player] = 0
    data = open('data/{}'.format(player), 'r')
    n = int(data.readline()[:-1])
    self_li = [int(i) for i in data.readline()[:-1].split()]
    enemy_li = [int (i) for i in data.readline()[:-1].split()]
    for i in range(n):
        a, b, c = self_li[i], enemy_li[i], 0
        if a == 0 and b == 0:
            c = 0
        elif a == 0 and b == 1:
            c = 4
        elif a == 1 and b == 0:
            c -= 1
        elif a == 1 and b == 1:
            c += 4
        marks[player] += c

if __name__ == '__main__':
    source_file = os.listdir('source')
    marks = json.load(open('marks.json', 'r'))
    for i in os.listdir('source'):
        for j in os.listdir('source'):
            if i != j:
                print('{} Fight {}...'.format(i, j))
                print(colorama.Cursor.UP(1), end='')
                print(colorama.ansi.clear_line(), end='')
                print(0, file=open('data/{}'.format(i), 'w'))
                print(0, file=open('data/{}'.format(j), 'w'))
                for k in range(random.randint(12, 18)):
                    os.system('./fight.py {} {}'.format(i, j))
                update_marks(i, marks)
                update_marks(j, marks)
    json.dump(marks, open('marks.json', 'w'))
