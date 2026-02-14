from random import choice


def random(word):
    return choice(word)


names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park","in the kitchen","in the office"]
print("Hello this is your first random sentence:)")
while True:
    random_name = random(names)
    random_place = random(places)
    random_verb = random(verbs)
    random_noun = random(nouns)
    random_adverb = random(adverbs)
    random_detail = random(details)
    print(f"{random_name} from {random_place} {random_verb} {random_noun} {random_adverb} {random_detail}")
    input("Click [Enter] to generate new one")


