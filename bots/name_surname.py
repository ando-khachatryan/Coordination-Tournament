"""
This is demo of how to implement a strategy.
Note that this strategy is not good -- in fact, it is pretty bad.
The purpose is to demonstrate some language constructs in python,
because some of the students have never used it.
"""
import numpy as np


def strategy(my_moves: list, op_moves: list, payoffs: dict):
    """
    :param my_moves: list of what we have played in proceeding rounds
    :param op_moves: list of what our opponent has played in proceeding rounds
    :param payoffs: dictionary containing the payoff matrix.
            payoffs['UD'] is the payoff for P1 when P1 plays 'U' and P2 plays 'D'
    :return: 'U' or 'D', which is your strategy

    Note: to get the number of the current round, use len(my_moves) + 1.
    """

    uu = payoffs['UU']  # this is the payoff of P1 when P1 plays 'U' and P2 plays 'U' This is going to be 0
    ud = payoffs['UD']  # this is the payoff of P1 when P1 plays 'U' and P2 plays 'D'.
    du = payoffs['DU']  # this is the payoff of P1 when P1 plays 'D' and P2 plays 'U'.
    dd = payoffs['DD']  # this is the payoff of P1 when P1 plays 'D' and P2 plays 'D'. This is going to be 0

    if len(my_moves) == 0:
        # this means we are at the very first round
        return 'U'

    if len(my_moves) > 50:
        # after round 50 our strategy always returns 'D'
        return 'D'

    uu_count = 0
    ud_count = 0
    du_count = 0
    dd_count = 0

    for i in range(len(my_moves)):
        if my_moves[i] == 'U' and op_moves[i] == 'U':
            uu_count += 1
        elif my_moves[i] == 'U' and op_moves[i] == 'D':
            ud_count += 1
        elif my_moves[i] == 'D' and op_moves[i] == 'U':
            du_count += 1
        else:  # when my_moves[i] == 'D' and op_moves[i] == 'D'
            dd_count += 1

    my_score = ud_count * ud + du_count * du  # this is because uu == dd == 0

    # use the symmetry of the payoff matrix to calculate our opponent's payoff
    op_score = ud_count * du + du_count * ud

    # now, we play 'U' with probability my_score/(my_score + op_score)
    # again, we are not suggesting that it is a good idea to do this,
    # we just want to demonstrate how to play a randomized strategy

    # first, check that if (my_score + op_score) is not 0.
    if my_score + op_score == 0:
        return 'U'

    flip = np.random.rand()  # first, generate a uniform random number from [0, 1)
    if flip < my_score/(my_score + op_score):
        return 'U'  # play 'U' if the number is between 0 and my_score/(my_score + op_score)
    else:
        return 'D'  # play 'D' otherwise
