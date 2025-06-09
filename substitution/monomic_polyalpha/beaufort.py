vigenere_table = [
    [chr((i + j) % 26 + ord('A')) for j in range(26)]
    for i in range(26)
]

def encode(text: str = "", keyStream: str = "") -> str:
    result = []
    filtered_key = [k for k in keyStream if k.isalpha()]
    key_len = len(filtered_key)
    key_index = 0

    for c in text:
        if c.isalpha():
            key = filtered_key[key_index % key_len]
            result.append(_search_viginere_table(c, key))
            key_index += 1
        else:
            result.append(c)

    return "".join(result)

def _search_viginere_table(c, key):
    # Compute char and key positions
    posChar = ord(c.upper()) - ord('A')
    posKey = ord(key.upper()) - ord('A')
    
    # If char is not a letter or in range return char itself
    if not (0 <= posChar < 26) or not c.isalpha():
        return c
    if not (0 <= posKey < 26) or not key.isalpha():
        return c
    # return table position
    return vigenere_table[posKey][posChar]