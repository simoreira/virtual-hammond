import hashlib

__all__ = ['md5', 'list_to_csv', 'remove_string_whitespace']

def md5(string):
    return hashlib.md5(str(string)).hexdigest()

def list_to_csv(a):
    return ",".join(map(str, list(a)))

def remove_string_whitespace(string):
    return string.replace(" ", "")
