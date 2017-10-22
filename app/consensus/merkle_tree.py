import codecs
from merkle import MerkleTree


def merkle_tree(transactions):
    mt = MerkleTree()

    for t in transactions:
        mt.add(t.encode('utf-8'))

    return codecs.encode(mt.build(), 'hex-codec').decode('utf-8')

