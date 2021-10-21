from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')

def sub():
  sleep(1)
  clear()
  print('You have chosen: Subtraction.')
  sleep(1)
  Amount = eval(input('How many numbers do you want to add(LIMIT:5)\n> '))
  i = 1
  n = 2
  while i < n:
    if Amount == 1:
      print('SYTEM ERROR: You need more than one number to subtract')
      input('\n|:PRESS ENTER WHEN DONE:|\n')
      sleep(1)
      clear()
      break
    if Amount == 2:
      f = eval(input('You have chosen 2 numbers, Choose your first number to be subtracted.\n> '))
      s = eval(input('Choose Your second number.\n> '))
      equ = (f)-(s)
      print('Your answer is:',equ)
      input('\n|:PRESS ENTER WHEN DONE:|\n')
      sleep(1)
      clear()
      break
    
    if Amount == 3:
      f = eval(input('You have chosen 3 numbers choose your first number to be subtracted.\n >'))
      s = eval(input('Choose your second number.\n >'))
      t = eval(input('Choose your third number.\n > '))
      equ = (f)-(s)-(t)
      print('Your answer is:',equ)
      input('|:PRESS ENTER WHEN DONE:|\n')
      sleep(1)
      clear()
      break

    if Amount == 4:
      f = eval(input('You have chosen 4 numbers choose your first number to be subtracted.\n> '))
      s = eval(input('Choose your second number.\n> '))
      t = eval(input('Choose your third number.\n> '))
      o = eval(input('Choose your fourth number.\n> '))
      equ = (f)-(s)-(t)-(o)
      print('Your answer is:',equ)
      input('\n|:PRESS ENTER WHEN DONE:|\n')
      sleep(1)
      clear()
      break
    
    if Amount == 5:
      f = eval(input('You have chosen 5 numbers choose your first number to be subtracted.\n>'))
      s = eval(input('Choose your second number.\n> '))
      t = eval(input('Choose your third number.\n> '))
      o = eval(input('Choose your fourth number.\n> '))
      fi = eval(input('Choose your fith number.\n> '))
      equ = (f)-(s)-(t)-(o)-(fi)
      print('Your answer is:',equ)
      input('\n|:PRESS ENTER WHEN DONE:|\n')
      sleep(1)
      clear()
      break
    
    if Amount > 5:
      print('ERROR MESSAGE: Please enter a valid number.')
      break

    if Amount < 5:
      print('ERROR MESSAGE: Please enter a valid number.')
      break