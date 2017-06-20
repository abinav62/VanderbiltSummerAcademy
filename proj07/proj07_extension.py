from proj07 import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score,
	and return it. This word should be calculated by considering all possible
	permutations of lengths 1 to HAND_SIZE.
    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    valid_word_list = []
    perm =  get_perms(hand, HAND_SIZE)
    print "Generating answers..."
    for word in perm:
        if is_valid_word(word, hand, word_list):
            valid_word_list.append(word)
    random_word = random,choice()

    print valid_word_list
    print random_word
comp_choose_word(deal_hand(HAND_SIZE), load_words())
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:
     * The hand is displayed.
     * The computer chooses a word using comp_choose_words(hand, word_dict).
     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.
     * The sum of the word scores is displayed when the hand finishes.
     * The hand finishes when the computer has exhausted its possible choices
        (i.e. comp_play_hand returns None).
     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    display_hand(hand)
    comp_choose_word(hand, word_dict)


#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.
    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand
        (created above).
    * If the user inputs anything else, ask them again.
    3) After the computer or user has played the hand, repeat from step 1
    word_list: list (string)
    """
    # TO DO...
    n = HAND_SIZE
    hand = {}
    order = raw_input('Type u if you want to go first, or type c if you want the computer to go first.'
    if order == 'u':
        while True:  # ?
            cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
            if cmd == 'r':
                if not hand:
                    print 'You have not played a hand yet. Please play a new hand first!'
                else:
                    play_hand(hand, load_words())
            elif cmd == 'n':
                hand = deal_hand(n)
                play_hand(hand, load_words())
            elif cmd == 'e':
                break
            else:
                print 'Invalid command.'
    elif order == 'c':
        comp_play_hand(hand, word_list)
    else:
        print "Invalid command."
    if get_word_score(comp_play_hand(hand, word_list), n) > get_word_score(play_hand(hand, word_list), n):
        print "The computer wins!"
    elif get_word_score(play_hand(hand, word_list), n) > get_word_score(comp_play_hand(hand, word_list), n)
        print "You won!"
    else:
        print "Wow! It's a tie!"
        
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
