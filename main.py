import random

def die():
    print("You died.")
    exit()

health = 10
enemyHealth = 10
defend = 0
forcefield = 0
confused = 0
ally = []

print("Time to fight a monster!")
while True:
    if enemyHealth <= 0:
        print("Somehow you managed to kill the monster. Great job! You leveled up!\nSuddenly you hear something rustling behind you. It's another monster! It roars at you and jumps toward you.\n")
        die()
    if health < 0:
        health = 0
    print("\nYou have " + str(health) + " health.\n")
    if health <= 0:
        print("That's not a good amount of health to have.")
        die()
    if confused:
        print("The enemy monster is confused.")
    if len(ally) == 1:
        print("You are aided by an ally.")
    elif len(ally) > 1:
        print("You are aided by " + str(len(ally)) + " allies.")
    choice = input("Options:\n[A]ttack\n[D]efend\n[P]otion\n[S]pell\n[R]un\n")
    if choice == "A" or choice == "a":
        print("You attacked the monster.")
        damage = random.randint(0, 1)
        print(["The monster's spikes hurt you instead. You took 1 damage.", "Your attack glances harmlessly off of the monster's rocky skin."][damage])
        health -= damage
    elif choice == "D" or choice == "d":
        defend = random.randint(0, 3)
        print("You defend.\n" + ["Too bad! You fumble and drop your shield.", "It works, a little.", "It works pretty well.", "Your defensive stance is legendary."][defend])
    elif choice == "R" or choice == "r":
        if random.random() > 0.5:
            print("You ran.")
            exit()
        else:
            print("You did not escape. Too bad!")
    elif choice == "P" or choice =="p":
        potion = random.randint(0, 4)
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
        elif potion == 4:
            print("You pull out an orange potion and throw it at the monster. It creates an explosion of smoke.\nThe monster becomes confused.")
            confused = 1
        else:
            print("Potion " + int(potion) + "is not a real potion.")
            die()
    elif choice == "S" or choice == "s":
        spell = random.randint(0, 4)
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
        elif spell == 4:
            print("The spell summons an ally to fight with you. That's pretty good. Sadly, the ally has only 2 health and deals only 1 damage.")
            ally.append(2)
        else:
            print("This spell is totes fake man. This message should not appear.")
            die()
    else:
        print("That's not an option.")
        die()
    if confused:
        print("The monster is confused. It hurt itself in its confusion!\n\nSadly, it's still scary. It looks at you. Fear deals you " + str(max(0, 3 - defend - 2 * forcefield)) + " damage.")
        enemyHealth -= 1
        health -= max(0, 3 - defend - 2 * forcefield)
        if random.random() > 0.5:
            print("The monster is still confused.")
        else:
            print("The monster shakes off its confusion.")
            confused = 0
    else:
        print("The monster looks at you. Fear deals you " + str(max(0, 4 - defend - 2 * forcefield)) + " damage.")
        health -= max(0, 4 - defend - 2 * forcefield)
    if len(ally) > 0:
            if len(ally) == 1:
                print("Your ally " + random.choice(["strikes", "smells", "ensnares", "licks"]) + " the monster. It seems to hurt it.")
                print("The monster looks at your ally. Since it was summoned by a magic spell, it only takes 1 damage.")
            else:
                print("Your allies " + random.choice(["strike", "smell", "ensnare", "lick"]) + " the monster. They seem to hurt it.")
            enemyHealth -= len(ally)
            if confused:
                print("The confused monster cannot find your all" + ["y", "ies"][len(ally) > 1] + " to make an attack.")
            else:
                oldLen = len(ally)
                ally = list(filter(lambda health: health > 0, map(lambda health: health - 1, ally))) # subtract 1 from each and lose all the ones that are 0 or less
                if oldLen - len(ally) == 1:
                    print("Your ally was destroyed. Sad!")
                elif oldLen - len(ally) > 1:
                    print(str(oldLen - len(ally)) + " of your allies were destroyed." + " Sad!" * (oldLen - len(ally)))    
    if forcefield:
        print("Your forcefield fizzles out.")
        forcefield = 0
    if defend:
        print("You leave your defensive stance.")
        defend = 0
