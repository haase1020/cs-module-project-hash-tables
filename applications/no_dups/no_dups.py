def no_dups(s):
    # Your code here
    # input: a string of words separated by spaces (only lower case alphabet)
    # output: same string with no duplicate words
    # no extra spaces at end of returned string: rstrip()
    nodup_dict = {}
    unique_words = []

    s = s.split()

    for word in s:
        if word in nodup_dict:
            continue
        else:
            nodup_dict[word] = 1
            unique_words.append(word)

    return ' '.join(unique_words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
