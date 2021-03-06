import os

from ecdsa import SigningKey, NIST256p, VerifyingKey

KEY_PATH = os.getcwd()
PRI_KEY_PATH = KEY_PATH + "/data/private.pem"
PUB_KEY_PATH = KEY_PATH + "/data/public.pem"


def generate_key():
    # 공개키, 개인키 생성
    pri_key = SigningKey.generate(curve=NIST256p)
    pub_key = pri_key.get_verifying_key()

    # 생성된 공인키 개인키를 파일로 생성
    open(PRI_KEY_PATH, "w", encoding='utf-8').write(pri_key.to_pem().decode('utf-8'))
    open(PUB_KEY_PATH, "w", encoding='utf-8').write(pub_key.to_pem().decode('utf-8'))

    return pri_key, pub_key


def get_key():
    # 파일로부터 개인키, 공개키 읽어서 리턴

    if (not os.path.exists(PRI_KEY_PATH)):
        print("Generate keys...")
        generate_key()

    if (os.path.exists(PRI_KEY_PATH)):
        pri_key = SigningKey.from_pem(open(PRI_KEY_PATH, encoding='utf-8').read())
        pub_key = pri_key.get_verifying_key()
        return pri_key, pub_key

    return '', ''




def key_to_string(key):
    return key.to_string()


def key_to_string2(key):
    return key.to_pem().decode('utf-8')


def get_signature(message, private_key):
    return private_key.sign(message.encode('utf-8'))


if __name__ == '__main__':
    import json

    pri, pub = generate_key()
    print (key_to_string2(pri))
    print (key_to_string2(pub))

    pri2, pub2 = get_key()
    print (key_to_string2(pri2))
    print (key_to_string2(pub2))





