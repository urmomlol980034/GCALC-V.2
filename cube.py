from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')

def cube():
  sleep(1)
  clear()
  print('You have chosen: Cube Root')
  sleep(1)
  f = eval(input('What number do you want to be cube rooted.\n> '))
  equ = f ** (1./3.)
  print('Your answer is:',equ)
  input('|:PRESS ENTER WHEN DONE:|')
  sleep(1)
  clear()