import random
import time

#final fight
def final_fight():

    print("""Look like you succesfully made it trough all of the rooms.
Now its time to meet the final boss. Its mutated rat and now its time to fight.
(you can use low kick by pressing 7 or hand punch by pressing 8 - both of them deal 2 hp)
GOOD LUCK, """ + jmeno + "!")
    time.sleep(1.5)
    hp_rat = 10
    hp_player = 10

    fightstart = int(input("Type 1 to start the figth: "))

    if fightstart == 1:
        print("Rat has 10 hp and you have also 10 hp")
        time.sleep(1.5)

        strike1 = int(input("Punch it (7 or 8): "))
        if strike1 == 7:
            print("*Low kick*")
            time.sleep(0.5)
            print("*hit*")
            hp_rat = hp_rat - 2
            print(f"Rat has {hp_rat} hp left")
            
        elif strike1 == 8:
            print("*hand punch*")
            time.sleep(0.5)
            print("*hit*")
            hp_rat = hp_rat - 2
            print(f"Rat has {hp_rat} hp left")
            
        strike2 = int(input("Attack it (7 or 8): "))  
        if strike2 == 7:
            print("*Low kick*")  
            time.sleep(0.5)
            print("*miss*")
            print(f"Rat has {hp_rat} hp left")

        elif strike2 == 8:
            print("*Hand punch*")
            time.sleep(0.5)
            print("*miss*")
            print(f"Rat has {hp_rat} hp left")

        strike3 = int(input("One more time (7 or 8): "))
        if strike3 == 7:
            print("*Low kick*")  
            time.sleep(0.5)
            print("*miss*")
            print(f"Rat has {hp_rat} hp left")

        elif strike3 == 8:
            print("*Hand punch*")
            time.sleep(0.5)
            print("*miss*")
            print(f"Rat has {hp_rat} hp left")
            time.sleep(1)

        print("Now its rats turn, try to defend your self as much as you can, good luck!")
        time.sleep(4)
        
        cas = 5

        print(f"u have 5 seconds to doge it")
        time.sleep(2)
        zacatek_odpoctu = time.time()

        input("type 9 to dodge it: ")

        konec_odpoctu = time.time()

        celkovy_cas = konec_odpoctu - zacatek_odpoctu 

        if celkovy_cas <= cas:
            print("you dodge it")
            print(f"You have {hp_player} hp left")

        elif celkovy_cas > cas:
            print("you got hit")
            hp_player = hp_player - 2
            print(f"You have {hp_player} hp left")
        time.sleep(4)
        
        print("One more time")
        time.sleep(1.5)
        print(f"u have 5 seconds to doge it")

        zacatek_odpoctu = time.time()

        input("type 9 to dodge it: ")

        konec_odpoctu = time.time()

        celkovy_cas = konec_odpoctu - zacatek_odpoctu 

        if celkovy_cas <= cas:
            print("you dodge it")
            print(f"You have {hp_player} hp left")

        elif celkovy_cas > cas:
            print("you got hit")
            hp_player = hp_player - 2
            print(f"You have {hp_player} hp left")
        time.sleep(2)
        print("Rat is starting to be tired... Take a chance!")

        time.sleep(2)
        strike4 = int(input("Attack it (7 or 8): "))
        if strike4 == 7:
            print("*Low kick*")
            time.sleep(0.5)
            print("*Hit*")
            hp_rat = hp_rat - 2
            print(f"Rat has {hp_rat} hp left")

        elif strike4 == 8:
            print("*Hand punch*")
            time.sleep(0.5)
            print("*Hit*")
            hp_rat = hp_rat - 2
            print(f"Rat has {hp_rat} hp left")

        time.sleep(2.5)
        print("Now its rats turn, try to defend your self as much as you can, good luck!")
        time.sleep(4)
        
        cas = 5

        print(f"u have 5 seconds to doge it")
        time.sleep(2)
        zacatek_odpoctu = time.time()

        input("type 9 to dodge it: ")

        konec_odpoctu = time.time()

        celkovy_cas = konec_odpoctu - zacatek_odpoctu 

        if celkovy_cas <= cas:
            print("you dodge it")
            print(f"You have {hp_player} hp left")

        elif celkovy_cas > cas:
            print("you got hit")
            hp_player = hp_player - 2
            print(f"You have {hp_player} hp left")
            time.sleep(1.5)

        print("Rat fell on the ground give it K.O. with low kick")

        strike5 = int(input("Atatck it (7 for low kick): "))
        if strike5 == 7:
            print("*Low kick*")
            time.sleep(0.5)
            print("*Hit*")
            print("you Won!")
            time.sleep(1.5)
            hp_rat = hp_rat - 6
            time.sleep(2)
            print(f"""{jmeno}, unbeatatble player, who went trought all of the levels without dying.
Congratulation you won!""")
            exit()

#prostredni chodba
def chodba_zelena():

    #Room one
    pocet_pokusu = 4

    while True:
        if pocet_pokusu == 0:
            print("Game over :(")
            print("Panda beat you, you can see that it has years of experience in this")
            exit()

        cislo1 = random.randint(1,6)
        cislo2 = random.randint(1,6)

        game_start = int(input("Type 5 to start the game: "))

        print("Panda threw: ")
        time.sleep(2)
        print(cislo2)

        if game_start == 5:
            your_threw = int(input("type 5 to throw a dice roll: "))
            if your_threw == 5:

                print("You threw: ")
                time.sleep(2)
                print(cislo1)

                if cislo2 >= cislo1:
                    print("Try again...")
                    pocet_pokusu -= 1
                    time.sleep(1.5)
                    
                elif cislo2 < cislo1:
                    print("You won " + jmeno + "! It was good game, but next time be careful when you see me...")
                    time.sleep(1.5)
                    break
                
    #Room two   
    time.sleep(2.5) 
    print("Room Two ")
    time.sleep(2)
    
    print("""Look like its highly feared kungfu master. His only weakness is light.
Try to find torch in one of the 3 chests, Good luck """ + jmeno)
        
    cislo1 = random.randint(1,3)
    guess1 = 0
    pokusybro = 2

    while guess1 != cislo1:

        if pokusybro == 0:
            print("Game over :(")
            print("Kung fu master won. Dont be sad a lot of people died here")
            exit()

        guess1 = int(input("Is that chest 1, 2 or 3: "))
        if guess1 > cislo1:
            print("this chest is empty")
            pokusybro -=1

        elif guess1 < cislo1:
            print("this chest is empty")
            pokusybro -= 1

        else:
            print("There it is, you can blind him to countinue")
    time.sleep(2)
    print("Room three")
    print(f"Wheel spinning - one option is chosen at random (1, 2, 3, 4 or 5) Good luck {jmeno}!")
    #wheel spinning(room three)
    while True:
        
        x = int(input("Type 1 to spin: "))

        if x == 1:
            pepa = random.randint(1,5)
            print("*Wheel spinning*")
            time.sleep(1.5)
            print(pepa)
            if pepa == 1:
                print("1 - Nothing")
                time.sleep(1)
                print("You can continue without fighting or other dangerous things")
                break

            elif pepa == 2:
                print("2 - fight")
                time.sleep(1)
                print(f"You have to fight, good luck!")
                time.sleep(2)

                cislo = random.randint(1,10)
                guess = 0

                print("""Oh no! there is a snake that want to kill you.If you want to beat him,
you have to guess the right number from 1-10 (remember you have only 5 attempts)""")
    
                pocet_pokusu1 = 5
                while guess != cislo:
        
                    if pocet_pokusu1 == 0:
                        print("Game over :(")
                        print("thats sad ngl")
                        exit()

                    guess = int(input("guess the number: "))

                    if guess > cislo:
                        print("guess lower")
                        pocet_pokusu1 = pocet_pokusu1 - 1
                    elif guess < cislo:
                        print("guess higher")
                        pocet_pokusu1 -= 1
                    else:
                        print("That was close, but you survived")
                        break
            elif pepa == 3:
                print("Game over")
                time.sleep(1.2)
                print("The chance of this is low but it is what it is")
                exit()
        
            elif pepa == 4:
                print("You are spinning again!")

            elif pepa == 5:
                print("2 - fight")
                time.sleep(1)
                print(f"You have to fight, good luck!")
                time.sleep(2)

                cislo = random.randint(1,10)
                guess = 0

                print("""Oh no! there is a snake that want to kill you.If you want to beat him,
you have to guess the right number from 1-10 (remember you have only 5 attempts)""")
    
                pocet_pokusu1 = 5
                while guess != cislo:
        
                    if pocet_pokusu1 == 0:
                        print("Game over :(")
                        print("thats sad ngl")
                        exit()

                    guess = int(input("guess the number: "))

                    if guess > cislo:
                        print("guess lower")
                        pocet_pokusu1 = pocet_pokusu1 - 1
                    elif guess < cislo:
                        print("guess higher")
                        pocet_pokusu1 -= 1
                    else:
                        print("That was close, but you survived")
                        break
            break

#levá chodba
def chodba_zluta():
    
    #Room one
    cislo = random.randint(1,10)
    guess = 0

    print("Room one")
    print("""Oh no! there is a snake that want to kill you.If you want to beat him,
you have to guess the right number from 1-10 (remember you have only 5 attempts)""")
    
    pocet_pokusu1 = 5
    while guess != cislo:
        
        if pocet_pokusu1 == 0:
            print("Game over :(")
            print("thats sad ngl")
            exit()

        guess = int(input("guess the number: "))

        if guess > cislo:
            print("guess lower")
            pocet_pokusu1 = pocet_pokusu1 - 1
        elif guess < cislo:
            print("guess higher ")
            pocet_pokusu1 -= 1
        else:
            print("That was close " + jmeno + ", but you survived")

            #room two
            time.sleep(2)
            print("Room two")
            time.sleep(2)
            print("""Look like there is nothing special... Oh look over there, its panda with a dice roll and paper.
The paper says - You have to throw higher number than me but you have only four attempts.""")
            
            pocet_pokusu_ = 4

            while True:

                if pocet_pokusu_ == 0:
                    print("Game over :(")
                    print("Panda beat you, you can see that it has years of experience in this")
                    exit()
    
                cislo1 = random.randint(1,6)
                cislo2 = random.randint(1,6)

                time.sleep(1)
                game_start = int(input("Type 5 to start the game: "))

                print("Panda threw: ")
                time.sleep(2)
                print(cislo2)

                if game_start == 5:
                    your_threw = int(input("type 5 to throw a dice roll: "))
                    if your_threw == 5:

                        print("You threw: ")
                        time.sleep(2)
                        print(cislo1)

                        if cislo2 >= cislo1:
                            print("Try again...")
                            pocet_pokusu_ = pocet_pokusu_ - 1
                            time.sleep(1.5)

                        elif cislo2 < cislo1:
                            print("You won " + jmeno + "! It was good game, but next time be careful when you see me...")
                            break
    
    
    print("Room three")
    time.sleep(1.5)

    print("""Comleptly empty room with just a little keyboard and display. The display says - your task is to
guess the three digits PIN code to continue to the next room. 
The important thing is that if you write the code wrong, it's game over and the next room is closed forever. 
Good luck!""")
    time.sleep(4)

    continue1 = int(input("Type 1 to continue: "))
    if continue1 == 1:
        print("First digit: if you add 3 to it and then divide by 2 you will get the first digit")
        time.sleep(2)
        first_digit = int(input("First digit: "))
        print("*procesing*")
        time.sleep(2)

        print("Second digit: if you divide it by 2 and then add 3 you will get second digit")
        time.sleep(2)
        second_digit = int(input("Second digit: "))
        print("*procesing*")
        time.sleep(2)

        print("third digit: if you divide it by 6 and then subtract 6 you will get negative 5") 
        time.sleep(2)
        third_digit = int(input("Third digit: "))
        print("*procesing*")
        time.sleep(2)

        if first_digit == 3:
            print("first digit was right")

        else:
            print("wrong")
            print("Next room is closed for ever - You loose")
            exit()

        if second_digit == 6:
            print("second digit was right")

        else:
            print("Wrong")
            print("Next room is closed for ever - You loose")
            exit()

        if third_digit == 6:
            print("Third Digit was right")
            time.sleep(2)

        else:
            print("wrong")
            print("Next room is closed for ever - You loose")
            exit()

        print("You can continue. Look like you are really good at math! " + jmeno)

#pravá chodba
def chodba_oranzova():
    while True:
        
        x = int(input("Type 1 to spin: "))

        if x == 1:
            pepa = random.randint(1,5)
            print("*Wheel spinning*")
            time.sleep(1.5)
            print(pepa)
            if pepa == 1:
                print("1 - Nothing")
                time.sleep(1)
                print("You can continue without fighting or other dangerous things")
                break

            elif pepa == 2:
                print("2 - fight")
                time.sleep(1)
                print(f"You have to fight, good luck!")
                time.sleep(2)

                cislo = random.randint(1,10)
                guess = 0

                print("""Oh no! there is a snake that want to kill you.If you want to beat him,
you have to guess the right number from 1-10 (remember you have only 5 attempts)""")
    
                pocet_pokusu1 = 5
                while guess != cislo:
        
                    if pocet_pokusu1 == 0:
                        print("Game over :(")
                        print("thats sad ngl")
                        exit()

                    guess = int(input("guess the number: "))

                    if guess > cislo:
                        print("guess lower")
                        pocet_pokusu1 = pocet_pokusu1 - 1
                    elif guess < cislo:
                        print("guess higher")
                        pocet_pokusu1 -= 1
                    else:
                        print("That was close, but you survived")
                        break
            elif pepa == 3:
                print("Game over")
                time.sleep(1.2)
                print("The chance of this is low but it is what it is")
                exit()
        
            elif pepa == 4:
                print("You are spinning again!")

            elif pepa == 5:
                print("2 - fight")
                time.sleep(1)
                print(f"You have to fight, good luck!")
                time.sleep(2)

                cislo = random.randint(1,10)
                guess = 0

                print("""Oh no! there is a snake that want to kill you.If you want to beat him,
you have to guess the right number from 1-10 (remember you have only 5 attempts)""")
    
                pocet_pokusu1 = 5
                while guess != cislo:
        
                    if pocet_pokusu1 == 0:
                        print("Game over :(")
                        print("thats sad ngl")
                        exit()

                    guess = int(input("guess the number: "))

                    if guess > cislo:
                        print("guess lower")
                        pocet_pokusu1 = pocet_pokusu1 - 1
                    elif guess < cislo:
                        print("guess higher")
                        pocet_pokusu1 -= 1
                    else:
                        print("That was close, but you survived")
                        break
            break
    time.sleep(2)
    print("Room two")
    time.sleep(1.5)

    print("""Comleptly empty room with just a little keyboard and display. The display says - your task is to
guess the three digits PIN code to continue to the next room. 
The important thing is that if you write the code wrong, it's game over and the next room is closed forever. 
Good luck!""")
    time.sleep(4)

    continue1 = int(input("Type 1 to continue: "))
    if continue1 == 1:
        print("First digit: if you add 3 to it and then divide by 2 you will get the first digit")
        time.sleep(2)
        first_digit = int(input("First digit: "))
        print("*procesing*")
        time.sleep(2)

        print("Second digit: if you divide it by 2 and then add 3 you will get second digit")
        time.sleep(2)
        second_digit = int(input("Second digit: "))
        print("*procesing*")
        time.sleep(2)

        print("third digit: if you divide it by 6 and then subtract 6 you will get negative 5") 
        time.sleep(2)
        third_digit = int(input("Third digit: "))
        print("*procesing*")
        time.sleep(2)

        if first_digit == 3:
            print("first digit was right")

        else:
            print("wrong")
            print("Next room is closed for ever - You loose")
            exit()

        if second_digit == 6:
            print("second digit was right")

        else:
            print("Wrong")
            print("Next room is closed for ever - You loose")
            exit()

        if third_digit == 6:
            print("Third Digit was right")
            time.sleep(2)
        else:
            print("wrong")
            print("Next room is closed for ever - You loose")
            exit()

        print("You can continue. Look like you are really good at math! " + jmeno)
        time.sleep(2)

    #room three
    print("Room three")
    time.sleep(1.5)

    otazka = int(input("""There are three doors. Only one of them is going to the next room.
Choose carefully (Type 1 for first door, 2 for second door and 3 for last door): """))
    print("")
    if otazka == 1:
        print("The first door is correct. You are such a lucky guy! Keep going")

    elif otazka == 2:
        print("Oh no there is a tiger you have 5 second to close the door")
        time.sleep(4)

        cas3 = 5

        odpocet_zacatek = time.time()
        door_closing = int(input("Type 9 to close the door: "))
        if door_closing == 9:
            odpocet_konec = time.time()

            cas_celkovy = odpocet_konec - odpocet_zacatek

            time.sleep(1.5)

            if cas_celkovy <= cas3:
                print("You succesfully closed the door")
        
            elif cas_celkovy > cas3:
                print("The tiger ate you. You loose!")
                exit()
        else:
            print("That wrong! You loose, but dont worry, you can try again")
            exit()
    elif otazka == 3:
        print("""There is a big black hole. Be carefull dont fall into th... Wait you can see your reflection?
Oh its glass and it looks kinda strong. You can safely continue""")

print("Welcome to the game Cursed corridor!")
time.sleep(1.5)

jmeno = str(input("Select your nickname: "))
time.sleep(1.5)

print("Hello " + jmeno + """ ,you just found 
abandoned place, your task is to make it trough all of the rooms to the final one.
Be careful there are lots of dangerous things. Good luck!""")

startquestion = int(input("type 1 to start the game: "))
time.sleep(1)

#starting room
direction1 = int(input("Welcome to the starting room " + jmeno + """,
from here you have 3 choices - left, forward, right (type 4 for left, 8 for forward or 6 for right): """))

#room one(1)
if direction1 == 8:
    print("Room one")
    time.sleep(1.5)
    print("""Look like there is nothing special... Oh look over there, its panda with a dice roll and paper.
The paper says - You have to throw higher number than me but you have only four attempts.""")
    chodba_zelena()
    final_fight()
    exit()

#room one(2)
elif direction1 == 4:
    print("Room One")
    time.sleep(1.5)
    chodba_zluta()
    final_fight()
    exit()

#room one(3)
elif direction1 == 6:
    print("Room one")
    time.sleep(1.5)
    print(f"Wheel spinning -one option is chosen at random (1, 2, 3, 4 or 5) Good luck {jmeno}!")
    time.sleep(3)
    chodba_oranzova()
    final_fight()
    exit()

