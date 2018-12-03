def anagram(str1, str2):

    # Remove spaces and lower case all letters
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # Fast Fail
    # are the strings the same length?
    if len(str1) != len(str2):
        return False

    # create a dict to hold key, value pairs ex. -> { a:1, b:0, c:1 }
    counter = {}

    
    # iterate through letters in first string
    for letter in str1:
        # is the letter in the counter dict?
        if letter in counter:
            # YES..? add one to count
            counter[letter] += 1
        else:
            # NO..? initalize key, value pair in dict
            counter[letter] = 1
            
    # iterate through letters in second string
    for letter in str2:
        # is the letter in the counter dict?
        if letter in counter:
            # YES..? subtract one to count
            counter[letter] -= 1
        else:
            # NO..? strings are not anagrams (return False)
            return False
    
    # Check to make sure multiple letters are accounted for
    for letter in counter:
        # check that no extra letters are stored
        if counter[letter] != 0:
          return False
    
    # strings contain same letters (return True)
    return True



### TESTS ###

test_1 = anagram('abc', 'bca')
print(test_1)

test_2 = anagram('aabbcc', 'aabbca')
print(test_2)

test_3 = anagram('go go go', 'gggooo')
print(test_3)

test_4 = anagram('hi man', 'hi     man')
print(test_4)

