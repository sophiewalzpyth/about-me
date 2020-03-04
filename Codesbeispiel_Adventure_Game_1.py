#I am still learning how to set up codes to catch input errors. 
import random
import numpy
from numpy.random import choice


health = [100, 250, 500]
ph = random.choice(health)
        
coins = [100, 500, 1000]
pc = random.choice(coins)

weaponhealth = (50, 100, 250)
pw = random.choice(weaponhealth)

turns = [10,11,12,13,14,15]
pt = random.choice(turns)

pchallenge = 0


goals = ['collect 5000 coins', 'make it to Solstein (Takes 17 turns)', 'defeat 10 challengers']
pg = random.choice(goals)

event = ['A stranger approaches you in the woods...', "You're beeing robbed!", 'You have come to a river crossing,', "You're low on food and should go for a hunt,", 'While strolling through the market, an old, suspicious woman offers you a glowing potion...', 'Your day was uneventful', 'You found a horse!', 'You found some coins!', "You've gotten lost!", 'You are being challenged to a duel!']

class Events:
    def choice():
       x = random.choice(event)
       print(x)
       global pc
       global pw
       global pt
       global ph
       global pchallenge

       if x == event[0]: #stranger
           opt = 'A. Attack!\nB. Attempt to run\nC. Wait for the stranger to speak'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               resultsa1 = ['You attacked the stranger and made it away with some of their gold', 'You stood your ground and managed to grab their weapon (+ 30 power)', "You've been wounded (-40 health)", "You've been wounded (health - 30) and your weapon has been damaged (- 50 power)"]
               a1 = (numpy.random.choice(resultsa1, p=[0.2, 0.25, 0.25, 0.3]))
               print(a1)
               if a1 == resultsa1[0]:                  
                   pc = int(pc) + 100
                   pchallenge = int(pchallenge) + 1
               elif a1 == resultsa1[1]:                   
                   pw = int(pw) + 30                   
                   pchallenge = int(pchallenge) + 1
               elif a1 == resultsa1[2]:
                   pw = int(pw) - 20                   
                   ph = int(ph) - 15
               elif a1 == resultsa1[3]:                   
                   pw = int(pw) - 50                 
                   ph = int(ph) - 40
               
           elif opts == 'B' or opts == 'b':
               resultsb1 = ['The stranger disappears in the distance as you run off.', 'You brush past the stranger, noticing a hidden knife in their pocket. Close one!', 'The stranger does not seem to notice as you scurry off.', 'The stranger calls out to you, but you cannot hear what they are saying.']
               b1 = (numpy.random.choice(resultsb1, p=[0.25, 0.25, 0.25, 0.25]))
               print(b1)
               
           elif opts == 'C' or opts == 'c':
               resultsc1 = ['The stranger smiles at you, handing you a nicely crafted sword and saying nothing more (+ 100 power)', 'The stranger begins to babble incoherently and appears drunk. You manage to slip away after an hour of confusing conversation.']
               c1 = (numpy.random.choice(resultsc1, p=[0.15, 0.85]))
               print(c1)
               if c1 == resultsc1[0]:
                   pw = int(pw) + 100

           #else:
               
               
       elif x == event[1]: #robber
           opt = 'A. Attack!\nB. Attempt to run\nC. Hand over valuables (- 150 coins)'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               resultsa2 = ['You attack the robber and manage to get away with 50 extra coin', 'You try to attack the robber, but it does not fair well. You lost some health (- 20) and 50 coins', 'You realized too late that attacking would be foolish, the robber attacks back, taking 150 coins and leaving you seriously injured (- 50 health)']
               a2 = (numpy.random.choice(resultsa2, p=[0.15, 0.60, 0.25]))
               print(a2)
               if a2 == resultsa2[0]:
                   pc = int(pc) + 50
                   pchallenge = int(pchallenge) + 1
               elif a2 == resultsa2[1]:
                   pc = int(pc) - 50
                   ph = int(ph) - 20
               elif a2 == resultsa2[2]:
                   pc = int(pc) - 150
                   ph = int(ph) - 50
                   
           elif opts == 'B' or opts == 'b':
               resultsb2 = ['You managed to run away withtout a scratch', 'You try to run, but the robber attacks. You lose 50 coins and are injured (-25 health)']
               b2 = (numpy.random.choice(resultsb2, p=[0.6, 0.40]))
               print(b2)
               if b2 == resultsb2[1]:
                   pc = int(pc) - 50
                   ph = int(ph) - 25
                   
           elif opts == 'C' or opts == 'c':
               resultsc2 = ['You pay off a large sum of 150 coins', 'You try to pay off the coins but do not have enough. The enraged robber attacks (- 500 health)']
               if pc >= 150:
                   print(resultsc2[0])
                   pc = int(pc) - 150
               else:
                   print(resultsc2[1])
                   ph = int(ph) -500
          #else:
               
       elif x == event[2]: #river
           opt = 'A. Cross carefully\nB. Cross quickly\nC. Look for another path'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               resultsa3 = ['You slowly and carefully made your way through the river. Success!', 'While trying to prepare for the forge, a heavy rain picked up and made the river impassible. You lose a day']
               a3 = (numpy.random.choice(resultsa3, p=[0.85, 0.15]))
               print(a3)
               if a3 == resultsa3[1]:
                   pt = int(pt) - 1
                   
           elif opts == 'B' or opts == 'b':
               resultsb3 = ['You hurried your way through the river. Success!', 'While carelessly hurrying through the river, you lose a pouch of 50 coins']
               b3 = (numpy.random.choice(resultsb3, p=[0.6, 0.4]))
               print(b3)
               if b3 == resultsb3[1]:
                   pc = int(pc) - 50
                   
           elif opts == 'C' or opts == 'c':
               resultsc3 = ['You found another way around the river and gained an extra day!', 'Your search around the river was futile, costing you two days travel time.']
               c3 = (numpy.random.choice(resultsc3, p=[0.45, 0.55]))
               print(c3)
               if c3 == resultsc3[0]:
                   pt = int(pt) + 1
               elif c3 == resultsc3[1]:
                   pt = int(pt) - 2
          #else:
               
       elif x == event[3]: #hunt
           opt = 'A. Hunt now\nB. Wait\nC. Skip'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               effects = [int(pc) + 50]
               print('Your hunt was successful. You gained 50 coins worth of meat to trade.')
               pc = int(pc) + 50
                              
           elif opts == 'B' or 'b':
               resultsb4 = ['You waited until the evening and managed to hunt down a large buck (+ 100 coin)', 'You decided to wait and hunt later. Unfortunately, no animals could be found. You have to go buy more meet at the market (-20 coin).']
               b4 = (numpy.random.choice(resultsb4, p=[0.25, 0.75]))
               print(b4)
               if b4 == resultsb4[0]:
                   pc = int(pc) + 100
               elif b4 == resultsb4[1]:
                   pc = int(pc) - 20
                
           if opts == 'C' or opts == 'c':
               print('You must venture to the market and pay 20 coins for some meat. It takes an entire extra day')
               pc = int(pc) - 20
               pt = int(pt) - 1
          #else:
               
       elif x == event[4]: #potion
           opt = 'A. Make accusations\nB. Refuse the potion\nC. Drink the potion (-15 coins)\nD. Throw the potion on her'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               print('The woman was arrested. I guess you will never know what potion she was offering you.')
               
           elif opts == 'B' or opts == 'b':
               print('The woman shrugs and wanders off. I guess you will never know what potion she was offering you.')
               
           elif opts == 'C' or opts == 'c':
               resultsc5 = ['You bought the potion for 15 coins and decided to drink it. You feel slightly odd, but nothing more seems to happen. Later in the evening, you feel a strange but wonderful rush. You feel stronger than ever (+50 ph).','You bought the potion for 15 coins. You immediately feel dizzy and dazed. When you come to, you realize 50 coins are missing and your weapon has been traded for a fish...', 'You bouoght the potion for 15 coins. You feel no changes. I guess that was a waste of 15 coins...']
               c5 =(numpy.random.choice(resultsc5, p=[0.15, 0.15, 0.7]))
               print(c5)
               if c5 == resultsc5[0]:
                   pc = int(pc) - 15
                   ph = int(ph) + 50
               elif c5 == resultsc5[1]:
                   pc = int(pc) - 65
                   pw == 30
               elif c5 == resultsc5[2]:
                  pc = int(pc) - 15
                  
           elif opts == 'D' or opts == 'd':
               resultsd5 = ['The potion spills on the old woman, transforming her into a powerful and mighty witch. She smiles at you in a disturbing manner.','Before the potion even spills on the woman, she casts a curse on you.']
               d5 = (numpy.random.choice(resultsd5, p=[0.6, 0.4]))
               print(d5)
               if d5 == resultsd5[1]:
                   ph = int(ph) - 500
          #else:
               
       elif x == event[5]: #rest
            opt = 'A. Rest'
            opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
            if opts == 'A' or opts == 'a':
                print('You feel relaxed and well rested.')
                ph = int(ph) + 50

            #else:
                
       elif x == event[6]: #horse
           opt = 'A. Take it\nB. Leave it'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               resultsa7 = ['You grabbed the horse and took off. You gained 2 days travel time!', 'The owner spots you stealing their horse! They attack leaving you with minor wounds (-25 health)']
               a7 = (numpy.random.choice(resultsa7, p=[0.2, 0.8]))
               print(a7)
               effects = [int(pt) + 2, int(ph) -25]
               if a7 == resultsa7[0]:
                   pt = int(pt) + 2
               elif a7 == resultsa7[1]:
                   ph = int(ph) - 25
           elif opts == 'B' or opts == 'b':
               print('You will never know what could have happened if you had taken the horse...')

           #else:    

       elif x == event [7]: #coin
           opt = 'A. Take it\nB. Leave it'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               resultsa8 = ['You pocketed the coin and took off. You gained 50 coins but feel guilty for the possible theft.', 'The owner of the coin returns from bathing to see you pocketing their money! They attack you and demand you pay them twice what you stole (-100 coin, -25 health)']
               a8 = (numpy.random.choice(resultsa8, p=[0.7, 0.3]))
               print(a8)
               if a8 == resultsa8[0]:
                   pc = int(pc) + 50
               elif a8 == resultsa8[1]:
                   pc = int(pc) - 100
                   ph = int(ph) - 25
           elif opts == 'B' or opts == 'b':
               print('You decided to leave the coin behind. Hopefully the person who lost it will find it where they left it.')

          #else:
           
       elif x == event[8]: #lost
           opt = 'A. Rest\nB. Search for a way out\nC. Panic'
           opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
           if opts == 'A' or opts == 'a':
               resultsa9 = ['You decide to rest and clear your mind before continuing. You fall asleep, and in your dream you remember a short cut you have used before. You awaken and exit the forest, gaining an extra days travel time.', 'Believeing a rest will clear your mind, you decide to nap near a tree. When you awaken, not only have you been robbed of 50 coins, but you are more lost than ever. It takes you two extra days to travel out of the woods.']
               a9 = (numpy.random.choice(resultsa9, p=[0.15, 0.85]))
               print(a9)
               if a9 == resultsa9[0]:
                   pt = int(pt) + 1
                   ph = int(ph) + 50
               elif a9 == resultsa9[1]:
                   pc = int(pc) - 50
                   pt = int(pt) -2
                   
           elif opts == 'B' or opts == 'b':
               resultsb9 = ['You decide to continue searching for a way out of the woods. With some dumb luck, you manage to find the exit.', 'You spend an entire day searching for the exit. Not only have you lost a day, but along the way you were robbed of 75 coin.']
               b9 = (numpy.random.choice(resultsb9, p=[0.6, 0.4]))
               print(b9)
               if b9 == resultsb9[1]:
                   pc = int(pc) - 75
                   pt = int(pt) -1
                   
           elif opts == 'C' or opts == 'c':
               resultsc9 = ['You begin a full scale panic. Along with loosing some coin (- 35 coin), you damaged your weapon (- 30 power) out of frustration following an ankle injury (- 35 health).', 'Your panic attracts the attention of a local hunter. After explaining that you are lost, he kindly guides you back out of the woods.']
               c9 =(numpy.random.choice(resultsc9, p=[0.75, 0.25]))
               print(c9)
               if c9 == resultsc9[0]:
                   ph = int(ph) - 35
                   pw = int(pw) - 30
                   pc = int(pc) - 35

        #  else:
               
       elif x == event[9]: #duel
          opt = 'A. Duel\nB. Attempt to Run\nC. Decline\nD. Attempt to talk your way out of it'
          opts = input('What will you do? \n' + opt + '\n\n' + name + ', remember you have:\nWon ' + str(pchallenge) + ' challenges\n' + str(ph) + ' health\n' + str(pc) + ' coins\n' + str(pw) + ' weapon power\n' + str(pt) + ' turns left\n')
          if opts == 'A' or opts == 'a':
               resultsa10 = ['You duel the challenger and fair quite well. Though you recieve minor injuries (- 15 health), you gain a large sum of 350 coins!', 'You fight to the best of your abilities, but cannot defeat the challenger (-40 health). Impressed by your courage however, they offers you 50 coins.', 'While entering the duel arena, you stumble and impail yourself on your sword (- 80 health)']
               a10 = (numpy.random.choice(resultsa10, p=[0.2, 0.6, 0.2]))
               print(a10)
               if a10 == resultsa10[0]:
                   ph = int(ph) - 15
                   pc = int(pc) + 350
                   pchallenge = int(pchallenge) + 1
               elif a10 == resultsa10[1]:
                   pc = int(pc) + 50
                   ph = int(ph) - 40
               elif a10 == resultsa10[2]:
                   ph = int(ph) - 80
                   
          elif opts == 'B' or opts == 'b':
               resultsb10 = ['You successfully run away!', 'You are caught before you can get away. A group of upset spectators take turns attacking you (- 50 health)', 'While entering the duel arena, you stumble and impail yourself on your sword (- 80 health)']
               b10 = (numpy.random.choice(resultsb10, p=[0.4, 0.6]))
               print(b10)
               if b10 == resultsb10[1]:
                   ph = int(ph) - 50
                   
          elif opts == 'C' or opts == 'c':
               print('You decline to fight and are charged 250 coins')
               pc = int(pc) - 250
               
          elif opts == 'D' or opts == 'd':
               resultsd10 = ['You attempt to talk your way out of the duel. The challenger listens intently and decides to call it off.', 'Your attempts to avoid the duel are futile. You lose the duel (-90 health) and are charged 100 coins.', 'Your attempts to avoid the duel are futile. You fight the opponent and manage to win. You recieve 300 coins and your weapon was slightly damaged (-35 power).']
               d10 = (numpy.random.choice(resultsd10, p=[0.1, 0.8, 0.1]))
               print(d10)
               if d10 == resultsd10[1]:
                   pc = int(pc) - 100
                   ph = int(ph) - 90
               elif d10 == resultsd10[2]:
                   pw = int(pw) - 35
                   pc = int(pc) + 300
               
          #else:

while pt >= -5:
    print("Welcome to Sophie's little adventure game. I hope you are ready to play!\n\n")
    print("You are going on an adventure to a city outside of Solstein. You will have " + str(pt) + " days. Along the way, you may encounter unexpected events. These events may even help you achieve your goal! Be warned though, not every choice you make has a good outcome.")
    name = input("What, may I ask, is your name, adventurer?\n")
    print("Horrah, " + name + "! I hope you are ready for your journey. Let's see how well you have prepared yourself.")


    if int(ph) == 100:
        pha = 'peasant'
        print("Ahh, I see you're a " + str(pha) + "... It seems you only have " + str(ph) + " health.")
        if int(pc) == 100:
            print("Oh no! It seems you only have " + str(pc) + " coins.\n")
        elif int(pc) == 500:
            print("You should fair well though with your " + str(pc) + " coins.\n")
        elif int(pc) == 1000:
            print("Oh! You're related to royalty! You have " + str(pc) + " coins.\n")
    elif int(ph) == 250:
        pha = 'soldier'
        print("Ahh, your trip shouldn't be so hard since you are a " + str(pha) + ". It seems you have " + str(ph) + " health.")
        if int(pc) == 100:
            print("It's a shame you only have " + str(pc) + " coins.\n")
        elif int(pc) == 500:
            print("You should fair well with your " + str(pc) + " coins.\n")
        elif int(pc) == 1000:
            print("Oh! You're part of the royal army! You have " + str(pc) + " coins.\n")
    elif int(ph) == 500:
        pha = 'knight'
        print("Oh! You're a " + str(pha) + "! You have " + str(ph) + " health.")
        if int(pc) == 100:
            print("You should learn to save though, you only have " + str(pc) + " coins.\n")
        elif int(pc) == 500:
            print("You should fair well with your " + str(pc) + " coins.\n")
        elif int(pc) == 1000:
            print("Of course since you have been knighted, you have " + str(pc) + " coins.\n")

    if int(pw) == 50:
        pwa = 'blunt dagger'
        print("Unfortunately, you only have a " + str(pwa) + ". Its limited to " + str(pw) + " power.")
    elif int(pw) == 100:
        pwa = 'sword'
        print("You should get a good use out of your " + str(pwa) + " since it has " + str(pw) + " power.")
    elif int(pw) == 250:
        pwa = 'sharpened blade'
        print("That " + str(pwa) + " certainly is quite a weapon! It has " + str(pw) + " power.")
        
    print('Now it is time for you to set off on your journey. I hope you have prepared for your first day.\nYour goal is to ' + str(pg) + '. Begin!\n\n')
    while pt >= 0 and pc >= 0 and ph >= 0 and pw >= 0:
        print(Events.choice())
        print('\n\n')
        pt = int(pt) - 1

    if ph <= 0 or pc <= -1 or pw <= -1 or pt <= -1:
        play_again = input(name + ", you don't have what it takes to complete your quest and become a champion. What a shame, you had such potential...\nWould you like to try again and see if you can become a mighty champion?\n (Y/N)")
        if play_again == 'Y' or play_again == 'y':
            ph = random.choice(health)
            pc = random.choice(coins)
            pw = random.choice(weaponhealth)
            pt = random.choice(turns)
            continue
        else:
            quit          

    if pg == goals[0]:
        if pc >= 5000:
            play_again = input(name + ", you've completed your quest and earned quite some coin. Congratulations champion!\nWould you like to try again and see if you will remain the mighty champ? (Y/N)\n")
            if play_again == 'Y' or 'y':
                ph = random.choice(health)
                pc = random.choice(coins)
                pw = random.choice(weaponhealth)
                pt = random.choice(turns)
                continue
            else:
                quit
    elif pg == goals[1]:
        if pt <= 0: # and design counter to determine if pt >= 17:##
            play_again = input(name + ", you've completed your quest and made it even further, all the way to Solstein. Congratulations champion!\nWould you like to try again and see if you will remain the mighty champ? (Y/N)\n")
            if play_again == 'Y' or play_again == 'y':
                ph = random.choice(health)
                pc = random.choice(coins)
                pw = random.choice(weaponhealth)
                pt = random.choice(turns)
                continue
            else:
                quit    
    elif pg == goals[2]:
        if pchallenge >= 10:
            play_again = input(name + ", you've completed your quest and become a true conquorer. Maybe you weren't always ethical, but hey, you won. Congratulations champion!\nWould you like to try again and see if you will remain the mighty champ? (Y/N)\n")
            if play_again == 'Y' or play_again == 'y':
                ph = random.choice(health)
                pc = random.choice(coins)
                pw = random.choice(weaponhealth)
                pt = random.choice(turns)
                continue
            else:
                quit  
    else:
        play_again = input("You've run out of time to finish your quest, " + name + ". I guess you were not meant to be our champion...\nWould you like to try again? (Y/N)\n")
        if play_again == 'Y' or play_again == 'y':
            ph = random.choice(health)
            pc = random.choice(coins)
            pw = random.choice(weaponhealth)
            pt = random.choice(turns)
            continue
        else:
            quit

