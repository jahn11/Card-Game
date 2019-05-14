import random

money = 100
deckValue = []
def makeValues():
    values = [1,2,3,4,5,6,7,8,9,0,0,0,0]
    deckValue = []
    newValue = []
    for i in range(13):
        newValue.append([values[i]]*4)

    
    for j in range(13):
        deckValue = deckValue + newValue[j]
    return deckValue 
valueResult = makeValues()

deck = []
def makeNames():
    cards = []
    deck = []
    hand = []
    spades = "spades"
    hearts = "hearts"
    diamonds = "diamonds"
    clubs = "clubs"
    cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for i in range(13):
        deck.append(cards[i] + " " + str(spades))
        deck.append(cards[i] + " " + str(clubs))
        deck.append(cards[i] + " " + str(diamonds))
        deck.append(cards[i] + " " + str(spades))
    
    return deck



    

while money>0:
    answer = input("Choose either Player A or Player B to win: ")
    nameResult = makeNames()
    rand1 = random.randint(0,len(nameResult)-1)
    rand2 = random.randint(0,len(nameResult)-1)
    rand3 = random.randint(0,len(nameResult)-1)
    rand4 = random.randint(0,len(nameResult)-1)
    rand5 = random.randint(0,len(nameResult)-1)
    rand6 = random.randint(0,len(nameResult)-1)
    A = [nameResult.pop(rand1),nameResult.pop(rand2)]
    nameResult = makeNames()
    print("Player A cards:", A)
    handA = valueResult[rand1] + valueResult[rand2]
    if handA >= 10:
        handA = str(handA)[1]
        handA = int(handA)
    print("Initial hand value:", int(handA))
    finalA = 0
    if int(handA) != 8 | int(handA) != 9:
        lastCardA = nameResult.pop(rand5)
        print("Player A draws a", lastCardA)
        finalA = int(handA) + valueResult[rand5]
        if finalA >= 10:
            finalA = str(finalA)[1]
            finalA = int(finalA)
        print("Player A final total is", int(finalA))
    elif int(handA) == 8 | int(handA) == 9:
        print("Player A is done")
        finalA = int(handA)
        print("Player A final total is", int(finalA))
    print("")
    print("")
    nameResult = makeNames()
    B = [nameResult.pop(rand3),nameResult.pop(rand4)]
    nameResult = makeNames()

    print("Player B cards:", B)
    handB = valueResult[rand3] + valueResult[rand4]
    if handB >= 10:
        handB = str(handB)[1]
        handB = int(handB)
    print("Initial hand value:", int(handB))
    finalB = 0
    if int(handB) != 8 | int(handB) !=9:
        lastCardB = nameResult.pop(rand6)
        print("Player B draws a", lastCardB)
        finalB = int(handB) + valueResult[rand6]
        if finalB >= 10:
            finalB = str(finalB)[1]
            finalB = int(finalB)
        print("Player B final total is", int(finalB))
    elif int(handB) == 8 | int(handB) == 9:
        print("Player B is done")
        finalB = int(handB)
        print("Player B final total is", int(finalB))
    print("")
    print("")
    if answer == "A":
        if finalA>finalB:
            money += 10
            print("Player A wins")
            print("You win")
            print("money is:", money)
        elif finalB>finalA:
            money = money - 10
            print("Player B wins")
            print("You lost")
            print("money is:", money)
        elif finalA == finalB:
            print("It's a tie")
            print("NO winner")
            print("money is:", money)
    print("")
    if answer == "B":
        if finalB>finalA:
            money += 10
            print("Player B wins")
            print("You win")
            print("money is:", money)
        elif finalA>finalB:
            money = money - 10
            print("Player A wins")
            print("You lost")
            print("money is:", money)
        elif finalA == finalB:
            print("It's a tie")
            print("NO winner")
            print("money is:", money)
    print("")


