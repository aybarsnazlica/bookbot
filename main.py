from stats import count_chars, count_words
import sys


def main():
    """Generates a report on the frequency of each alphabetical character in a text file.

    Reads the file located at "books/frankenstein.txt", counts the total number of words,
    and counts the frequency of each alphabetical character in the text.
    Prints a sorted report of the character frequencies in descending order.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = ""
    total_words = 0

    with open(file_path) as f:
        for line in f:
            total_words += count_words(line)
            line = line.strip()
            text += line

    count_table = count_chars(text)
    count_table_sorted = dict(
        sorted(count_table.items(), key=lambda item: item[1], reverse=True)
    )

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for key, value in count_table_sorted.items():
        print(f"{key}: {value}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
