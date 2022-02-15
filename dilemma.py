# ITERATED PRISONER'S DILEMMA
# February 2022
# Olga Koldachenko
#
# ARGUMENTS FORMAT:
# python dilemma.py num_rounds p1_strategy p2_strategy
# - defaults to 5 rs rs
# 
# STRATEGIES:
# tft  = tit for tat
# coop = always cooperate (stay silent)
# comp = always compete (betray)
# rc = random choice
# rs = random strategy (defaults to this with invalid string)

from server import DilemmaServer
from prisoner import Prisoner
import strategy
import sys

if __name__ == "__main__":

    address = ('localhost', 6000)
    
    num_rounds = 5
    s1 = strategy.random_strat()
    s2 = strategy.random_strat()

    try:
        num_rounds = int(sys.argv[1])
        s1 = strategy.string_to_strat(sys.argv[2])
        s2 = strategy.string_to_strat(sys.argv[3])
    except:
        pass

    w = DilemmaServer(address, num_rounds)
    p1 = Prisoner(address, s1)
    p2 = Prisoner(address, s2)

    w.start()
    p1.start()
    p2.start()

    w.join()
    p1.join()
    p2.join()