# beaufort.py

def encode(text: str = "", keyStream: str = "") -> str:
    result = []
    filtered_key = [k.upper() for k in keyStream if k.isalpha()]
    key_len = len(filtered_key)
    key_index = 0

    for c in text:
        if c.isalpha():
            key = filtered_key[key_index % key_len]
            result.append(_beaufort_char(c, key))
            key_index += 1
        else:
            result.append(c)

    return "".join(result)

def _beaufort_char(key, c):
    key_val = ord(key.upper()) - ord('A')
    char_val = ord(c.upper()) - ord('A')

    if not (0 <= key_val < 26 and 0 <= char_val < 26):
        return c

    result = (key_val - char_val + 26) % 26
    return chr(result + ord('A'))
