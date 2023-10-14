import requests

def get_word_definition(word):
    base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en'
    url = f"{base_url}/{word}"

    try:
        response = requests.get(url)
        data = response.json()

        if isinstance(data, list) and len(data) > 0:
            word_data = data[0]
            print(f"Word: {word_data['word']}")
            print(f"Phonetic: {word_data.get('phonetic', 'N/A')}")

            if 'meanings' in word_data:
                for meaning in word_data['meanings']:
                    part_of_speech = meaning['partOfSpeech']
                    print(f"Part of Speech: {part_of_speech}")

                    for definition in meaning['definitions']:
                        print(f"Definition: {definition['definition']}")
                        if 'example' in definition:
                            print(f"Example: {definition['example']}")

                    print()
   
    


        else:
            print("Word not found in the dictionary.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        
        
    print()
    print()
    print()     
    

if __name__ == "__main__":
    while True:
        word = input("Enter a word to look up (or type 'exit' to quit): ").strip().lower()

        if word == 'exit':
            break

        get_word_definition(word)
