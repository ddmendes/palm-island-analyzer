'''
Palm Island Analyzer

This code is intended to given a randon deck shuffle of Palm Island
generate all the possible games and its points.
'''


ACT_LVL_UP = 'ACT_LVL_UP'
ACT_TO_LVL0 = 'ACT_TO_LVL0'
ACT_TO_LVL1 = 'ACT_TO_LVL1'
ACT_TO_LVL2 = 'ACT_TO_LVL2'
ACT_TO_LVL3 = 'ACT_TO_LVL3'
ACT_TO_LVL4 = 'ACT_TO_LVL4'
ACT_TO_LVL5 = 'ACT_TO_LVL5'
ACT_TO_LVL6 = 'ACT_TO_LVL6'
ACT_TO_LVL7 = 'ACT_TO_LVL7'
ACT_TO_HAND = 'ACT_TO_HAND'


class Resource():

    def __init__(self, wood = 0, fish = 0, stone = 0):
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

    def __init__(self, vp, resources, actions):
        self.vp = vp
        self.resources = resources
        self.actions = actions


class Player():

    def __init__(self, deck):
        self.deck = PalmIslandDeck(deck)



class CardPosition():

    def __init__(self, card, nxt = None, last = False):
        self.card = card
        self.nxt = nxt
        self.last = last


class PalmIslandDeck():

    def __init__(self, deckList):
        last = CardPosition(deckList[-1], last = True)
        before = last
        for c in deckList[-2,0]:
            actual = CardPosition(c, before)
            before = actual
        last.nxt = before
        # Last loop iteration let first item on the before pointer
        self.first = before

    
    def first(self):
        return self.first.card


    def second():
        return self.first.nxt.card


def constructDeckList():
    return [
        Card(1, "Canoaria", [
            CardLevel(0, Resource(fish = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(fish = 1), ACT_TO_LVL1), Action(fish = 1, ACT_TO_LVL2)]),
            CardLevel(0, Resource(fish = 2), [Action(Resource(), ACT_TO_HAND), Action(Resource(fish = 1, wood = 1), ACT_TO_LVL3)]),
            CardLevel(0, Resource(wood = 1, fish = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL3)]),
            CardLevel(0, Resource(wood = 1, fish = 2), [Action(Resource(), ACT_TO_HAND)
        ]),
        Card(2, "Canoaria", [
            CardLevel(0, Resource(fish = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(fish = 1), ACT_TO_LVL1), Action(fish = 1, ACT_TO_LVL2)]),
            CardLevel(0, Resource(fish = 2), [Action(Resource(), ACT_TO_HAND), Action(Resource(fish = 1, wood = 1), ACT_TO_LVL3)]),
            CardLevel(0, Resource(wood = 1, fish = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL3)]),
            CardLevel(0, Resource(wood = 1, fish = 2), [Action(Resource(), ACT_TO_HAND)
        ]),
        Card(3, "Canoaria", [
            CardLevel(0, Resource(fish = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(fish = 1), ACT_TO_LVL1), Action(fish = 1, ACT_TO_LVL2)]),
            CardLevel(0, Resource(fish = 2), [Action(Resource(), ACT_TO_HAND), Action(Resource(fish = 1, wood = 1), ACT_TO_LVL3)]),
            CardLevel(0, Resource(wood = 1, fish = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL3)]),
            CardLevel(0, Resource(wood = 1, fish = 2), [Action(Resource(), ACT_TO_HAND)
        ]),
        Card(4, "Madeireira", [
            CardLevel(0, Resource(wood = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL1)]),
            CardLevel(1, Resource(wood = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL2)]),
            CardLevel(2, Resource(wood = 2), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 2, stone = 2), ACT_TO_LVL3)]),
            CardLevel(5, Resource(), [])
        ]),
        Card(5, "Madeireira", [
            CardLevel(0, Resource(wood = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL1)]),
            CardLevel(1, Resource(wood = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL2)]),
            CardLevel(2, Resource(wood = 2), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 2, stone = 2), ACT_TO_LVL3)]),
            CardLevel(5, Resource(), [])
        ]),
        Card(6, "Madeireira", [
            CardLevel(0, Resource(wood = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL1)]),
            CardLevel(1, Resource(wood = 1), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 1, fish = 1), ACT_TO_LVL2)]),
            CardLevel(2, Resource(wood = 2), [Action(Resource(), ACT_TO_HAND), Action(Resource(wood = 2, stone = 2), ACT_TO_LVL3)]),
            CardLevel(5, Resource(), [])
        ])
    ]


if __name__ == '__main__':
