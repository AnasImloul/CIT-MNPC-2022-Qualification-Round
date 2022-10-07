vowels = "aeiou"


def remove_adj(word):
    """
    n is the length of the word
    time complexity: O(n) -> we iterate over the word once
    space complexity: O(n) -> we use a string to store the result
    """
    # remove all the adjacent characters that are the same
    # initialize the result string
    result = ""
    # set a variable to keep track of the last character
    last = None
    # iterate over the word
    for char in word:
        # if the current character is the same as the last one, skip it
        if last == char:
            continue
        # otherwise, append it to the result
        result += char
        # update the last character to the current one
        last = char
    # return the result
    return result


def remove_vowels(word):
    """
    n is the length of the word
    time complexity: O(n) -> we iterate over the word once
    space complexity: O(n) -> we use a string to store the result
    """
    # remove all the vowels from the word
    # except the first and the last one

    # initialize the result string
    result = word[0]
    # iterate over the word starting from the second character to the last one minus one
    for i in range(1, len(word) - 1):
        char = word[i]
        # if the current character is a vowel, skip it
        if char in vowels:
            continue
        # otherwise, append it to the result
        result += char
    # if length of the word is greater than 1
    # append the last character to the result
    if len(word) > 1:
        result += word[-1]
    # return the result
    return result


def clean(word):
    """
    n is the length of the word
    time complexity: O(n) -> we iterate over the word once
    space complexity: O(n) -> we use a string to store the result
    """
    # remove all the adjacent characters that are the same
    # remove all the vowels from the word except the first and the last one

    # note that the order of the operations is important here
    # example: "lol" -> remove_vowel -> "ll" -> remove_adj -> "l"
    # example: "lol" -> remove_adj -> "lol" -> remove_vowel -> "ll"
    return remove_vowels(remove_adj(word))


def solve(text):
    """
    n is the number of words in the text
    m is the length of the longest word in the text
    n*m is the total length of the text
    time complexity: O(n*m) -> we iterate over the text once
    space complexity: O(n*m) -> we use a string to store the result
    """
    # iterate over the text and clean each word
    # then join the words together and return the result
    return " ".join(map(lambda word: clean(word), text.split()))


n = int(input())
text = input()
print(solve(text))
