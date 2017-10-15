import json

from dateutil import parser

from app import util

block_list = []

class Block():
    type = ''
    prev_block_id = ''
    prev_block_hash = ''
    tx_list = ''
    merkle_root = ''
    time_stamp = ''
    block_id = ''
    block_hash = ''
    nonce = ''
    block_info = ''
    block_miner = ''

    def __init__(self):
        self.type = 'B'

    def __str__(self):
        return self.to_json()

    def to_json(self):
        return json.dumps({
            'type': self.type,
            'time_stamp': self.time_stamp.strftime('%Y%m%d%H%M%S'),
            'prev_block_id': self.prev_block_id,
            'prev_block_hash': self.prev_block_hash,
            'merkle_root': self.merkle_root,
            'block_hash': self.block_hash,
            'nonce': self.nonce,
            'block_id': self.block_id
        })

    def from_json(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

        self.time_stamp = parser.parse(self.time_stamp)
        return self


def count():
    return len(block_list)


def get_all_block():
    return block_list


def create_block(block):
    block_list.append(block)


def create_genesis_block():
    # master node 인지 확인
    '''
    isMasterNode = util.get_config_item("NODE_INF0", "isMasterNode")
    if isMasterNode == '1': # master node
        print ("This is a master node...")
    else:
        print ("This is a normal node...")
    '''

    b = Block()

    b.prev_block_id = 'B000000000000'
    b.prev_block_hash = '0'
    b.block_id = 'B000000000000'
    b.merkle_root = 'mychain'
    b.block_hash = 'mychain'
    b.nonce = 2010101010

    return b



def get_last_block():
    if count() == 0:
        return create_genesis_block()
    else:
        return get_all_block()[-1]



if __name__ == '__main__':

    t = create_genesis_block()
    temp = json.dumps(t, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    temps = json.loads(temp)
    print(temp)
    print(type(temps['nonce']))
