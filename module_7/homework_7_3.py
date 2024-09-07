class WordsFinder:
    def __init__(self, *file_names):
        self.files_names = file_names


    def get_all_words(self):
        all_words = {}
        for f in self.files_names:
            try:
                with open(f, 'r', encoding='utf-8') as file:
                    file_words = file.read().lower()
                    for chars in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        file_words = file_words.replace(chars, ' ')
                    file_words = file_words.split()
                    all_words[f] = file_words
            except FileNotFoundError:
                print(f'File {f} not found.')
            except Exception as exc:
                print(f'An error occurred while processing the file {f}: {exc}')

        return all_words

    def find_word(self, word):
        word = word.lower()
        position = {}
        all_words = self.get_all_words()

        for key_, value_ in all_words.items():
            if word in value_:
                position[key_] = value_.index(word) + 1 # +1 что бы совпало с ответом (позиция != индекс видимо)
            else:
                position[key_] = None

        return position

    def words_count(self, word):
        word = word.lower()
        count = {}
        all_words = self.get_all_words()

        for key_, value_ in all_words.items():
            count[key_] = value_.count(word)

        return count







finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find_word('the'))
print(finder1.words_count('the'))