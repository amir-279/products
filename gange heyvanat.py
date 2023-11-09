import random

animals = {
    'shir': 10,
    'babr': 9,
    'gorg': 8,
    'palang': 7,
    'goril': 6,
    'khers': 5,
    'khok': 4,
    'sag': 3,
    'gorbe': 2,
    'mosh': 1
}

def calculate_power(animal):
    return animals[animal]

def battle(an1, an2):
    power1 = calculate_power(an1)
    power2 = calculate_power(an2)

    if power1 > power2:
        winner = an1
        loser = an2
    elif power1 < power2:
        winner = an2
        loser = an1
    else:
        print("mosavi!")
        return

    print(f"win: {winner}")
    print(f"los: {loser}")


an1 = input(list(animals.keys()))
an2 = input(list(animals.keys()))
print(" an 1: {an1}")
print(" an 2: {an2}")
battle(an1, an2)
#get help as google