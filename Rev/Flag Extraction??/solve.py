def manipulate_string(input_str):
    result = []
    for i, char in enumerate(input_str):
        if i % 2 == 0:  # Even index
            result.append(chr(ord(char) - 1))
        else:  # Odd index
            result.append(chr(ord(char) + 1))
    return ''.join(result)

input_string = "[dorfBUE|q4u`/s0h0o4~"
output_string = manipulate_string(input_string)
print(output_string)
