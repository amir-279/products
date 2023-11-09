def play():
    user1_choice = input("select kon user 1: sang، kaghaz or gheychy: ")
    user2_choice = input("select kon user 2: sang، kaghaz or gheychy: ")    
    print("you selected: {user1_choice}")
    print("pc selected: {user2_choice}")
    
    if user1_choice == user2_choice:
        print("mosavi!")
    elif (user1_choice == 'sang' and user2_choice == 'gheychy') or \
         (user1_choice == 'kaghaz' and user2_choice == 'sang') or \
         (user1_choice == 'gheychy' and user2_choice == 'kaghaz'):
        print("user 1 victoty!")
    else:
        print("user 2 victory!")

play()