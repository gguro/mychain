import hashlib
import random


from numpy import long

max_nonce = 2 ** 32


def proof_of_work(block_header, diff_bits):
    target = 2 ** (256 - diff_bits)

    print("target : %064x" % target)

    found = False

    while not found:
        nonce = random.randint(0, max_nonce)

        hash_result = hashlib.sha256(str(block_header).encode('utf-8') + str(nonce).encode('utf-8')).hexdigest()

        if long(hash_result, 16) <= target:
            print("Found, nonce = " + str(nonce))
            return hash_result, nonce

    return '', 0


if __name__ == '__main__':

    hash_value, nonce = proof_of_work('TEST', 5)
    print (nonce)