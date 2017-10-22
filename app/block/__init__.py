import json

block_list = []

class Block():
    type = ''
    prev_block_id = 0
    prev_block_hash = ''
    block_id = 0;
    merkle_root = ''
    # time_stamp = ''
    block_hash = ''
    nonce = ''
    difficulty = 0
    tx_list = ''

    def __init__(self):
        self.type = 'B'

    def __str__(self):
        return self.to_json()

    def to_json(self):
        return json.dumps({
            'type': self.type,
            'prev_block_id': self.prev_block_id,
            'prev_block_hash': self.prev_block_hash,
            'block_id': self.block_id,
            'merkle_root': self.merkle_root,
            'difficulty:': self.difficulty,
            'nonce': self.nonce,

            'block_hash': self.block_hash,
            'tx_list': self.tx_list
        })

    def from_json(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

        return self

    def getheader_json(self):
        return json.dumps({
            'type': self.type,
            'prev_block_id': self.prev_block_id,
            'prev_block_hash': self.prev_block_hash,
            'block_id': self.block_id,
            'merkle_root': self.merkle_root,
            'difficulty': self.difficulty,
            'nonce': self.nonce
        })

def count():
    return len(block_list)


def get_all_block():
    return block_list


def append_block(block):
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
    b.prev_block_id = 0
    b.prev_block_hash = 'prev_block_hash'
    b.block_id = 1
    b.merkle_root = 'merkle_root'
    b.block_hash = 'block_hash'
    b.difficulty = 0
    b.nonce = 'nonce'
    b.tx_list = []

    append_block(b)
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
