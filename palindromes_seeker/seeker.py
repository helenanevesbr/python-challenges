import re
import unicodedata

from dispatcher import add_lines

def main():
    set_of_lines = add_lines()
    print(f'Linha com mais Palíndromos: {line_with_most_palindromes(set_of_lines)[0]}')
    print(f'Quantidade de palavras Palíndromas:', line_with_most_palindromes(set_of_lines)[1])

def remove_punctuation(line):
    special_characters = re.compile('[,;.:_!? -]+')
    return special_characters.sub('', line)

def line_with_most_palindromes(set_of_lines):
    highest_number_of_palindromes = 0
    line_with_most_palindromes = 'Nenhuma linha com palíndromos encontrada'
    for line in set_of_lines:
        raw_line = list(map(remove_punctuation, line.split()))
        palindromes_in_line = 0
        for raw_word in raw_line:
            word = normalize_word(raw_word)
            reversed_word = word[::-1]
            if reversed_word == word:
                palindromes_in_line += 1
        if highest_number_of_palindromes < palindromes_in_line:
            highest_number_of_palindromes = palindromes_in_line
            line_with_most_palindromes = line
    return line_with_most_palindromes, highest_number_of_palindromes

def normalize_word(raw_word):
    text = ''.join((word for word in unicodedata.normalize('NFD', raw_word) if unicodedata.category(word) != 'Mn')).lower()
    return text

main()