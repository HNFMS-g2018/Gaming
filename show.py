#!/usr/bin/python3
import os
import json
import time
import colorama

print('{}', file=open('marks.json', 'w')) # 分数清零
while True:
    os.system('./run.py 2> /dev/null')
    marks = json.load(open('marks.json', 'r'))
    marks = [(i[1], i[0]) for i in marks.items()]
    marks.sort(reverse=True)
    marks = [(i[1], i[0]) for i in marks]
    print('All player and their marks:')
    for i in marks:
        print(i[0], ':', i[1])
    sleep_time = 10
    for i in range(sleep_time):
        print('The next fight will start after {} seconds.'.format(sleep_time - i))
        print(colorama.Cursor.UP(1), end='')
        time.sleep(1)
    print()
    for i in range(len(marks) + 2):
        print(colorama.Cursor.UP(1), end='')
        print(colorama.ansi.clear_line(), end='')

