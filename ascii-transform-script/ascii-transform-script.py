def text_to_ascii(text):
    ascii_art = ""
    for char in text:
        if char.isalpha():
            ascii_art += chr(ord(char) + 3)  # You can adjust the value to modify the ASCII art
        elif char.isspace():
            ascii_art += " "
        else:
            ascii_art += char
    return ascii_art

if __name__ == "__main__":
    input_text = input("Enter the text you want to convert to ASCII art: ")
    ascii_art = text_to_ascii(input_text)
    print(ascii_art)
