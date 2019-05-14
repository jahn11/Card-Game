import random

money = 100
def makeValues():
    values = [1,2,3,4,5,6,7,8,9,0,0,0,0]
    deck = []
    for i in range(13):
        for j in range(7):


def makeNames():
    cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck.append(cards + "spades")
    deck.append(cards + "clubs")
    deck.append(cards + "diamonds")
    deck.append(cards + "hearts")

while money>0:
    input("Choose either Player A or Player B to win: ")
    A = []
    B = []
    randNum = random.randint(0,len(cards)-1)

    print("Player A cards: " ,A)
