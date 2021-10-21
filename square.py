from os import system, name
from time import sleep
from math import sqrt
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')

def square():
  sleep(1)
  clear()
  print('You have chosen: Square Root')
  f = eval(input('What number do you want to be square rooted?\n> '))
  equ = sqrt(f)
  print('Your answer is:',equ)
  input('|:PRESS ENTER WHEN DONE:|')
  sleep(1)
  clear()