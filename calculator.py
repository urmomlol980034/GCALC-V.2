from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
      _ = system('clear')
l = 1
k = 2
clear()
while l < k:
  print('==================\n| By: GavinRepls |\n==================')
  print('OFFICIAL: CALCULATOR V.2')
  print('Copyright© GavinRepls 2021')
  print('How to use: checke the READ.md file.\n====================================')
  print('Menu:\n|> ADDITION = 1\n|> SUBTRACTION = 2\n|> MULTIPLICATION = 3\n|> DIVISION = 4\n|> SQUARE ROOT = 5\n|> CUBE ROOT = 6\n|> Even/Odd check = 7 ')
  Option = eval(input('\n|==> '))
  if Option == 1:
    from add import add
    add()
  if Option == 2:
    from sub import sub
    sub()
  if Option == 3:
    from mul import mul
    mul()
  if Option == 4:
    from div import div
    div()
  if Option == 5:
    from square import square
    square()
  if Option == 6:
    from cube import cube
    cube()
  if Option ==7:
    from evenorodd import evenorodd
    evenorodd()
  if Option > 7 or Option <  1:
    sleep(1)
    print('ERROR MESSAGE: Please enter a valid number.')
    sleep(2)
    clear()