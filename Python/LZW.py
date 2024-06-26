import os

# Dynamically grab a list of the available resource files
RESOURCE_FILE_PATH = os.getcwd() + os.path.sep + "Resource"
RESOURCE_FILES = [RESOURCE_FILE_PATH + os.path.sep + FILE for FILE in os.listdir(RESOURCE_FILE_PATH)]

# Define output directory for encoded data
OUTPUT_FILE_PATH = os.getcwd() + os.path.sep + "Output"
os.mkdir(OUTPUT_FILE_PATH)

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
    
    # Output

# Decode using LZW algorithm
def decode(data):
    # Initialise variables
    next_code = 256
    decompressed = ""
    string = ""

    # Build the dictionary
    dictionary_size = 256
    dictionary = {x: chr(x) for x in range(dictionary_size)}

    # Iterate through the codes
    for code in data:
        if not (code in dictionary):
            dictionary[code] = string + string[0]
        decompressed += dictionary[code]
        if not (len(string) == 0):
            dictionary[next_code] = string + dictionary[code][0]
            next_code += 1
        string = dictionary[code]
    
    return decompressed

def main():
    pass

if __name__ == '__main__':
    main()