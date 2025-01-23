import sys

ALPHABET_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def count_chars(contents: str) -> dict:
    lower_contents = contents.lower()
    char_counts = {}
    for char in lower_contents:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

def print_report(char_dict) -> None:
    only_letters = { char: char_dict[char] for char in char_dict if char in ALPHABET_lower}
    keys_descending = sorted(only_letters, key=only_letters.get, reverse=True)

    for key in keys_descending:
        print(f"The '{key}' character was found {only_letters[key]} times")


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Incorrect number of args found, expected 1 file path as input.")
    #     sys.exit(1)
        
    try:
        path_to_file = "books/frankenstein.txt"
        # path_to_file = sys.argv[1]
        with open(path_to_file) as f:
            file_contents = f.read()
            all_words = file_contents.split()
            counts = count_chars(file_contents)
            #print(file_contents)
            print(f"--- Begin report of {path_to_file} ---")
            print(f"{len(all_words)} words found in the document\n")
            #print(counts)

            print_report(counts)

    except FileNotFoundError as fnfe:
        print(fnfe)