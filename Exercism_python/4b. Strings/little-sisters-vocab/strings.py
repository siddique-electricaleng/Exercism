"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return f"un{word}"

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    word_list = []
    prefix = vocab_words[0] if vocab_words else ""

    for index, item in enumerate(vocab_words):
        if (index == 0):
            word_list.append(prefix)
        else:
            word_list.append(prefix+item)

    return " :: ".join(word_list)

print(make_word_groups(['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
                      'echolalia', 'encoder', 'biography']))

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if isinstance(word,str):
        if(word[-5:]=="iness"):
            return (word[:-5] + "y")
        elif (word[-4:]=="ness"):
            return (word[:-4])
        else:
            return "Error: No rule was accounted for this"
    else:
        return "You didn't enter a string"

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    word = sentence.split()[index].strip(",.?!-:")
    return f"{word}en"
