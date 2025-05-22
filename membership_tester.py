from derivation import string_derivation

def test(target, G):
    N, Sigma, P, S = G
    if string_derivation(S, target, P, Sigma, N, []):
        print(f"'{target}' apartine gramaticii.")
    else:
        print(f"'{target}' nu apartine gramaticii.")