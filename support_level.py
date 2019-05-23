
from collections import defaultdict

# product lookup table
lookup = {}

# txs
txs = []


def print_support_level(level=2):
    '''print result depends on level parameter'''
    with open('results.txt', 'w') as fout:
        for item in lookup:
            if len(lookup[item]) >= level:
                print('{size}, {freq}, {items}'.format(size=len(item), freq=len(lookup[item]), items=', '.join(map(str,item))), file=fout)


def main():
    ''' main function '''

    with open('retail_25k.dat') as log:
        # scan input file and read a transaction
        for tx in log:
            item_set = set(map(int,tx.strip().split()))
            txs.append(item_set)

    # n^2 solution
    # intersection with all other transactions
    # if the size of common set is greater than 2, register lookup tables
    for i in range(len(txs)-1):
        print('start {}'.format(i))
        for j in range(i+1, len(txs)):
            common = txs[i] & txs[j]
            key = tuple(common)
            if len(key) > 2:
                if key in lookup:
                    lookup[key].add(i)
                    lookup[key].add(j)
                else:
                    lookup[key] = {i, j}

    print_support_level(level=4)


if __name__ == '__main__':
    main()


