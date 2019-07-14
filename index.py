# -*- coding: utf8 -*-
import random
import json

#Ouvre un fichier JSON et le converti en list python
def read_value_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
    for entry in data:
        values.append(entry[key])
    return values

#Efface les espaces avant et après la chaîne de caractères
def clean_strings(sentences):
    cleaned = []
    for sentence in sentences:
        cleaned.append(sentence.strip())
    return cleaned

#return un item aléatoire d'une list
def random_item_in(list):
    return list[random.randint(0, len(list) -1 )]

#return une valeur aléatoire d'un fichier JSON
def random_value(file, key):
    return random_item_in(clean_strings(read_value_from_json(file, key)))

#Citation aléatoire
def random_quote():
    return random_value("quotes.json", "quote")

#Personnage aléatoire
def random_character():
    return random_value("characters.json", "character")

#Met en majuscule la première lettre du mot
def capitalize(word):
    return word.capitalize()

#Affiche une sentence aléatoire
def print_random_sentence():
    print("{} a dit : {}".format(capitalize(random_character()), capitalize(random_quote())))

def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ?'
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == "B":
            break

if __name__ == "__main__":
    main_loop()