from time import sleep
import random

print('\033[93m-=-\033[m' * 6)
print(' R O P A S C I !')
print('\033[93m-=-\033[m' * 6, '\n')

ppt = ['Rock', 'Paper', 'Scissors']
pc = random.choice(ppt)

print('\033[91mYour choice!\033[m')
print('\033[34m[1]\033[m Rock')
print('\033[34m[2]\033[m Paper')
print('\033[34m[3]\033[m Scissors')

us = int(input('Enter your move: '))

while us != 1 and us != 2 and us != 3:
    print('\033[91m\nINVALID COMMAND!\033[m')
    us = int(input('Enter your move: '))

print('\n\033[1;95mRO\033[m')
sleep(0.5)
print('\033[1;93mPAS\033[m')
sleep(0.5)
print('\033[1;34mCI\033[m!\n')
sleep(0.5)

if us == 1 and pc == ppt[1]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE ROCK!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE PAPER!'))
    print('\033[1;93m{:^20}\033[m'.format('PC WON'))
    print('-='*11)
elif us == 1 and pc == ppt[0]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE ROCK!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE ROCK!'))
    print('\033[1;93m{:^20}\033[m'.format('A TIE!'))
    print('-='*11)
elif us == 1 and pc == ppt[2]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE ROCK!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE SCISSORS!'))
    print('\033[1;93m{:^20}\033[m'.format('YOU WON!'))
    print('-='*11)
elif us == 2 and pc == ppt[0]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE PAPER!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE ROCK!'))
    print('\033[1;93m{:^20}\033[m'.format('YOU WON!'))
    print('-='*11)
elif us == 2 and pc == ppt[1]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE PAPER!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE PAPER!'))
    print('\033[1;93m{:^20}\033[m'.format('A TIE!'))
    print('-='*11)
elif us == 2 and pc == ppt[2]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE PAPER!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE SCISSORS!'))
    print('\033[1;93m{:^20}\033[m'.format('PC WON'))
    print('-='*11)
elif us == 3 and pc == ppt[0]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE SCISSORS!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE ROCK!'))
    print('\033[1;93m{:^20}\033[m'.format('PC WON'))
    print('-='*11)
elif us == 3 and pc == ppt[1]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE SCISSORS!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE PAPER!'))
    print('\033[1;93m{:^20}\033[m'.format('YOU WON!'))
    print('-='*11)
elif us == 3 and pc == ppt[2]:
    print('-='*11)
    print('\033[34m{:^20}\033[m'.format('YOU CHOOSE SCISSORS!'))
    print('\033[91m{:^20}\033[m'.format('PC CHOSE SCISSORS!'))
    print('\033[1;93m{:^20}\033[m'.format('A TIE!'))
    print('-='*11)
