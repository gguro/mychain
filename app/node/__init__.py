import json

nodelist = []

class Node():
    ip_address = ''
    type =''
    public_key = ''
    private_key = ''

    def __init__(self, ip_address):
        self.type = 'N'
        self.ip_address = ip_address
        self.public_key = ''
        self.private_key = ''

    def __str__(self):
        return self.to_json()

    def to_json(self):
        return json.dumps({
            'type': self.type,
            'ip_address': self.ip_address,
            'pub_key': self.public_key,
            'pri_key': self.private_key
        })


def add_node(node):
    print ("add_node : " + str(node))
    nodelist.append(node)


def count():
    return nodelist.count()


def get_my_node():
    pass


def get_all():
    return nodelist
