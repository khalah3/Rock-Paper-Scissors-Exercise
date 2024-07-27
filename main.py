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
print("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.")
import random



print("Enter your input")
userinput=int(input())
import random
random=random.randint(1,3)
computerrandom=random-1
list=["rock", "paper", "scissors"]

if list[userinput]==list[computerrandom]:
  print("It's a draw")
if list[userinput]==list[0] and list[computerrandom]==list[1]:
  print("You lose!")
if list[userinput]==list[0] and list[computerrandom]==list[2]:
  print("You Win!")
if list[userinput]==list[1] and list[computerrandom]==list[2]:
  print("You lose!")
if list[userinput]==list[1] and list[computerrandom]==list[0]:
  print("You Win!")
if list[userinput]==list[2] and list[computerrandom]==list[0]:
  print("You lose!")
if list[userinput]==list[2] and list[computerrandom]==list[1]:
  print("You Win!")
print(f"computer choice was {computerrandom}")