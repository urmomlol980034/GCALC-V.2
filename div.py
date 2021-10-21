from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')

def div():
  sleep(1)
  clear()
  print('You have chosen: Division')
  f = eval(input('Choose your first number to be divided\n> '))
  s = eval(input('Choose your second number to go into your first number.\n>'))
  print('Your answer is:',(f)/(s))
  input('|:PRESS ENTER WHEN DONE:|')
  sleep(1)
  clear()