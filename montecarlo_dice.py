#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:09:05 2019

Alice wants to join her school's Probability Student Club. Membership dues
are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five
followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed
by a five.

Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value.

@author: carlgval
"""

from random import randint


def dice_game(*stop_condition):
    ''' Simulate a dice game.

    Given a set of stop conditions, this method returns the number of
    iterations (dice throws) needed to reach them.

    Args:
        *stop_condition: Variable length argument list. List of ints with the
            stop conditions
    Return:
        (int): Number of throws needed.

    '''
    n_conditions = len(stop_condition)

    n_throws = n_conditions

    dice = [randint(1, 6) for _ in range(n_conditions)]

    while not all([a == b for a, b in zip(dice, stop_condition)]):
        dice.pop(0)
        dice.append(randint(1, 6))
        n_throws += 1

    return n_throws


# Test
if __name__ == '__main__':
    n = 10000

    games_1 = [dice_game(5, 6) for i in range(n)]
    games_2 = [dice_game(5, 5) for i in range(n)]

    mean_1 = float(sum(games_1)) / len(games_1)
    mean_2 = float(sum(games_2)) / len(games_2)

    print('Mean throws for 5-6: %.2f. Mean throws for 5-5: %.2f' %
          (mean_1, mean_2))
