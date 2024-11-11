def count_chars(text):
    count_table = {}

    for char in text:
        if char.isalpha():
            count_table[char.lower()] = count_table.get(char.lower(), 0) + 1
    return count_table


def count_words(line):
    return len(line.split())


def main():
    file_path = "books/frankenstein.txt"
    text = ""
    total_words = 0

    with open(file_path) as f:
        for line in f:
            total_words += count_words(line)
            line = line.strip()
            text += line

    count_table = count_chars(text)
    count_table_sorted = dict(sorted(count_table.items(), key=lambda item: item[1], reverse=True))

    print(f"--- Begin report of {file_path} ---\n{total_words} words found in the document\n")

    for key, value in count_table_sorted.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


if __name__ == '__main__':
    main()
