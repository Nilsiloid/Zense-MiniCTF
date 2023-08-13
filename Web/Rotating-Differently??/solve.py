def convert_to_reverse_alphabet(text):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            shifted = ord(char) - offset
            new_char = chr(offset + 25 - shifted)
            result += new_char
        else:
            result += char
    return result

input_string = input("Enter a string: ")
converted_string = convert_to_reverse_alphabet(input_string)
print("Converted string:", converted_string)