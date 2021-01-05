def main():
  import random
  dice_roll = 2
  dice_sum = 0
  for i in range(0,dice_roll):
     roll =random.randint(1,6)
     print(f'You rolled a {roll}')
     dice_sum = dice_sum + roll # we can use also dice_sum += roll
  print(f'You rolled {dice_sum}')
if __name__== "__main__":
  main()
