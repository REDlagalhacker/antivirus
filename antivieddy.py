import os
from time import sleep
sleep(1.2)
print('projected for suspected files and not fo common files')
sleep(2)
print('_' * 60)
os.system('@echo off')
cmnam = list()
susex = list()
q99 = 0
q = input('1)scan')
if q == '1':
    q1 = input('file(no extension) ')
    q2 = input('extension (no dot) ')
    e = input('compleate name ')
    if q2 == 'exe' or q2 == 'com' or q2 == 'bat':
        q99 = q99 + 1
    print('scan ' + e + ' 4%')
    sleep(1)
    print('defin name c')
    cmnam.append('hack')
    cmnam.append('virus')
    cmnam.append('malware')
    cmnam.append('open me')
    cmnam.append('openme')
    cmnam.append('open_me')
    cmnam.append('iloveyou')
    cmnam.append('i_love_you_')
    cmnam.append('loveyou')
    cmnam.append('Iloveyou')
    print('8%')
    if q1 in cmnam:
        q99 = q99 + 3
    print('15%')
    print('new defin bad ex')
    print('28%')
    sleep(1)
    susex.append('exe')
    susex.append('bat')
    susex.append('com')
    print('45%')
    susex.append('pdf')
    sleep(1)
    susex.append('py')
    if q2 in susex:
        q99 = q99 + 1
    if q99 > 3:
        print()
        print()
        print('#' * 60)
        sleep(0.7)
        print('MALWARE')
        eddy = input('eliminate? [y/n] ')
        if eddy == 'n' or eddy == 'N':
            print('file will not be eliminated')
        else:
            elim = input('enter file path ')
            os.system('del ' + elim)
    else:
        print('secure')
