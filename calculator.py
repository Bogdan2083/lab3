def add(a, b):
    return a + b

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Аргумент повинен бути рядком")
    return s[::-1]