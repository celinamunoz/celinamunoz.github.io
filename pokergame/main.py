"""
Created: Celina Munoz
Project 3: Objectively, How does it Rank?
Due Monday May 25, 2018

I affirm that I have carried out the attached academic endeavors with full academic honesty, in
accordance with the Union College Honor Code and the course syllabus
"""


# from card import *
# from deck import *
# from poker_hand import *
# from community_card_set import *
# from stud_poker_hand import *

def oldPokergame():
    standard_deck = Deck()
    standard_deck.shuffle()
    player_points=0
    while standard_deck.size()>2:
        cards_in_hand_a= PokerHand(standard_deck,5)
        cards_in_hand_b = PokerHand(standard_deck, 5)
        print("Here are two hands:","\n", "Hand A:",cards_in_hand_a,"\n","Hand B:", cards_in_hand_b)
        print("If hand A is better than hand B, insert 1")
        print("If hand A is worse than hand B, insert -1")
        print("If hand A is the same as hand B, insert 0")
        user_answer=input("Please Enter Your Answer Here!")
        user_answer=int(user_answer)

        if user_answer==cards_in_hand_a.compare_to(cards_in_hand_b):
            player_points+=1
            print("Total Score:", player_points, "\n")
        elif user_answer != cards_in_hand_a.compare_to(cards_in_hand_b):
            print("Game Over! Bye")
            print("Total Score:",player_points)
            break
        else:
            print("ERROR, try again")

    print("The deck is done! Good Game!")
    print("Total Cumulative Score:",player_points)


def newPokergame():
    standard_deck = Deck()
    standard_deck.shuffle()
    game_over = False
    player_points=0

    while standard_deck.size()>7and not game_over:
        community_cards = CommunityCardSet(standard_deck)
        hole_carda= StudPokerHand(standard_deck,community_cards)
        hole_cardb = StudPokerHand(standard_deck, community_cards)
        print("The community cards are: \n", community_cards)
        print("Which of the following hands is worth more?")
        print("Hand a: \n", hole_carda)
        print("  or")
        print("Hand b: \n", hole_cardb, "\n")

        #print(hole_carda.stud_compare_to(hole_cardb))
        print("If hand a is better than hand b, insert 1")
        print("If hand a is worse than hand b, insert -1")
        print("If hand a is the same as hand b, insert 0")

        user_answer=input("Please Enter Your Answer Here!")
        user_answer=int(user_answer)

        if user_answer== (hole_carda.stud_compare_to(hole_cardb)):
            player_points+=1
            print("Total Score:", player_points, "\n")
        elif user_answer !=  (hole_carda.stud_compare_to(hole_cardb)):
            print("Game Over! Bye")
            print("Total Score:",player_points)
            game_over=True
        else:
            print("ERROR, try again")

    print("The deck is done! Good Game!")
    print("Total Cumulative Score:",player_points)


if __name__ == '__main__':
    newPokergame()
