#include "card_deck.h"
#include <stdlib.h>

/*
*	This function takes in the number of cards and returns a pointer 
*	to the head and tail of the stack of cards.
*/
deck_t *make_deck(int num_cards) {

	// hand deck of n cards
	deck_t *deck = (deck_t *)malloc(sizeof(deck_t));

	deck->num_cards = num_cards;
	deck->top = NULL;
	deck->bottom = NULL;

	// make deck in hand
	int i;
	for (i = 0; i < num_cards; ++i) {
		card_t *card = (card_t *)malloc(sizeof(card_t));

		// assign unique identity to the card
		card->identity = i;

		// make the new card the top of the stack
		card->next = deck->top;

		// update the top of the deck
		deck->top = card;

		// make the bottom card the bottom of the stack
		if (i == 0) {
			deck->bottom = card;
			card->next = NULL;
		}
	}

	return deck;
}

/*
*	Given a hand deck and a table deck, move the top of the hand deck 
*	to the top of the table deck
*/
void move_to_top(deck_t *handdeck, deck_t *tabledeck) {
	
	// if hand deck is empty, there is nothing to move
	if (handdeck->top == NULL) {
		printf("move_to_top called on an empty deck\n");
		return;
	}

	// If hand deck only has one card remaning, then we need to make its 
	// bottom to nullptr. We thus need a flag to track if thats true
	int bottom_flag = 0;
	if (handdeck->top->identity == handdeck->bottom->identity) {
		bottom_flag = 1;
	}

	// store the 2nd card in a tmp var
	card_t *new_head = handdeck->top->next;

	// make the top of the hand deck point at the current top of the 
	// table deck as the its next card
	handdeck->top->next = tabledeck->top;

	// update the table deck's head
	tabledeck->top = handdeck->top;

	// update the hand deck's top
	handdeck->top = new_head;

	// if table deck only has one card, then set its bottom
	if (tabledeck->bottom == NULL) {
		tabledeck->bottom = tabledeck->top;
	}

	if (bottom_flag) {
		handdeck->bottom = NULL;
	}

	return;
}

/*
*	Given a pointer to the deck, move the top card to the bottom. 
* 	In the process, update the top and bottom of the deck.
*/
void move_to_bottom(deck_t *handdeck) {

	// if no card, then return
	if (handdeck->top == NULL) {
		return;
	}

	// if only one card in the deck, move_to_bottom is already done
	if (handdeck->top->next == NULL) {
		return;
	}

	// update bottom card's next from nullptr to top (the new bottom)
	handdeck->bottom->next = handdeck->top;

	// update the top and the bottom of the deck
	handdeck->bottom = handdeck->top;
	handdeck->top = handdeck->top->next;
	
	// update the new bottom card's next to be a nullptr instead of pointing to 
	// the 2nd card in the deck
	handdeck->bottom->next = NULL;

}

/*
*	Given two decks, return if they are the equal by looking at their 
*   respective card identities.
*/
int is_equal(deck_t *tabledeck) {
	
	if (tabledeck->top == NULL) {
		return -1;
	}

	card_t *current = tabledeck->top;
	int card_number = tabledeck->num_cards - 1;
	while (current->next != NULL) {
		if (current->identity != card_number) {
			return 0;
		}
		--card_number;
		current = current->next;
	}

	return 1;
}

void play_round(deck_t *handdeck, deck_t *tabledeck) {
	while (handdeck->top != NULL) {
		move_to_top(handdeck, tabledeck);
		move_to_bottom(handdeck);
	}
}

/*
*	Print function for a deck. Iterate through the cards 
*	in the deck, and print the identity of the cards to stdout
*/
void print(deck_t *deck) {
	
	card_t *current = deck->top;
	
	if (current == NULL)
		return;

	printf("%d ->", current->identity);

	while (current->next != NULL) {
		current = current->next;
		printf(" %d ->", current->identity);
	}

	printf("\n");

	return;
}

/*
*	Print function for a card so that top and bottom can easily be printed.
*/
void print_card(card_t *card) {
	if (card == NULL) {
		return;
	}
	printf("%d\n", card->identity);
	return;
}

int main(void) {

	int num_cards = 10;
	
	// make new deck and print it
	deck_t* handdeck = make_deck(num_cards);
	print(handdeck);

	// initialize empty table deck
	deck_t *tabledeck = (deck_t *)malloc(sizeof(deck_t));
	tabledeck->num_cards = num_cards;
	tabledeck->top = NULL;
	tabledeck->bottom = NULL;

	// play the game
	int num_rounds = 0;
	while (1) {
		play_round(handdeck, tabledeck);
		printf("table deck = ");
		print(tabledeck);
		// hand deck will get table deck as hand deck should be null after 
		// a round has been played
		handdeck->top = tabledeck->top;
		handdeck->bottom = tabledeck->bottom;

		// table deck is an empty deck again
		tabledeck->top = NULL;
		tabledeck->bottom = NULL;

		++num_rounds;
		if (is_equal(handdeck)) {
			break;
		}
	}
	printf("Number of rounds played = %d\n", num_rounds);


	return 1;
}