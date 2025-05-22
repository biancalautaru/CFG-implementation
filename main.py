from string_generator import generator
from derivation import derivation
from membership_tester import test

if __name__ == "__main__":
    # task 1:
    N = {'S'} # multimea neterminalelor
    Sigma = {'a', 'b'} # multimea terminalelor
    P = {'S' : {'aSb', ''}} # multimea productiilor ('' este lambda)
    S = 'S' # simbolul de start
    G = (N, Sigma, P, S) # gramatica ceruta
    print(f"task 1: {G}\n")

    # task 2:
    strings_from_cfg = generator(G)
    print(f"task 2: {strings_from_cfg}\n")

    # task 3:
    print("task 3:")
    for string in strings_from_cfg:
        derivation(string, G)
    print()

    # task 4:
    print("task 4:")
    for string in strings_from_cfg:
        test(string, G)
    test("aabbbb", G)
    test("aba", G)
    test("aaaaaabbbbbb", G)
    test("aaaaaabbbcbb", G)