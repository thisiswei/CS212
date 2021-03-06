# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

MY_DECK = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=MY_DECK):
    # Your code here.
    random.shuffle(deck)
    return [deck[i*n:(i+1)*5] for i in range(numhands)]

# Write a function, allmax(iterable, key=None), that returns
# a list of all items equal to the max of the iterable,
# according to the function specified by key.

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    to_return = []
    key = key or (lambda x: x)
    max_val = key(max(iterable, key=key))
    [to_return.append(i) for i in iterable if key(i) == max_val]
    return to_return

def weird_all_max_from_forum(iterable, key=None):
    max_val = map(key , max(iterable, key=key))
    return [item for val, item in zip(map(key, iterable), iterable)
            if val == max_val]

def hand_rank(hand):
    ranks = card_ranks(hand)
    return ((8, max(ranks)) if stright(ranks) and flush(hand) else
            (7, kind(4, ranks), kind(1, ranks)) if kind(4, ranks) else
            (6, kind(3, ranks), kind(2, ranks)) if kind(3, ranks) and kind(2, ranks) else
            (5, ranks) if flush(hand) else
            (4, max(ranks)) if stright(ranks) else
            (3, kind(3, ranks), ranks) if kind(3, ranks) else
            (2, two_pair(2, ranks), ranks) if two_pair else
            (1, kind(2, ranks), ranks) if kind(2, ranks) else
            (0, ranks))

def better_hand_rank(hand):
    group = groupit([r for r, s in hand])
    counts, ranks = zip(*group)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    is_straight = stright(ranks)
    is_flush = flush(hand)
    return ((8 if is_straight and is_flush else
             7 if counts == (4, 1) else
             6 if counts == (3, 2) else
             5 if is_straight else
             4 if is_flush else
             3 if counts == (2, 2) else
             2 if counts == (2, 1, 1, 1) else
             0), ranks)

def groupit(ranks):
    ranks = sorted(set(ranks), reverse=True)
    return [(ranks.count(r), r) for r in ranks]

# Define a function, two_pair(ranks).
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    high, low = kind(2, ranks), kind(2, ranks[::-1])
    return (high, low) if high != low else None

def flush(hand):
    return len(set([s for r, s in hand])) == 1

def stright(ranks):
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the
    """
    #Your code here
    return next((r for r in ranks if ranks.count(r) == n), None)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

def test():
    "Test cases for the functions in poker program."
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fkranks = card_ranks(fk)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    print 'tests pass'

def test_allmax():
    hands = [['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD'], ['9D', '9H', '9S', '9C', '7D'], ['TD', 'TC', 'TH', '7C', '7D']]
    assert allmax(hands, hand_rank) == hands[:2]

def main():
    test()
    test_allmax()

if __name__ == '__main__':
    exit(main())
