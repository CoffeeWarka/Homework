import string
class WordsFinder():
    file_names = []

    def __init__(self, *args):
        self.args = args

    def get_all_words(self):
        all_words = {}
        for i in self.args:
            strip_words = []
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
            index = 0
            for i in words:
                index +=1


                if i == word.lower():
                    match_dict[f'{name}'] = index
                    break
        return match_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if i == word.lower():
                    count += 1
            count_dict[f'{name}'] = count
        return count_dict
