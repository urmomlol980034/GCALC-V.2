from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')

def evenorodd():
  sleep(1)
  clear()
  print('You have chosen: Even/Odd check')
  numcheck = eval(input('Choose a number to see if its even or odd.\n>'))
  if numcheck % 2 == 0:
    print('Your number',numcheck,'is: Even')
  if numcheck % 2 == 1:
    print('Your number',numcheck,'is: odd')
  input('|:PRESS ENTER WHEN DONE:|')
  sleep(1)
  clear()