def count_chars(text):
    """Counts the frequency of each alphabetical character in a string.

    Args:
        text (str): The input text to count characters from.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    count_table = {}

    for char in text:
        if char.isalpha():
            count_table[char.lower()] = count_table.get(char.lower(), 0) + 1
    return count_table


def count_words(line):
    """Counts the number of words in a line of text.

    Args:
        line (str): The input line to count words from.

    Returns:
        int: The number of words in the line.
    """
    return len(line.split())
