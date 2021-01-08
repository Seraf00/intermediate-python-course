def main():
  import random
  dice_roll = int(input('How many dice would you like to roll ?'))
  dice_size = int(input('How many sides are the dice '))
  dice_sum = 0
  for i in range(0,dice_roll):
     roll =random.randint(1,dice_size)
     if roll == 1:
         print(f'You rolled a {roll}! Loose !')
     elif roll == dice_size:
         print(f'You rolled a {roll}! Succes !')
     else:
         print(f'You rolled a {roll}')
     dice_sum = dice_sum + roll # we can use also dice_sum += roll
  print(f'You rolled {dice_sum}')
if __name__== "__main__":
  main()
