# Deck Shuffler
# Creates a fresh deck of cards;
# Shuffles deck of cards;
# Compares shuffled deck with decks already stored in shuffleddecksofcards.txt;
# Saves shuffled deck to shuffleddecksofcards.txt on a new line;
# Saves any individual matched cards to cardmatches.csv;
# Saves any whole deck matches to deckmatches.txt (lol);
# ver1

import random, csv, sys

# Generates a list of unshuffled Deck of Cards

class deck_builder:
    card_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    card_suite = ["H","D","S","C"]
    card_deck = []

    for suites in range(0, len(card_suite)):
        for numbers in range(0, len(card_number)):
            card_deck.append(card_suite[suites]+card_number[numbers])

# Use deck_builder.card_deck to shuffle a new deck of cards

def shuffler(deck):
    random.shuffle(deck)

    comparer(deck) # Uses shuffled deck in comparer

# Stores deck, a list, on a new line in shuffleddecksofcards.txt

def storer(deck):
    with open("shuffleddecksofcards.txt","a") as card_deck_shuffled_storage:
        for card in range(0, len(deck)):
            card_deck_shuffled_storage.write(deck[card])

            if card != (len(deck)-1):
                card_deck_shuffled_storage.write(",")

            else:
                card_deck_shuffled_storage.write("\n")

# Compares deck, a list, to each line in shuffleddecsofcards.txt
            # Stores deck, a list, if there is a match to deckmatches.txt (lol)
            # When a card from deck matches a card from a stored deck,
            # it will be noted by the card position and card value in the
            # file cardmatches.csv for future analysis.

def comparer(deck):
    deck_match = True
    with open("shuffleddecksofcards.txt","r") as deck_shuffled_storage:
        for line in deck_shuffled_storage:

            # Gets stored shuffled decks one at a time from
                        # shuffleddecksofcards.txt and formats for use
            stored_curr_deck = line
            stored_curr_deck = stored_curr_deck.split(",")
            stored_curr_deck[-1] = str(stored_curr_deck[-1]).rstrip("\n")

            # Placeholder to test for positives: deck = stored_curr_deck

            # Compares each card in current deck and compares to stored decks
            count = 1
            for card in range(0, len(deck)):
                if deck[card] != stored_curr_deck[card]:
                    deck_match = False
                else:
                    with open("cardmatches.csv", "a", newline='') as cardmatches:
                        csv.writer(cardmatches).writerow([str(card+1), str(deck[card])])
                count += 1

            #Checks if all cards match and stores deck in deckmatches.txt
            if deck_match == True:
                print("Two deck shuffles have matched!")
                with open("deckmatches.txt", "a") as deckmatches:
                    deckmatches.write(str(deck)+"\n")
            else:
                pass

    # Gives user feedback and resets deck_match
    if deck_match == False:
        print("No matches for that deck.")
        deck_match == True

    storer(deck) # Stores the shuffled deck.

# Gets user input and starts everything up

def initialize():
    print("How many times should I run? (0 to quit!)")
    x = input()
    print("\n"+"\n")
    if x == "0":
        print("All done! Thank you!")
        print("\n"+"\n")
        sys.exit(0)

    elif x.isdigit():
        x = int(x)
        for runtimes in range(0,x):
            print(str(runtimes+1) + " decks have been shuffled so far.")
            shuffler(deck_builder.card_deck)
        print(str(x)+ " decks were shuffled and checked."+"\n \n")

    else:
        print("Not a valid input!")

    initialize()

initialize()
