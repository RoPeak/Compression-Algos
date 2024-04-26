# Encode using LZW algorithm
def encode(data):
    """Compress the given string into a list of output symbols"""
    # Build the dictionary
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    
    string = ""     # Null string
    compressed = [] # Variable to store result

    # Iterate through input symbols
    for symbol in data:
        string_with_symbol = string + symbol
        if string_with_symbol in dictionary:
            string = string_with_symbol
        else:
            compressed.append(dictionary[string])
            string = symbol

    if string in dictionary:
        compressed.append(dictionary[string])
    
    print(compressed)

# Decode using LZW algorithm
def decode(data):
    pass

def main():
    encode("ABABBABBB")

if __name__ == '__main__':
    main()