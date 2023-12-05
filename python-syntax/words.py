# this should print "HELLO", "HEY", "YO", and "YES"
def print_upper_words(words, must_start_with):
    """For a list of words, print out each word on a separate line, but in all uppercase. """
    print(must_start_with)
    for word in words:
        for i in must_start_with:
            if word.startswith(i):
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h"})
# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).