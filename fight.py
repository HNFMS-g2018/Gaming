#!/usr/bin/python3
import sys
import os
import random

def get_res(player):
    os.system('source/{} > /tmp/player'.format(player))
    res_file = open('/tmp/player', 'r')
    try:
        res = int(res_file.readline()[:-1])
        if res < 0 or res > 1:
            raise ValueError
    except ValueError:
        print('Error in {}'.format(player), file=sys.stderr)
        res = 0
    # if random.randint(0, 7) == 0: # 有一定概率出现传达失败的情况
        # res = 1 - res
    return res
    
def add_res(player, self_res, enemy_res):
    target = open('data/{}'.format(player), 'r')
    n = int(target.readline()[:-1])
    self_li = target.readline()[:-1]
    enemy_li = target.readline()[:-1]
    target.close()
    target = open('data/{}'.format(player), 'w')
    print(n + 1, file=target)
    print(self_li, self_res, file=target)
    print(enemy_li, enemy_res, file=target)
    target.close()
    
if __name__ == '__main__':
    playera, playerb = sys.argv[1:3]
    print('Fight: {} and {}'.format(playera, playerb), file=sys.stderr)
    resa = get_res(playera)
    resb = get_res(playerb)
    add_res(playera, resa, resb)
    add_res(playerb, resb, resa)

