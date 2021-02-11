def append_two_strings(string_1, string_2):
    
    return string_1 + string_2

def append_character(string_1, char_1):

    return string_1 + str(char_1)


def append_num_to_string(string_1, num_1):

    return string_1 + str(int(num_1))


if __name__ == "__main__":
    print(append_two_strings('hello', 'world'))
    print(append_character('hello', "*"))
    print(append_num_to_string('hello', 4))