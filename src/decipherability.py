def find_decipherable_words_above_threshold(Dico, threshold, mastered_relations, include_words_with_muted_letters=False):
    partially_decipherable_words = {}
    for word in Dico:
        percentage = compute_decipherability_percentage(Dico[word], mastered_relations, include_words_with_muted_letters)
        if percentage >= threshold:
            partially_decipherable_words[word] = percentage
    return partially_decipherable_words

def compute_decipherability_percentage(word_relations, mastered_relations, ignore_muted_letters=False):
    if ignore_muted_letters:
        for relation in word_relations:
            if relation[-1] == '#':
                word_relations.remove(relation)
    word_relations_set = set(word_relations)
    mastered_relations_set = set(mastered_relations)
    
    nb_word_relations = len(word_relations_set)
    nb_decipherable_relations = 0
    for relation in word_relations_set:
        if relation in mastered_relations_set:
            nb_decipherable_relations += 1
    return nb_decipherable_relations / nb_word_relations

def find_words_with_non_mastered_LO(Dico, LO, mastered_relations):
    words_with_LO = select_words_with_LO(Dico, LO)
    relations = mastered_relations + [LO]
    return find_decipherable_words_above_threshold(words_with_LO, threshold=1.0, mastered_relations=relations)

def select_words_with_LO(Dico, LO):
    words_with_LO = {word: Dico[word] for word in Dico if LO in Dico[word]}
    return words_with_LO