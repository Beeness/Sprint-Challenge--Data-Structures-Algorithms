Add your answers to the Algorithms exercises here.

Exercise I.
a) O(n)
b) O(logn)
c) O(logn)
d) O(n^2)
e) O(n^3)
f) O(n)
g) O(n)

Exercise II.
a)
b)
MAX_FLOOR = 100

def safest_egg_drop_floor(n):
    """Return the safest floor to drop an egg from."""

    assert 1 <= n <= MAX_FLOOR, 'Building has floors from 1 through {}'.format(MAX_FLOOR)

    # Calculate the optimal delta to start with, to reduce attempt numbers
    delta = int(math.ceil((math.sqrt(1 + 8*MAX_FLOOR) - 1)/ 2))

    low, high = 1, delta

    while low < MAX_FLOOR:
        if high >= n:
            print('  First egg broke on floor {}'.format(high))

            for i in range(low, high+1):
                if i >= n:
                    print('  Second egg broke on floor {}'.format(i))
                    if i == 1:
                        raise ValueError("Eggs will always break")
                    else:
                        return i - 1
        else:
            delta -= 1
            low, high = high, high + delta
            if high > MAX_FLOOR:
                high = MAX_FLOOR

    return MAX_FLOOR


def main():

    for i in range(0, MAX_FLOOR+2):
        print('\nFind egg drop when it breaks at {}'.format(i))
        try:
            max_floor = safest_egg_drop_floor(i)
            print('    Safest drop from floor {}'.format(max_floor))
        except (ValueError, AssertionError) as error:
            print(error)

Exercise III.
a) It would be O(n^2) even though it has already been sorted it still has to compare two numbers.
b) I feel like if the pivot is always the middle it should be quicker than a pivot in the beginning due to the placement although I'm not sure of the runtime. perhaps O(n).