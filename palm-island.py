'''
Palm Island Analyzer

This code is intended to given a randon deck shuffle of Palm Island
generate all the possible games and its points.
'''


ACT_LVL_UP = 'ACT_LVL_UP'
ACT_TO_LVL1 = 'ACT_TO_LVL1'
ACT_TO_LVL2 = 'ACT_TO_LVL2'
ACT_TO_LVL2 = 'ACT_TO_LVL3'
ACT_TO_LVL2 = 'ACT_TO_LVL4'
ACT_TO_HAND = 'ACT_TO_HAND'


class Resource():

    def __init__(self, wood, fish, stone):
        self.wood = wood
        self.fish = fish
        self.stone = stone


class Action():

    def __init__(self, cost, action):
        self.cost = cost
        self.action


class Card():

    def __init__(self, id, name, levels):
        self.id = id
        self.name = name
        self.levels = levels
        self.level_idx = 0


class CardLevel():

    def __init__(self, value, actions, vp):
        self.value = value
        self.actions = actions
        self.vp = vp


class Player():

    def __init__(self, deck):
        self.deck = deck



class PalmIsland():

    def __init__(self):
        self.deck = {}


