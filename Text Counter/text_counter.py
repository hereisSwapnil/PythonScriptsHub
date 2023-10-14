import re

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        file.close()
        return text
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None


def count_words(text):
    words = text.split()
    return len(words)


def count_sentences(text):
    sentences = re.split(r'[.!?\n]', text) # Split's the sentences by . or ! or ? or \n
    
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)


def count_paragraphs(text):
    paragraphs = re.split(r'\n{2,}', text) 
    # Assuming that paras are seperated by more than 1 \n (new line)

    paragraphs = [paragraph for paragraph in paragraphs if paragraph.strip()]
    return len(paragraphs)


if __name__ == "__main__":

    file_path = input("Enter the file path: ")

    text = read_text_from_file(file_path)
    if text:
        word_count = count_words(text)
        sentence_count = count_sentences(text)
        paragraph_count = count_paragraphs(text)

        print("Word count:", word_count)
        print("Sentence count:", sentence_count)
        print("Paragraph count:", paragraph_count)
