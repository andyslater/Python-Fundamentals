""" Retrieve and print words from a list
 Tools to read a UTF-8 text document from a URL which will be split in to its component words for printing.

 This is from pluralsight, Python Fundamentals, Strings and collections chapter
 https://app.pluralsight.com/player?course=python-fundamentals&author=austin-bingham&name=python-fundamentals-m02-strings&clip=8&mode=live

with this documentation you can use the REPL to do things like
    >>>import modularity  # the name of this module
    >>>help(modularity)
    >>>help(fetch_words)

 Script Usage:

    python modularity.py <URL>
    python modularity.py http://sixty-north.com/c/t.txt
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: the URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document
    """
    with urlopen(url) as story:  # with calls urlpen an binds the result to story
        story_words = []
        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                story_words.append(word)
    print(locals())
    return story_words

def print_items(items):
    """"Print items one per line

    Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)

def main(url):
    """Print each word from a test document from a URL.

    Args:
        url: the URL of a UTR-8 text document.
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == "__main__":
    main(sys.argv[1]) # the 0th arg is the module filename
        