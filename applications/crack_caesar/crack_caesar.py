frequency_table = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                   'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
tally_dict = {}
decode_table = {}


def crack_caesar(text):
    with open(f'./applications/crack_caesar/{text}') as f:
        data = f.read()

    # build up tally dictionary
    for char in data:
        if char < 'A' or char > 'Z':
            continue
        if char in tally_dict:
            tally_dict[char] += 1
        else:
            tally_dict[char] = 1

    # sort tally dictionary
    sorted_tally = sorted(tally_dict.items(), key=lambda x: x[1], reverse=True)
    print('sorted tally', sorted_tally)
    # assign encoded most frequent to general use most frequent
    counter = 0
    for key, value in sorted_tally:
        decode_table[key] = frequency_table[counter]
        counter += 1

    # decode
    decoded_string = ''
    for char in data:
        if char < 'A' or char > 'Z':
            decoded_string += char
            continue

        decoded_string += decode_table[char]

    print(decoded_string)


crack_caesar('ciphertext.txt')
