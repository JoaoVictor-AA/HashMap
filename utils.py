def hash_function(value):
    soma = 0
    for char in value:
        soma += ord(char)
    return soma % 10