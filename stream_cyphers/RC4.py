# stream_cyphers.RC4

'''
Generate classic RC4 256bit state array.
'''
def init_state_array(key: str = "") -> list:
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
def generate_keystream(state: list, len: int) -> list:
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
def encrypt(msg: str = "", key: str = "") -> bytes:
    sarray = init_state_array(key)
    ks = generate_keystream(sarray, len(msg))
    encrypted = bytes([ord(char) ^ ks_byte for char, ks_byte in zip(msg, ks)])
    return encrypted

'''
Decrypt bytes msg using key. Parameter msg should be passed as bytes.fromhex(str) or directly as byte stream.
'''
def decrypt(msg: str = "", key: str = "") -> str:
    sarray = init_state_array(key)
    ks = generate_keystream(sarray, len(msg))
    decrypted = bytes([byte ^ ks_byte for byte, ks_byte in zip(msg, ks)])
    return decrypted.decode('latin1')