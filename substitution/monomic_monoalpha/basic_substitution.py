# basic substitution
"""
@TODO: Add decode
"""
import sys
from typing import Optional

defaultKey = {chr(i): chr((i - 96) % 26 + 97) for i in range(97, 123)}

def encode(strArr: str = "", keyArr: Optional[dict] = None) -> str: 

    result = []
    key = str()

    # If fed key arr is empty then use default
    if keyArr == None:
        key = defaultKey
    else:
        key = keyArr

    for c in strArr:
        result.append(key.get(c))

    return "".join(result)