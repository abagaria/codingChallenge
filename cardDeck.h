#include <stdio.h>

/*
* Simple data structure representing a card. It has a unique identity
* and a pointer to another card
*/
typedef struct {
	int identity;		// identity of the card
	card_t *next;		// pointer to the card below self
} card_t;

/*
* Simple data structure representing a deck of cards. It is a stack which can
* be pushed to both from the top and the bottom.
*/
typedef struct {
	int num_cards;		// number of cards in the deck
	card_t *top;		// card at the top of the deck
	card_t *bottom;		// card at the bottom of the deck
} deck_t;

/* function prototypes for card game */
deck_t make_deck(int num_cards); // return a deck with unique identities
void move_to_top(deck_t *handdeck, deck_t *tabledeck); // change the decks given
void move_to_bottom(deck_t *handdeck); // change the hand deck
int is_equal(deck_t original_deck, deck_t tabledeck); // rebuilt original deck?
void play_round(deck_t *handdeck, deck_t *tabledeck); // play a 'round'
void print(deck_t deck); // print function for a deck_t object / structure