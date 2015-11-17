##
#	Author: Akhil Bagaria
#	Date: November 16th, 2015
#	Coding challenge to manage a deck of cards. 
##
import copy

class Card:
	def __init__(self, identity, nextcard=None):
		self.identity = identity
		self.next = nextcard

	def __repr__(self):
		return str(self.identity)

class Deck:
	def __init__(self, numCards, topcard = None, bottomcard = None):
		self.numCards = numCards
		self.top = topcard
		self.bottom = bottomcard

	def __repr__(self):
		current = self.top
		returnstr = ""
		returnstr += str(current.identity) + '->'
		while current.next is not None:
			current = current.next
			returnstr += str(current.identity) + '->'
		return returnstr


def makeDeck(numCards):
	# hand deck of 5 cards
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
	if originalHandDeck is None:
		return None
	if tabledeck is None:
		return False

	tabledeck2 		   = copy.deepcopy(tabledeck)
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
	return None

if __name__ == '__main__':
	numCards = 5
	handdeck = makeDeck(numCards)

	# make a copy of the original deck for comparison later
	originalHandDeck = copy.deepcopy(handdeck)

	print "***BEFORE***"
	print "hand deck = ", handdeck
	print "top of deck = ", handdeck.top
	print "bottom of deck = ", handdeck.bottom

	# make an empty table deck
	tabledeck = Deck(numCards=numCards)

	# Place the top of handdeck into tabledeck
	handdeck, tabledeck = moveToTop(handdeck, tabledeck)

	print "***AFTER TOP MOVE***"
	print "handdeck = ", handdeck
	print "top of deck = ", handdeck.top
	print "bottom of deck = ", handdeck.bottom

	print "tabledeck = ", tabledeck
	print "topcard = ", tabledeck.top
	print "bottom card = ", tabledeck.bottom

	handdeck = moveToBottom(handdeck)
	print "***AFTER BOTTOM MOVE***"
	print "handdeck = ", handdeck
	print "top of deck = ", handdeck.top
	print "bottom of deck = ", handdeck.bottom

	fake = originalHandDeck
	print "****TEST EQUALITY 1 = TRUE****"
	print isEqual(originalHandDeck, fake)
	print "****TEST EQUALITY 2 = TRUE****"
	print isEqual(originalHandDeck, copy.deepcopy(originalHandDeck))
	print "****TEST EQUALITY 3 = FALSE****"
	print isEqual(originalHandDeck, None)
	print "****TEST EQUALITY 4 = FALSE****"
	fake2 = copy.deepcopy(fake)
	print isEqual(originalHandDeck, fake2)
	print "****TEST EQUALITY 5 = FALSE****"
	fake3 = copy.deepcopy(fake)
	print isEqual(originalHandDeck, moveToTop(fake3, Deck(numCards))[0])
	print "****TEST EQUALITY 6 = FALSE****"
	print isEqual(originalHandDeck, moveToTop(fake3, Deck(numCards))[0])
	print "fake = ", fake3











