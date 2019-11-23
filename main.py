import math
import random

def die():
    print("You died.")
    exit()

health = 10
enemyHealth = 10
defend = 0
forcefield = 0
print("Time to fight a monster.")
while True:
    if enemyHealth <= 0:
        print("Somehow you managed to kill the monster. Great job! You leveled up!\nSuddenly you hear something rustling behind you. It's another monster! It roars at you and jumps toward you.")
        die()
    if health < 0:
        health = 0
    print("\nYou have " + str(health) + " health.\n")
    if health == 0:
        print("That's not a good amount of health to have.")
        die()
    choice = input("Options:\n[A]ttack\n[D]efend\n[P]otion\n[S]pell\n[R]un\n")
    if choice == "A" or choice == "a":
        print("You attacked the monster.")
        print("The monster's spikes hurt you instead. You took 1 damage.")
        health -= 1
    elif choice == "D" or choice == "d":
        defend = random.randint(0, 3)
        print("You defend.\n" + ["Too bad! You fumble and drop your shield.", "It works, a little.", "It works pretty well.", "Your defensive stance is legendary."][defend])
    elif choice == "R" or choice == "r":
        print("You ran.")
        exit()
    elif choice == "P" or choice =="p":
        potion = math.floor(4 * random.random())
        print("You used a potion.\nYou pull a random one out of your Potion Bag™.")
        if potion == 0:
            print("Darn. This green potion is actually a poison. You must've misread the label.\n\nToo bad for you.")
            die()
        elif potion == 1:
            print("You throw a red potion at the monster. It seems to damage the monster.")
            enemyHealth -= 1.5
        elif potion == 2:
            print("You drink the contents of a blue potion and heal 2 damage.")
            health += 2
        elif potion == 3:
            print("You pull out a yellow potion. It creates a large explosion. It does 1 damage to you, but it seems to hurt the monster too.")
            enemyHealth -= 2
            health -= 1
        else:
            print("Potion " + int(potion) + "is not a real potion.")
            die()
    elif choice == "S" or choice == "s":
        spell = math.floor(4 * random.random()) # random 0-3 inclusive
        consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"]
        vowels = ["a", "e", "i", "o", "u"]
        print('You cast a spell.\n"' + random.choice(consonants).upper() + random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + '!" you say.')
        if spell == 0:
            print("The spell backfires. Your pants explode, dealing you 2 damage.")
            health -= 2
        elif spell == 1:
            print("Nice, the spell worked! That is, it worked to turn the monster into a frog.\n\nTemporarily.\n\nThe monster turns back into a monster and stares at you. Fear deals you 2 damage.")
            health -= 2
        elif spell == 2:
            print("The spell worked! It seems to damage the monster.")
            enemyHealth -= 1
        elif spell == 3:
            print("The spell creates a forcefield that seems to defend you from some damage.")
            forcefield = 1
    else:
        print("That's not an option.")
        die()
    print("The monster looks at you. Fear deals you " + str(4 - defend - 2 * forcefield) + " damage.")
    health += defend + 2 * forcefield - 4
    if forcefield:
        print("Your forcefield fizzles out.")
        forcefield = 0
    if defend:
        print("You leave your defensive stance.")
        defend = 0
