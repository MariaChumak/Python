from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
lst_0 = []

def get_jokes(n, flag = False):
    for i in range(n):
        random_1 = choice(nouns)
        random_2 = choice(adverbs)
        random_3 = choice(adjectives)
        joke = f'{random_1} {random_2} {random_3}'
        lst = []
        print(joke)
        if flag == True:
            lst = joke.split()
            for noun in nouns:
                for fun in lst:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in lst:
                    if adverbs == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for fun in lst:
                    if adjective == fun:
                        adjectives.remove(adjective)

get_jokes(n = 3, flag = True)