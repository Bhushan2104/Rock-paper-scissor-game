import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#basic rules in the game 
"""
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock."""

game_images=[rock,paper,scissors]
user_choose=int(input("What do you choose?Type 0 for Rock,1 For Paper or 2 For Scissors\n"))

if user_choose>=3 or user_choose<0:
    print("You type a invalid number You Lose!")
else:
   print(game_images[user_choose])

computer_choose=random.randint(0,2)
print(f"Computer choose:{computer_choose} ")
print(game_images[computer_choose])

if user_choose==0 and computer_choose==2:
    print("You Wins!")
elif computer_choose==0 and user_choose==2:
    print("You Lose")
elif computer_choose>user_choose:
    print("You Lose")
elif user_choose>computer_choose:
    print("You Wins!")
elif computer_choose==user_choose:
    print("It's a draw")

    
