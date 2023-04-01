import itertools
import hashlib


def retrieve_input_file_info(inputDataFile):
    """ Read a file and convert content into an array of arrays of each line elements """

    try:
        inputFile = open(inputDataFile, "r")
        LinesRead = inputFile.readlines()
    except:
        return "Wrong file format. Please make sure that it is .txt file. "
    
    arr_of_lines = []
    array_of_line_items = []

    for line in LinesRead:
        line = line.strip()
        arr_of_lines.append(line)

    for elem in arr_of_lines:
        splitted_line_array = elem.split(',')
        splitted_line_array = [element.strip() for element in splitted_line_array]
        array_of_line_items.append(splitted_line_array)
    
    inputFile.close()
    return array_of_line_items

def generate_passwords(max_length, array_of_line_items):
    """ creates an array of passwords """
    
    array_of_passwords = []
    output_dictionary = {}
    dictionary_accepted_characters = { 'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 
                'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 
                'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z', 
                'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 
                'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 
                'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z',
                'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                'eight': '8', 'nine': '9', 
                '#': '#', '$': '$', '!': '!', '&': '&'
            }
    
    for num in range(1, max_length + 1):
        password_tuple = itertools.product(dictionary_accepted_characters.values(), repeat=num)
        for tuple_char in password_tuple:   # returns ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in tuple_char:
                characters_in_passcode += char
            array_of_passwords.append(characters_in_passcode)

    try:
        for arr in array_of_line_items:
            salt = arr[len(arr) - 1]
            for password in array_of_passwords:
                salted_password = password + salt
                hashed_salted_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()       
                if(hashed_salted_password == arr[1]):
                    output_dictionary[arr[0]] = password

        # handle remaining elements in array_of_line_items
        for array in array_of_line_items:
            if array[0] not in output_dictionary:
                output_dictionary[array[0]] = '?????'
    except:
        return "Invalid input file. Make sure it's .txt file and exists in correct directory."

    return list(output_dictionary.items()) # display tuple of key and value pair


def user_input():
    """ Accepts user input and renders passwords generated using password generator function """
    
    input_file = input("Enter your input file: ")
    try:
        max_password_length = int(input("Enter maximum password length (Example 4): "))
    except:
        return "Invalid literal. Length must be of type integer. "

    array_of_line_items = retrieve_input_file_info(input_file)
    return generate_passwords(max_password_length, array_of_line_items)


if __name__ == "__main__":
    print(user_input())