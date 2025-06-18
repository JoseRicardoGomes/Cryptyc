# stream_cyphers.RC4

'''
Generate classic RC4 256bit state array.
'''
def key_schedulling(key: str = "") -> list:
    key_bytes = [ord(char) for char in key]
    key_len = len(key_bytes)

    state = list(range(256))

    j = 0

    for i in range(256):
        j = (j + state[i] + key_bytes[i % key_len]) % 256
        state[i], state[j] = state[j], state[i]

    return state

'''
Generate keystream.
'''
def pseudo_random_gen(state: list, len: int) -> list:
    i = j = 0
    keystream = []

    for _ in range(len):
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]

        t = (state[i] + state[j]) % 256
        keystream.append(state[t])

    return keystream 

'''
RC4 encript message using key.
'''
def encrypt(msg: bytes, key: str = "") -> bytes:
    sarray = key_schedulling(key)
    ks = pseudo_random_gen(sarray, len(msg))
    encrypted = bytes([b ^ ks_byte for b, ks_byte in zip(msg, ks)])
    return encrypted

'''
Decrypt bytes msg using key. msg must be bytes.
'''
def decrypt(msg: bytes = b"", key: str = "") -> bytes:
    sarray = key_schedulling(key)
    ks = pseudo_random_gen(sarray, len(msg))
    decrypted = bytes([b ^ ks_byte for b, ks_byte in zip(msg, ks)])
    return decrypted