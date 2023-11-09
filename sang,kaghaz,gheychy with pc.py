import random

def play():
    user_choice = input("select kon: sang، kaghaz or gheychy: ")
    computer_choice = random.choice(['sang', 'kaghaz', 'gheychy'])
    
    print(f"you selected: {user_choice}")
    print(f"pc selected: {computer_choice}")
    
    if user_choice == computer_choice:
        print("mosavi!")
    elif (user_choice == 'sang' and computer_choice == 'gheychy') or \
         (user_choice == 'kaghaz' and computer_choice == 'sang') or \
         (user_choice == 'gheychy' and computer_choice == 'kaghaz'):
        print("you victoty!")
    else:
        print("pc victory!")

play()