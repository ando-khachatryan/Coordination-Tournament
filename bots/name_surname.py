import numpy as np


def strategy(my_moves: list, op_moves: list, payoffs: dict):
    """

    :param my_moves: list of what we have played in proceeding rounds
    :param op_moves: list of what our opponent has played in proceeding rounds
    :param payoffs: dictionary containing the payoff matrix.
            payoffs['UD'] is the payoff for P1 when P1 plays 'U' and P2 plays 'D'
    :return: 'U' or 'D'
    """
    UU = payoffs['UU']
    UD = payoffs['UD']
    DU = payoffs['DU']
    DD = payoffs['DD']


    flip = np.random.rand()
    if flip > 0.5:
        return 'U'
    else:
        return 'D'
