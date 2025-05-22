def string_derivation(word, target, P, Sigma, N, steps):
    if word == target:
        return True

    min_len = len([c for c in word if c in Sigma]) # numarul de terminale din cuvant este lungimea minima
                                                   # a unui cuvant ce poate fi generat din cuvantul curent
                                                   # (daca toate neterminalele ar deveni lambda)
    if min_len > len(target):
        return False

    for i in range(len(word)):
        if word[i] in N: # gasim primul neterminal din cuvant
            for p in P[word[i]]: # parcurgem productiile
                new_word = word[: i] + p + word[i + 1 :] # inlocuim neterminalul cu productia curenta
                if string_derivation(new_word, target, P, Sigma, N, steps): # verificam daca se poate obtine cuvantul curent
                    steps.insert(0, new_word) # adaugam cuvantul in lista derivarii
                    return True
            break

    return False

def derivation(target, G):
    N, Sigma, P, S = G
    steps = []
    found = string_derivation(S, target, P, Sigma, N, steps)
    if found:
        print(f"Derivare pentru '{target}': ", end = "")
        print(*steps, sep=', ')
    else:
        print(f"Nu exista derivare pentru '{target}'.")