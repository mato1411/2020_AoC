# --- Day 22: Crab Combat ---
# It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of space cards! You'd like to play a game of Combat, and there's even an opponent available: a small crab that climbed aboard your raft before you left.
#
# Fortunately, it doesn't take long to teach the crab the rules.
#
# Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of rounds: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.
#
# For example, consider the following starting decks:
#
# Player 1:
# 9
# 2
# 6
# 3
# 1
#
# Player 2:
# 5
# 8
# 4
# 7
# 10
# This arrangement means that player 1's deck contains 5 cards, with 9 on top and 1 on the bottom; player 2's deck also contains 5 cards, with 5 on top and 10 on the bottom.
#
# The first round begins with both players drawing the top card of their decks: 9 and 5. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that 9 is above 5. In total, it takes 29 rounds before a player has all of the cards:
#
# -- Round 1 --
# Player 1's deck: 9, 2, 6, 3, 1
# Player 2's deck: 5, 8, 4, 7, 10
# Player 1 plays: 9
# Player 2 plays: 5
# Player 1 wins the round!
#
# -- Round 2 --
# Player 1's deck: 2, 6, 3, 1, 9, 5
# Player 2's deck: 8, 4, 7, 10
# Player 1 plays: 2
# Player 2 plays: 8
# Player 2 wins the round!
#
# -- Round 3 --
# Player 1's deck: 6, 3, 1, 9, 5
# Player 2's deck: 4, 7, 10, 8, 2
# Player 1 plays: 6
# Player 2 plays: 4
# Player 1 wins the round!
#
# -- Round 4 --
# Player 1's deck: 3, 1, 9, 5, 6, 4
# Player 2's deck: 7, 10, 8, 2
# Player 1 plays: 3
# Player 2 plays: 7
# Player 2 wins the round!
#
# -- Round 5 --
# Player 1's deck: 1, 9, 5, 6, 4
# Player 2's deck: 10, 8, 2, 7, 3
# Player 1 plays: 1
# Player 2 plays: 10
# Player 2 wins the round!
#
# ...several more rounds pass...
#
# -- Round 27 --
# Player 1's deck: 5, 4, 1
# Player 2's deck: 8, 9, 7, 3, 2, 10, 6
# Player 1 plays: 5
# Player 2 plays: 8
# Player 2 wins the round!
#
# -- Round 28 --
# Player 1's deck: 4, 1
# Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
# Player 1 plays: 4
# Player 2 plays: 9
# Player 2 wins the round!
#
# -- Round 29 --
# Player 1's deck: 1
# Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
# Player 1 plays: 1
# Player 2 plays: 7
# Player 2 wins the round!
#
#
# == Post-game results ==
# Player 1's deck:
# Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1
# Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:
#
#    3 * 10
# +  2 *  9
# + 10 *  8
# +  6 *  7
# +  8 *  6
# +  5 *  5
# +  9 *  4
# +  4 *  3
# +  7 *  2
# +  1 *  1
# = 306
# So, once the game ends, the winning player's score is 306.
#
# Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?
#
# Your puzzle answer was 30138.
#
# --- Part Two ---
# You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of Recursive Combat.
#
# Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of rounds with a few changes:
#
# Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
# Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
# If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
# Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.
# As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again so that the winner's card is above the other card). Note that the winner's card might be the lower-valued of the two cards if they won the round due to winning a sub-game. If collecting cards by winning the round causes a player to have all of the cards, they win, and the game ends.
#
# Here is an example of a small game that would loop forever without the infinite game prevention rule:
#
# Player 1:
# 43
# 19
#
# Player 2:
# 2
# 29
# 14
# During a round of Recursive Combat, if both players have at least as many cards in their own decks as the number on the card they just dealt, the winner of the round is determined by recursing into a sub-game of Recursive Combat. (For example, if player 1 draws the 3 card, and player 2 draws the 7 card, this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left, not counting the 3 and 7 cards that were drawn.)
#
# To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be copies of the next three cards in their deck.)
#
# Here is a complete example of gameplay, where Game 1 is the primary game of Recursive Combat:
#
# === Game 1 ===
#
# -- Round 1 (Game 1) --
# Player 1's deck: 9, 2, 6, 3, 1
# Player 2's deck: 5, 8, 4, 7, 10
# Player 1 plays: 9
# Player 2 plays: 5
# Player 1 wins round 1 of game 1!
#
# -- Round 2 (Game 1) --
# Player 1's deck: 2, 6, 3, 1, 9, 5
# Player 2's deck: 8, 4, 7, 10
# Player 1 plays: 2
# Player 2 plays: 8
# Player 2 wins round 2 of game 1!
#
# -- Round 3 (Game 1) --
# Player 1's deck: 6, 3, 1, 9, 5
# Player 2's deck: 4, 7, 10, 8, 2
# Player 1 plays: 6
# Player 2 plays: 4
# Player 1 wins round 3 of game 1!
#
# -- Round 4 (Game 1) --
# Player 1's deck: 3, 1, 9, 5, 6, 4
# Player 2's deck: 7, 10, 8, 2
# Player 1 plays: 3
# Player 2 plays: 7
# Player 2 wins round 4 of game 1!
#
# -- Round 5 (Game 1) --
# Player 1's deck: 1, 9, 5, 6, 4
# Player 2's deck: 10, 8, 2, 7, 3
# Player 1 plays: 1
# Player 2 plays: 10
# Player 2 wins round 5 of game 1!
#
# -- Round 6 (Game 1) --
# Player 1's deck: 9, 5, 6, 4
# Player 2's deck: 8, 2, 7, 3, 10, 1
# Player 1 plays: 9
# Player 2 plays: 8
# Player 1 wins round 6 of game 1!
#
# -- Round 7 (Game 1) --
# Player 1's deck: 5, 6, 4, 9, 8
# Player 2's deck: 2, 7, 3, 10, 1
# Player 1 plays: 5
# Player 2 plays: 2
# Player 1 wins round 7 of game 1!
#
# -- Round 8 (Game 1) --
# Player 1's deck: 6, 4, 9, 8, 5, 2
# Player 2's deck: 7, 3, 10, 1
# Player 1 plays: 6
# Player 2 plays: 7
# Player 2 wins round 8 of game 1!
#
# -- Round 9 (Game 1) --
# Player 1's deck: 4, 9, 8, 5, 2
# Player 2's deck: 3, 10, 1, 7, 6
# Player 1 plays: 4
# Player 2 plays: 3
# Playing a sub-game to determine the winner...
#
# === Game 2 ===
#
# -- Round 1 (Game 2) --
# Player 1's deck: 9, 8, 5, 2
# Player 2's deck: 10, 1, 7
# Player 1 plays: 9
# Player 2 plays: 10
# Player 2 wins round 1 of game 2!
#
# -- Round 2 (Game 2) --
# Player 1's deck: 8, 5, 2
# Player 2's deck: 1, 7, 10, 9
# Player 1 plays: 8
# Player 2 plays: 1
# Player 1 wins round 2 of game 2!
#
# -- Round 3 (Game 2) --
# Player 1's deck: 5, 2, 8, 1
# Player 2's deck: 7, 10, 9
# Player 1 plays: 5
# Player 2 plays: 7
# Player 2 wins round 3 of game 2!
#
# -- Round 4 (Game 2) --
# Player 1's deck: 2, 8, 1
# Player 2's deck: 10, 9, 7, 5
# Player 1 plays: 2
# Player 2 plays: 10
# Player 2 wins round 4 of game 2!
#
# -- Round 5 (Game 2) --
# Player 1's deck: 8, 1
# Player 2's deck: 9, 7, 5, 10, 2
# Player 1 plays: 8
# Player 2 plays: 9
# Player 2 wins round 5 of game 2!
#
# -- Round 6 (Game 2) --
# Player 1's deck: 1
# Player 2's deck: 7, 5, 10, 2, 9, 8
# Player 1 plays: 1
# Player 2 plays: 7
# Player 2 wins round 6 of game 2!
# The winner of game 2 is player 2!
#
# ...anyway, back to game 1.
# Player 2 wins round 9 of game 1!
#
# -- Round 10 (Game 1) --
# Player 1's deck: 9, 8, 5, 2
# Player 2's deck: 10, 1, 7, 6, 3, 4
# Player 1 plays: 9
# Player 2 plays: 10
# Player 2 wins round 10 of game 1!
#
# -- Round 11 (Game 1) --
# Player 1's deck: 8, 5, 2
# Player 2's deck: 1, 7, 6, 3, 4, 10, 9
# Player 1 plays: 8
# Player 2 plays: 1
# Player 1 wins round 11 of game 1!
#
# -- Round 12 (Game 1) --
# Player 1's deck: 5, 2, 8, 1
# Player 2's deck: 7, 6, 3, 4, 10, 9
# Player 1 plays: 5
# Player 2 plays: 7
# Player 2 wins round 12 of game 1!
#
# -- Round 13 (Game 1) --
# Player 1's deck: 2, 8, 1
# Player 2's deck: 6, 3, 4, 10, 9, 7, 5
# Player 1 plays: 2
# Player 2 plays: 6
# Playing a sub-game to determine the winner...
#
# === Game 3 ===
#
# -- Round 1 (Game 3) --
# Player 1's deck: 8, 1
# Player 2's deck: 3, 4, 10, 9, 7, 5
# Player 1 plays: 8
# Player 2 plays: 3
# Player 1 wins round 1 of game 3!
#
# -- Round 2 (Game 3) --
# Player 1's deck: 1, 8, 3
# Player 2's deck: 4, 10, 9, 7, 5
# Player 1 plays: 1
# Player 2 plays: 4
# Playing a sub-game to determine the winner...
#
# === Game 4 ===
#
# -- Round 1 (Game 4) --
# Player 1's deck: 8
# Player 2's deck: 10, 9, 7, 5
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 1 of game 4!
# The winner of game 4 is player 2!
#
# ...anyway, back to game 3.
# Player 2 wins round 2 of game 3!
#
# -- Round 3 (Game 3) --
# Player 1's deck: 8, 3
# Player 2's deck: 10, 9, 7, 5, 4, 1
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 3 of game 3!
#
# -- Round 4 (Game 3) --
# Player 1's deck: 3
# Player 2's deck: 9, 7, 5, 4, 1, 10, 8
# Player 1 plays: 3
# Player 2 plays: 9
# Player 2 wins round 4 of game 3!
# The winner of game 3 is player 2!
#
# ...anyway, back to game 1.
# Player 2 wins round 13 of game 1!
#
# -- Round 14 (Game 1) --
# Player 1's deck: 8, 1
# Player 2's deck: 3, 4, 10, 9, 7, 5, 6, 2
# Player 1 plays: 8
# Player 2 plays: 3
# Player 1 wins round 14 of game 1!
#
# -- Round 15 (Game 1) --
# Player 1's deck: 1, 8, 3
# Player 2's deck: 4, 10, 9, 7, 5, 6, 2
# Player 1 plays: 1
# Player 2 plays: 4
# Playing a sub-game to determine the winner...
#
# === Game 5 ===
#
# -- Round 1 (Game 5) --
# Player 1's deck: 8
# Player 2's deck: 10, 9, 7, 5
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 1 of game 5!
# The winner of game 5 is player 2!
#
# ...anyway, back to game 1.
# Player 2 wins round 15 of game 1!
#
# -- Round 16 (Game 1) --
# Player 1's deck: 8, 3
# Player 2's deck: 10, 9, 7, 5, 6, 2, 4, 1
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 16 of game 1!
#
# -- Round 17 (Game 1) --
# Player 1's deck: 3
# Player 2's deck: 9, 7, 5, 6, 2, 4, 1, 10, 8
# Player 1 plays: 3
# Player 2 plays: 9
# Player 2 wins round 17 of game 1!
# The winner of game 1 is player 2!
#
#
# == Post-game results ==
# Player 1's deck:
# Player 2's deck: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3
# After the game, the winning player's score is calculated from the cards they have in their original deck using the same rules as regular Combat. In the above game, the winning player's score is 291.
#
# Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same two decks as before. What is the winning player's score?
#
# Your puzzle answer was 31587.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import copy
from pprint import pprint


def play_game_p2(game):

    game_count = 0
    both_player_have_cards = True

    game_state = copy.deepcopy(game)
    rounds_card_decks = [game_state]
    game_count += 1
    game_round = 0

    while both_player_have_cards:

        game_round += 1

        # Before either player deals a card, if there was a previous round in this game that had exactly the same
        # cards in the same order in the same players' decks, the game instantly ends in a win for player 1.
        # Previous rounds from other games are not considered. (This prevents infinite games of
        # Recursive Combat, which everyone agrees is a bad idea.)

        if game_round > 1:
            for r in range(len(rounds_card_decks)-1):
                for k, v in rounds_card_decks[r].items():
                    if game[k] == v:
                        # Player 1 wins
                        return 1

        print("Game: {}, Round: {}".format(game_count, game_round))
        top_cards = {}
        top_card = 0
        player_with_highest_card = ""
        for k, v in game.items():
            print("Player: {}, Top card: {}".format(k, v[0]))
            if v[0] > top_card:
                top_card = v[0]
                player_with_highest_card = k

            top_cards[k] = v[0]

        # start recursive game:
        # if for both players the top card value <= number of remaining cards -1 (current top card does not count)
        play_recursive_sub_game = []
        for k, v in top_cards.items():
            if v <= len(game[k]) - 1:
                play_recursive_sub_game.append(True)
            else:
                play_recursive_sub_game.append(False)

        if all(play_recursive_sub_game):
            print("Playing a sub-game to determine the winner...")
            # Generate new game dictionary
            sub_game = {}
            print(top_cards)
            print(game)
            for k, v in game.items():
                sub_game[k] = v[1:top_cards[k] + 1]

            print("sub_game: ", sub_game)
            player_with_highest_card = play_game_p2(sub_game)

        print("Player {} wins game {} round {}!".format(player_with_highest_card, game_count, game_round))

        player_that_lost = int([p for p in game.keys() if p != player_with_highest_card][0])

        game[player_with_highest_card].append(game[player_with_highest_card].pop(0))
        game[player_with_highest_card].append(game[player_that_lost].pop(0))

        for k, v in game.items():
            print("Cards of player {}: {}".format(k, v))
            if len(v) == 0:
                both_player_have_cards = False
                player_that_lost = k
                print("Player {} wins the game {}!".format(k, game_count))

        # Save game state to prevent infinite recursion loop
        rounds_card_decks.append(copy.deepcopy(game))

    # player_that_won
    return int([p for p in game.keys() if p != player_that_lost][0])


if __name__ == '__main__':

    files = ['20201222-example.txt', '20201222-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        game_start = {}

        # Read player decks
        for i in range(len(lines)):

            line = lines[i].strip()

            # New tile
            if line.startswith("Player"):
                cards = []
                id = int(line.split()[1].split(":")[0].strip())
                continue

            # Player done
            if line == "":
                game_start[id] = cards
                number_of_cards_per_player = len(cards)
                continue

            cards.append(int(line))

        print("game_start:")
        pprint(game_start)

        number_of_cards = len(game_start) * number_of_cards_per_player

        print("number_of_cards: ", number_of_cards)

        print("\nPart One")

        both_player_have_cards = True
        round = 0

        part_one = copy.deepcopy(game_start)

        while both_player_have_cards:
            round += 1
            print("Round: ", round)
            top_card = 0
            player_with_highest_card = ""
            for k, v in part_one.items():
                print("Player: {}, Top card: {}".format(k, v[0]))
                if v[0] > top_card:
                    top_card = v[0]
                    player_with_highest_card = k

            print("Player {} wins!".format(player_with_highest_card))

            player_that_lost = int([p for p in part_one.keys() if p != player_with_highest_card][0])

            part_one[player_with_highest_card].append(part_one[player_with_highest_card].pop(0))
            part_one[player_with_highest_card].append(part_one[player_that_lost].pop(0))

            for k, v in part_one.items():
                print("Cards of player {}: {}".format(k, v))
                if len(v) == 0:
                    both_player_have_cards = False
                    player_that_lost = k
                    print("Player {} wins the game! Game over".format(k))

        player_that_won = int([p for p in part_one.keys() if p != player_that_lost][0])

        score = 0

        part_one[player_that_won].reverse()
        for e, c in enumerate(part_one[player_that_won]):
            score += (e+1)*c

        print("Part One Score: ", score)

        print("\nPart Two")

        part_two = copy.deepcopy(game_start)

        player_that_won = play_game_p2(part_two)

        score = 0

        part_two[player_that_won].reverse()
        for e, c in enumerate(part_two[player_that_won]):
            score += (e + 1) * c

        print("Part Two Score: ", score)
