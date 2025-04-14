'''
Palm Island Analyzer

This code is intended to given a randon deck shuffle of Palm Island
generate all the possible games and its points.
'''

KIND_WOOD = "WOOD"
KIND_FISH = "FISH"


class Resource():

    def __init__(self, amount, kind):
        self.amount = amount
        self.kind = kind


class Action():

    def __init__(self, card, cost):
        self.card = card
        self.cost = cost

    def execute(self):
        pass


class Card():

    def __init__(self, id, name, actions, victory_points):
        self.id = id
        self.name = name
        self.level = 0
        self.in_hand = False
        self.victory_points = victory_points

    def _set_actions(self, actions):
        self.actions = actions


class PalmIsland():

    def __init__(self):
        self.deck = {}


