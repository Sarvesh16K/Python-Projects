import random
def play():
    user_in = input("Rock..Paper...Scissorsss!!! ")
    com = random.choice(['r','p','s'])

    if win(user_in,com):
        print("Congrats!!!You Won!!!")
    else:
        print("Oops!!!Sorry, You Lost!!")

def win(user_in, com):
    if((user_in.lower()=='r' and com=='s') or (user_in.lower()=='s' and com=='p') or (user_in.lower()=='p' and com=='r')):
        return True
    else:
        return False

print('''------MENU------
  Rock - r/R
  Paper - p/P
  Scissor - s/S''')
p = True
while(p==True):
    play()
    i = input("Wanna Continue(c) or Quit(q) :")
    if (i.lower()=='q'):
        p = False
