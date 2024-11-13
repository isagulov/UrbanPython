class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()  # Приводим к нижнему регистру
                    for char in punctuation:
                        line = line.replace(char, '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        word_lower = word.lower()

        for file_name, words in all_words.items():
            if word_lower in words:
                result[file_name] = words.index(word_lower) + 1

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        word_lower = word.lower()

        for file_name, words in all_words.items():
            result[file_name] = words.count(word_lower)

        return result


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))      # Позиция первого вхождения слова
print(finder2.count('teXT'))     # Количество вхождений слова
