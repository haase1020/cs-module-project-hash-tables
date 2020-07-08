def word_count(s):
    # Your code here
    # single string as an argument
    # returns a dictionary of WORDS and their counts (if in sentence)
    # all outputs should be changed to lowercase
    # key order in dictionary doesn't matter
    # split with whitespace ''
    # ignore: " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    # if no ignored characters, return an empty dictionary
    s = s.split()
    count = {}

    if not s:
        return count

    for word in s:
        element = "".join(
            char for char in word if char.isalpha() or char == "'").lower()

        if element == "":
            continue
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
