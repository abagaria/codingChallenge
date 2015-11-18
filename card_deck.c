#import "card_deck.h"

deck_t make_deck(int num_cards) {
	deck_t deck;
	return deck;
}

void move_to_top(deck_t *handdeck, deck_t *tabledeck) {
	return;
}

void move_to_bottom(deck_t *handdeck) {
	return;
}

int is_equal(deck_t original_deck, deck_t tabledeck) {
	return 1;
}

void play_round(deck_t *handdeck, deck_t *tabledeck) {
	return;
}

/*
*	Print function for a deck. Iterate through the cards 
*	in the deck, and print the identity of the cards to stdout
*/
void print(deck_t deck) {
	card_t *current = deck.top;
	
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
	// make 2 cards, one on top of each other
	card_t topcard;
	topcard.identity = 1;

	card_t nextcard;
	nextcard.identity = 2;

	topcard.next = &nextcard;
	nextcard.next = NULL;

	// create deck from the 2 cards above
	deck_t deck;
	deck.num_cards = 2;
	deck.top = &topcard;
	deck.bottom = &nextcard;

	// print this deck
	print(deck);

	return 1;
}