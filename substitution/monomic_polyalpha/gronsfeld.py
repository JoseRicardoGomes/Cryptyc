def encode(text: str = "", key: str = "") -> str:
    if not key:
        raise ValueError("Key must not be empty.")
    
    key_as_list = list[int]
    output_buff = []

    if len(text) == len(key):
        key_as_list = [int(char) for char in key]
    else:
        key_as_list = __repeat_to_length(key, len(text))

    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key_as_list[i]) % 26 + base
            output_buff.append(chr(shifted))
        else:
            output_buff.append(char)
    
    return "".join(output_buff)

'''
Take a string key and add padding by repeating the key up to size.
'''
def __repeat_to_length(key: str = "", input_lenght: int = 0) -> list[int]:
    if not key:
        raise ValueError("Input string must not be empty.")
    repeated = (key * (input_lenght // len(key) + 1))[: input_lenght]
    return [int(char) for char in repeated]
