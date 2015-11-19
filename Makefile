# Author: Akhil Bagaria
# Date: November 18th, 2015
# Makefile for coding challenge cards question

CC = gcc
CFLAGS = -Wall

all: card_deck

card_deck: card_deck.o
	$(CC) $(CFLAGS) -o card_deck card_deck.o

card_deck.o: card_deck.h card_deck.c
	$(CC) $(CFLAGS) -c -O -g card_deck.c

clean:
	rm card_deck.o
	rm card_deck