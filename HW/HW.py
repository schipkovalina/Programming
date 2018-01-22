#Вариант3
# К сожалению, компьютер никак не воспринимает просто название файла, поэтому везде написаны пути

import random

def noun():
    with open("/Users/alina/Documents/GitHub/Programming/nouns.txt", 'r', encoding='utf-8') as f:
        nouns = []
        for line in f:
            nouns.append(line.strip())
    return random.choice(nouns)


def adverb():
    with open("/Users/alina/Documents/GitHub/Programming/adverbs.txt", 'r', encoding='utf-8') as f:
        adverbs = []
        for line in f:
            adverbs.append(line.strip())
    return random.choice(adverbs)


def intensifier(adverbs):
    with open("/Users/alina/Documents/GitHub/Programming/intensifiers.txt", 'r', encoding='utf-8') as f:
        intensifiers = []
        for line in f:
            intensifiers.append(line.strip())
    random_intensifier = random.choice(intensifiers)
    result = random_intensifier + ' ' + adverbs
    return result


def adjective(word):
    with open("/Users/alina/Documents/GitHub/Programming/adjectives.txt", 'r', encoding='utf-8') as f:
        adjectives = []
        for line in f:
            adjectives.append(line.strip())
    return random.choice(adjectives) + ' ' + word


def verb_of_thought(subj):
    with open("/Users/alina/Documents/GitHub/Programming/verbs_of_thought.txt", 'r', encoding='utf-8') as f:
        verbs_of_thought = []
        for line in f:
            verbs_of_thought.append(line.strip())
    return subj + ' ' + random.choice(verbs_of_thought)


def verb_transitive(subj):
    with open("/Users/alina/Documents/GitHub/Programming/verbs_transitive.txt", 'r', encoding='utf-8') as f:
        verbs_transitive = []
        for line in f:
            verbs_transitive.append(line.strip())
    return subj + ' ' + random.choice(verbs_transitive)

def verb_imperative():
    with open("/Users/alina/Documents/GitHub/Programming/verbs_imperative.txt", 'r', encoding='utf-8') as f:
        verbs_imperative = []
        for line in f:
            verbs_imperative.append(line.strip())
    return random.choice(verbs_imperative)


def random_sentence():
    sentence1 = verb_of_thought(adjective(noun())) + ',что ' + verb_transitive(adjective(noun())) + ' ' + intensifier(adverb()) + '.'
    sentence2 = verb_of_thought(adjective(noun())) + ',что ' + verb_transitive(adjective(noun())) + ' ' + intensifier(adverb()) + '?'
    sentence3 = verb_of_thought(adjective(noun()) + ' не') + ',что ' + verb_transitive(adjective(noun())) + ' ' + intensifier(adverb()) + '.'
    sentence4 = 'Если ' + verb_of_thought(adjective(noun())) + ',то ' + verb_transitive(adjective(noun())) + ' ' + intensifier(adverb()) + '.'
    sentence5 = adjective(noun()) + ', ' + verb_imperative() + ',что ' + verb_transitive(adjective(noun())) + ' ' + intensifier(adverb()) + '!'            

    return random.choice([sentence1,sentence2,sentence3,sentence4,sentence5])



num_of_sents = 5 
for i in range(num_of_sents):  
    sentence = random_sentence() 
    sentence = sentence.capitalize() 
    print(sentence, end=' ') 
    
