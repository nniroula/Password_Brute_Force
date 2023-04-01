import itertools
import hashlib


def retrieve_input_file_info(inputDataFile):
    """ Read a file and convert content into an array of arrays of each line elements """

    inputFile = open(inputDataFile, "r")
    LinesRead = inputFile.readlines()
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

    return list(output_dictionary.items()) # display tuple of key and value pair


def user_input():
    """ Accepts user input and renders passwords generated using password generator function """
    
    input_file = input("Enter your input file: ")
    max_password_length = int(input("Enter maximum password length (Example 4): "))

    array_of_line_items = retrieve_input_file_info(input_file)
    return generate_passwords(max_password_length, array_of_line_items)


if __name__ == "__main__":
    print(user_input())



# example output
# 1785634, hello2
salt1 = 'a567c'
salt2 = 'a5ppp'
salt3 = 'eecf2'
salt4 = 'nn3nn'
salt5 = 'a567c'

pass1 = 'a'
pass2 = 'a2'
pass3 = 'n$4'
pass4 = 'prin'
pass5 = 'denver1'

salted_pass1 = pass1 + salt1
# print(salted_pass1)
salted_pass2 = pass2 + salt2
salted_pass3 = pass3 + salt3
salted_pass4 = pass4 + salt4
# print(salted_pass4)
salted_pass5 = pass5 + salt5

# hashed_salted_pass1 = hashlib.sha256(salted_pass1.encode('utf-8')).hexdigest()
# print('salted pass code 1 ...')
# print(hashed_salted_pass1)

# hashed_salted_pass2 = hashlib.sha256(salted_pass2.encode('utf-8')).hexdigest()
# print('salted pass code 2 ...')
# print(hashed_salted_pass2)

# hashed_salted_pass3 = hashlib.sha256(salted_pass3.encode('utf-8')).hexdigest()
# print('salted pass code 3 ...')
# print(hashed_salted_pass3)

# hashed_salted_pass4 = hashlib.sha256(salted_pass4.encode('utf-8')).hexdigest()
# print('salted pass code 4 ...')
# print(hashed_salted_pass4)

# hashed_salted_pass5 = hashlib.sha256(salted_pass5.encode('utf-8')).hexdigest()
# print('salted pass code 5 ...')
# print(hashed_salted_pass5)


    # print('a' in array_of_passwords)
    # print('n$4' in array_of_passwords)
    # print('#$!' in array_of_passwords)

""" 
        # lenght one passwords
        length_one_password = itertools.product(dictionary_accepted_characters.values(), repeat=1)
        for password in length_one_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                characters_in_passcode += str(char)
            array_of_passwords.append(characters_in_passcode)

        print('length 1 array length is .........')
        print(len(array_of_passwords))

        # lenght 2 passwords
        length_two_password = itertools.product(dictionary_accepted_characters.values(), repeat=2)
        for password in length_two_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                characters_in_passcode += str(char)
            array_of_passwords.append(characters_in_passcode)
        print('array length is .........')
        print(len(array_of_passwords))

        # length 3 passwords
        length_three_password = itertools.product(dictionary_accepted_characters.values(), repeat=3)
        # array_of_passwords = []
        for password in length_three_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                characters_in_passcode += str(char)
            array_of_passwords.append(characters_in_passcode)
        
        print('array lenght is ..............')
        print(len(array_of_passwords))

        # length 4 passwords
        length_four_password = itertools.product(dictionary_accepted_characters.values(), repeat=4)
        for password in length_four_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                characters_in_passcode += str(char)
            array_of_passwords.append(characters_in_passcode)
        
        print('lenght 4 array lenght is ..............')
        print(len(array_of_passwords))
"""

""" 
        # lenght 5 array 
        length_five_password = itertools.product(dictionary_accepted_characters.values(), repeat=5)
        for password in length_five_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                # characters_in_passcode += str(char)
                characters_in_passcode += char
            array_of_passwords.append(characters_in_passcode)
        
        print('lenght 5 array lenght is ..............')
        print(len(array_of_passwords))

 
        # length 6 array
        length_six_password = itertools.product(dictionary_accepted_characters.values(), repeat=6)
        for password in length_six_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                characters_in_passcode += str(char)
            array_of_passwords.append(characters_in_passcode)
        
        print('lenght 6 array lenght is ..............')
        print(len(array_of_passwords))

        # lenght 7
            # length 4 passwords
        length_seven_password = itertools.product(dictionary_accepted_characters.values(), repeat=7)
        for password in length_seven_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                characters_in_passcode += str(char)
            array_of_passwords.append(characters_in_passcode)
        
        print('lenght 7 array lenght is ..............')
        print(len(array_of_passwords))

        # length 8
        length_eight_password = itertools.product(dictionary_accepted_characters.values(), repeat=8)
        for password in length_eight_password:   # return ('A', 'B') ->  combine this to get AB
            characters_in_passcode = ''
            for char in password:
                characters_in_passcode += str(char)
            array_of_passwords.append(characters_in_passcode)
        
        print('lenght 8 array lenght is ..............')
        print(len(array_of_passwords))
"""