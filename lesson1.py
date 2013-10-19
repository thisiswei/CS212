# Define a function, two_pair(ranks).

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    high, low = kind(2, ranks), kind(2, ranks[::-1])
    return (high, low) if high != low else None


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the
    """
    #Your code here
    return next((r for r in ranks if ranks.count(r) == n), None)

def test():
    "Test cases for the functions in poker program."
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fkranks = card_ranks(fk)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    print 'tests pass'

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

def main():
    test()

if __name__ == '__main__':
    exit(main())
