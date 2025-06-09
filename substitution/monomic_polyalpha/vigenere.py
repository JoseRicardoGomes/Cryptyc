# vigenere.py
import sys

vigenere_table = [
    [chr((i + j) % 26 + ord('A')) for j in range(26)]
    for i in range(26)
]

def encode(text: str = "") -> str:
    result = []

    for c in text:
        result.append(_search_viginere_table(c))

    return "".join(result)

def _search_viginere_table(c):
    pos = ord(c.upper()) - ord('A') 
    if not (0 <= pos < 26) or not c.isalpha():
        return c
    return vigenere_table[pos][pos]