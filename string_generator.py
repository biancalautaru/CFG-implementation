import random

def generate_string(word, max_len, P, Sigma, N, strings, num_strings):
    if len(strings) >= num_strings: # generam maxim num_strings stringuri
        return

    min_len = len([c for c in word if c in Sigma]) # numarul de terminale din cuvant este lungimea minima
                                                   # a unui cuvant ce poate fi generat din cuvantul curent
    if min_len > max_len:
        return

    if all(c in Sigma for c in word): # avem un cuvant format doar din terminale
        strings.append(word)
        return

    for i in range(len(word)):
        if word[i] in N: # gasim primul neterminal din cuvant
            productions = list(P[word[i]])
            random.shuffle(productions) # amestecam random productiile
            for p in productions:       # si le parcurgem pe rand
                new_word = word[: i] + p + word[i + 1 :] # inlocuim neterminalul cu productia curenta
                generate_string(new_word, max_len, P, Sigma, N, strings, num_strings) # apel recursiv
            break

def generator(G):
    N, Sigma, P, S = G
    strings = []
    generate_string(S, 10, P, Sigma, N, strings, 10)
    return strings