import sys
import string

def file_to_pig_latin(input, output):
    for line in input:
        words = line.split()
        # translated_words = [word_to_pig_latin(word) for word in words]
        translated_words = []
        for word in words:
            translated_word = word_to_pig_latin(word)
            translated_words.append(translated_word)
        translated_line = " ".join(translated_words)
        output.write(translated_line + "\n")

def word_to_pig_latin(word):
    for first_letter,char in enumerate(word):
        if char not in string.punctuation:
            break
    for last_letter,char in enumerate(word[::-1]):
        if char not in string.punctuation:
            break
    last_letter = len(word) - last_letter
    actual_word = word[first_letter:last_letter]
    pig = do_translation(actual_word.lower())
    
    if word. istitle():
        pig = pig.title()
    pig = word[:first_letter]+pig+word[last_letter:]
    return pig

def do_translation(word):
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        for i, letter in enumerate(word):
            if letter in vowels or letter == "y":
                return word[i:] + word[:i] + "ay"
        return word

def get_name(file_type):
    return input(f"Enter the {file_type} file name: ")

def main():
    input_name = get_name("input")
    output_name = get_name("output")
    # input_name = "jedi_code.txt"
    # output_name = "pig_code.txt"

    try:
        with (
        open(input_name, "r") as input_file,
        open(output_name, "w") as output_file
        ):
            file_to_pig_latin(input_file, output_file)
            
    except OSError:
        print(f"File Error!")
        sys.exit()

main()