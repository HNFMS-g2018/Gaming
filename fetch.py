#!/usr/bin/python3
import os

os.system('curl ftp://noip:noip@172.16.14.3/g2018/PersonalFile/Kewth/Gaming/ -l > /tmp/os')
source_list = open('/tmp/os')
while True:
    source = source_list.readline()[:-1]
    if not source:
        break
    os.system('curl ftp://noip:noip@172.16.14.3/g2018/PersonalFile/Kewth/Gaming/{0} \
            --output source/{0}'.format(source))
    print('get', source)
