import os
import argparse
from importlib import import_module
import inspect

def find_bots():
    """
    Find bot files, and the methods which should play the game
    :return:
    """
    bot_dir = 'bots'
    bot_files = [f for f in os.listdir(os.path.join('.', bot_dir)) if f.endswith('.py')]
    bots = []
    names = []
    is_valid_method = lambda obj: inspect.isfunction(obj) and obj.__name__ == 'strategy'
    #is_valid_method = lambda obj: inspect.isfunction(obj)
    for bot_file in bot_files:
        bot_without_ext = bot_file.split('.')[0]  # remove file extension
        mod = import_module('bots.{}'.format(bot_without_ext))
        for name, obj in inspect.getmembers(mod, is_valid_method):
            bots.append(obj)
            names.append(bot_without_ext)

    return names, bots

def run_match(bot1_func, bot2_func, n_rounds, payoffs, verbose = False):
    bot1_plays = []
    bot2_plays = []
    for i in range(n_rounds):
        bot1_play = bot1_func(bot1_plays, bot2_plays, payoffs).upper()
        bot2_play = bot2_func(bot2_plays, bot1_plays, payoffs).upper()
        bot1_plays.append(bot1_play)
        bot2_plays.append(bot2_play)

    return bot1_plays, bot2_plays

def summary(bot1_plays, bot2_plays, payoffs):
    p1_payoff = 0
    p2_payoff = 0
    for s1, s2 in zip(bot1_plays, bot2_plays):
        p1_payoff += payoffs[s1+s2]
        p2_payoff += payoffs[s2+s1]

    return p1_payoff, p2_payoff

def main():
    parser = argparse.ArgumentParser(description='Run the coordination tournament')
    parser.add_argument('--rounds', type=int, default=10, help='Number of rounds per match (default: 10)')
    args = parser.parse_args()

    n_rounds = args.rounds
    payoffs = {'UU': 0, 'UD': 3, 'DU': 1, 'DD': 0}

    names, bots = find_bots()
    print(bots)
    print([func.__name__ for func in bots])
    for i in range(len(bots)):
        for j in range(i+1, len(bots)):
            bot1_plays, bot2_plays = run_match(bots[i], bots[j], n_rounds, payoffs, False)
            print('P1: {} P2: {}'.format(names[i], names[j]))
            print(bot1_plays)
            print(bot2_plays)
            print('payoffs')
            p1_payoff, p2_payoff = summary(bot1_plays, bot2_plays, payoffs)
            print('P1: {} P2: {}'.format(p1_payoff, p2_payoff))
            print()

if __name__ == '__main__':
    main()