##
#   Author: Akhil Bagaria
#   Date: November 16th, 2015
#   Coding challenge to manage a deck of cards. 
##
import copy
import sys

# Simple data structure representing a card. It has a unique identity
# and a pointer to another card
class Card:
    def __init__(self, identity, nextcard=None):
        self.identity = identity
        self.next = nextcard

    def __repr__(self):
        return str(self.identity)

# Simple data structure representing a deck of cards. It is a stack which can
# be pushed to both from the top and the bottom. It has a print function for 
# debugging purposes. 
class Deck:
    def __init__(self, numCards, topcard = None, bottomcard = None):
        self.numCards = numCards
        self.top = topcard
        self.bottom = bottomcard

    def __repr__(self):
        current = self.top
        if current is None:
            return ""
        returnstr = ""
        returnstr += str(current.identity) + '->'
        while current.next is not None:
            current = current.next
            returnstr += str(current.identity) + '->'
        return returnstr

# Call this function to initialize a deck of cards with numCards cards.
def makeDeck(numCards):
    # hand deck of n cards
    handdeck = Deck(numCards=numCards)

    # make deck in hand
    for i in range(numCards):
        card = Card(identity=i, nextcard=handdeck.top)

        # make the new card the top of the stack
        handdeck.top = card

        # make the first card the bottom of the stack
        if i == 0:
            handdeck.bottom = card

    return handdeck

# Given a deck of cards, simulate the process of picking out the 
# top card and placing that into the table deck. 
def moveToTop(handdeck, tabledeck):
    if handdeck.top == None:
        return 

    # if hand deck only has one card remaining, flag it so that we can 
    # later set its bottom to None
    bottomFlag = False
    if handdeck.top.identity == handdeck.bottom.identity:
        bottomFlag = True

    # top of the hand deck
    topcard = handdeck.top

    # update what is the top of the hand deck
    handdeck.top = handdeck.top.next

    # place the top of the hand deck to the top of the table deck
    topcard.next = tabledeck.top
    tabledeck.top = topcard

    # if topcard is the only card in the table deck, set its bottom
    if tabledeck.bottom is None:
        tabledeck.bottom = tabledeck.top

    # if top was also bottom (last card in deck), set the bottom to null
    if bottomFlag:
        handdeck.bottom = None

    return (handdeck, tabledeck)

# Move the top of the hand deck to the bottom
def moveToBottom(handdeck):

    # if no top card, return
    if handdeck.top is None:
        return

    # tmp vars for top and bottom cards
    # deep copy because python defaults to object bindings, not copies
    topcard =  copy.deepcopy(handdeck.top)
    bottomcard = copy.deepcopy(handdeck.bottom)

    # update the bottom of the deck
    handdeck.bottom.next = topcard
    handdeck.bottom = topcard
    handdeck.bottom.next = None

    # update the top of the deck
    handdeck.top = handdeck.top.next

    # return the updated deck
    return handdeck

def isEqual(originalHandDeck, tabledeck):
    if originalHandDeck.top is None:
        return None
    if tabledeck.top is None:
        return False

    tabledeck2         = copy.deepcopy(tabledeck)
    originalHandDeck2  = copy.deepcopy(originalHandDeck)

    currentTable = tabledeck2.top
    currentHand  = originalHandDeck2.top

    while currentHand.next is not None and currentTable.next is not None:
        if currentHand.identity != currentTable.identity:
            return False

        # update the currents
        currentHand  = currentHand.next
        currentTable = currentTable.next

    return True

# A round is defined as taking a card from hand and placing it on the table, 
# then placing the next card in hand to the bottom of the hand deck until all
# the cards in the hand deck is in on the table deck.
def playRound(handdeck, tabledeck):
    while handdeck.top is not None:
        moveToTop(handdeck, tabledeck)
        moveToBottom(handdeck)

if __name__ == '__main__':
    # get the number of cards as a terminal input
    numCards = int(sys.argv[1])

    # initialize the hand deck with numCards cards
    handdeck = makeDeck(numCards)

    # make a copy of the original deck for comparison later
    originalHandDeck = copy.deepcopy(handdeck)

    print "*** Starting Deck ***"
    print "hand deck = ", handdeck
    print "top of deck = ", handdeck.top
    print "bottom of deck = ", handdeck.bottom

    # make an empty table deck
    tabledeck = Deck(numCards=numCards)

    numRounds = 0
    while True:
        playRound(handdeck, tabledeck)
        print "table deck = ", tabledeck
        handdeck = copy.deepcopy(tabledeck)
        tabledeck = Deck(numCards)
        numRounds += 1
        if isEqual(originalHandDeck, handdeck):
            break
    print "Number of rounds to get back to original deck = ", numRounds 