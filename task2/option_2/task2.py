import wikipediaapi


def animal_counting() -> dict:
        wiki_wiki = wikipediaapi.Wikipedia(
                language='ru',
                extract_format=wikipediaapi.ExtractFormat.WIKI)
        page = wiki_wiki.page("Категория:Животные по алфавиту")
        all_animals = page.categorymembers
        animals_list = list(all_animals.keys())
        return letter_count(animals_list)

def letter_count(list) -> dict:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        final_dict = {}
        for letter in list:
                if bool(set(alphabet).intersection(set(letter[0].lower()))):
                       continue
                if letter[0] in final_dict.keys():
                        final_dict[letter[0]] += 1
                else:
                        final_dict[letter[0]] = 1
        return final_dict

print(animal_counting())
