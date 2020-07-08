# understand:
# given a string
# return every letter and how many times it occurs in this string
# sorted by frequence of occurrence

# planning:
# iterate through our string
# tally the count using a dictionary
# sort the dicionary by the value(ie. the count of each letter)

# upper or lower-case everything
# handle spaces

# should we turn the string into a list first

def print_letter_count(s):
    tally = {}

    s = s.lower()
    for character in s:
        if character >= 'a' and character <= 'z':
            if character not in tally:
                tally[character] = 1

            else:
                tally[character] += 1


# print_letter_count: print_letter_count
# print_letter_count('the quick brown fox jumps over the lazy dog')

# sort works in place
    tally_list = list(tally.items())
    tally_list.sort(key=lambda x: x[1], reverse=True)
