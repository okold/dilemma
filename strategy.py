# ITERATED PRISONER'S DILEMMA - STRATEGIES
# February 2022
# Olga Koldachenko

import random

def random_strat():
    return random.choice((tit_for_tat, always_cooperate, always_compete, random_choice))

def string_to_strat(string):
    if string == "tft":
        return tit_for_tat
    if string == "coop":
        return always_cooperate
    if string == "comp":
        return always_compete
    if string == "rc":
        return random_choice
    else:
        return random_strat()

def tit_for_tat(state):
    if state == None:
        return True
    else:
        return state

def always_cooperate(_):
    return True

def always_compete(_):
    return False

def random_choice(_):
    return random.choice((True, False))