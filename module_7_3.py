import string
class WordsFinder():
    file_names = []

    def __init__(self, *args):
        self.args = args

    def get_all_words(self):
        all_words = {}
        strip_words = []
        for i in self.args:
            with open(i, encoding='utf-8') as file:
                for j in file:
                    j_low = j.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for p in punctuation:
                        if p in j_low:
                            j_low = j_low.replace(p,'')
                            strip_words += j_low.split()
                    all_words[f"{i}"] = strip_words
                return all_words

    def find(self, word):
        match_dict = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    match_dict[f'{name}'] = (words.index(i)) + 1
                    return match_dict

    def count(self, word):
        count_dict = {}
        count = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    count += 1
            count_dict[f'{name}'] = count
            return count_dict

