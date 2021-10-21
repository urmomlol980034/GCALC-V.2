from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')

def mul():
  if 1 < 2:
    sleep(1)
    clear()
    print('You have chosen: Multiplication')
    sleep(1)
    f = eval(input('Choose your first number to multiply\n> '))
    s = eval(input('Choose your second number\n>'))
    print('Your answer is:',(f)*(s))
    input('|:PRESS ENTER WHEN DONE:|')
    sleep(1)
    clear()