import pymorphy2
import csv
import string
import os
import importlib.resources as resources

class Borrowed:
    def __init__(self, words, found_borrowed):
        self._dict = dict(sorted(found_borrowed.items(), key=lambda x: x[1].get("Repeats", 1), reverse=True))  # order by repeats
        self._len = len(words)
        self._bor = sum(len(value["Instances"]) for value in found_borrowed.values())
        self._percent = round(self._bor / self._len * 100, 2) if (self._len > 0) else 0

    @property
    def dict(self):
        return self._dict

    @property
    def len(self):
        return self._len

    @property
    def bor(self):
        return self._bor

    @property
    def percent(self):
        return self._percent


def extract(the_text=None, output_file=None):    
    words = [] # read words from the original text file
    words = read_txt(the_text) if the_text.endswith(".txt") else clean_and_split(the_text)

    # normalize words
    normalized_words = normalize(words)

    # read and store borrowed words from the CSV file
    borrowed_words = load_borrowed()

    # check if normalized word is present in borrowed_words
    found_borrowed = find_borrowed(normalized_words, borrowed_words)

    #create instance
    ready_dictionary = Borrowed(words, found_borrowed)

    #manage output file if provided
    if output_file:
        expanded_output_path = os.path.expanduser(output_file)
        if output_file.endswith(".txt"):
            output_file_txt(expanded_output_path, ready_dictionary)

        elif output_file.endswith(".csv"):
            output_file_csv(expanded_output_path, ready_dictionary)

        else: 
            raise ValueError("Invalid output file format. Supported formats are .txt and .csv.")

    return ready_dictionary


def clean_and_split(text):
    words = text.split()
    words_cleaned = []

    for word in words: 
        if not word[-1].isalnum():
            while word and not word[-1].isalnum():
                word = word[:-1]
            while word and not word[0].isalnum():
                word = word[1:]
            if word and word[-1].isalnum():
                words_cleaned.append(word)
        else:
            words_cleaned.append(word)

    return words_cleaned



def read_txt(text_file):
    words_from_file = []
    expanded_file_path = os.path.expanduser(text_file)

    with open(expanded_file_path, "r") as file:
        for line in file:
            words_from_file.extend(clean_and_split(line))

    return words_from_file


def normalize(words):
    morph = pymorphy2.MorphAnalyzer()
    normalized_words = {}

    for word in words:
        normalized_word = morph.parse(word)[0].normal_form.lower()
        normalized_words.setdefault(normalized_word, []).append(word)

    return normalized_words


def load_borrowed(): 
    borrowed_dictionary = resources.files(__name__) / 'borrowed_dictionary.csv'
    borrowed_words = {}

    with open(borrowed_dictionary, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            borrowed_words[row["Key"].lower()] = {"Value": row["Value"], "Origin": row["Origin"], "Repeats": 0}

    return borrowed_words


def find_borrowed(normalized_words, borrowed_words):
    found_borrowed = {}  
    
    for word, instances in normalized_words.items():
        if word in borrowed_words:
            repeats = len(instances)
            borrowed_words[word]["Repeats"] = repeats
            found_borrowed[word] = {
                "Value": borrowed_words[word]["Value"],
                "Origin": borrowed_words[word]["Origin"],
                "Repeats": borrowed_words[word]["Repeats"],
                "Instances": instances
            }

    return found_borrowed


def output_file_txt(expanded_output_path, ready_dictionary):
    with open(expanded_output_path, "w", encoding="utf-8") as formatted_file:
        formatted_file.write(f"Out of a total of {ready_dictionary.len} words, {ready_dictionary.bor} are borrowed, comprising {ready_dictionary.percent}% of the total.\n\n")
        for key, value in ready_dictionary.dict.items():
            formatted_file.write(f"{value['Repeats']}x: {key} {value['Value']} – {value['Origin']}.\nВ тексте встречается: {', '.join(value['Instances'])}\n\n")


def output_file_csv(expanded_output_path, ready_dictionary):
    with open(expanded_output_path, "w", encoding="utf-8", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Word", "Value", "Origin", "Repeats", "Instances"])
        for key, value in ready_dictionary.dict.items():
            instances_str = ', '.join(value["Instances"])
            csv_writer.writerow([key, value["Value"], value["Origin"], value["Repeats"], instances_str])








