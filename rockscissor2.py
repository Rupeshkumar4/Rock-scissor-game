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
list=[rock,paper,scissors]
print(" 0. rock, 1.paper, 2. scissors\n")
ch = int(input("enter your choice\n"))
print(list[ch])

random_ch=random.randint(0,2)
# print(list[random_ch])
print(list[random_ch])
if ch==1 and random_ch==0:
  print("you wain\n")
elif ch==1 and random_ch==2:
  print("you loose\n")
elif ch==0 and random_ch==1:
  print("you loose\n")
elif ch==0 and random_ch==2:
  print("you win")
elif ch==2 and random_ch==0:
  print("you loose\n")
elif ch==2 and random_ch==1:
  print("you win")