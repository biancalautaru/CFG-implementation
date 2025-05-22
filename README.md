# CFG implementation

Acest proiect are 4 componente principale:
- **definirea gramaticii independente de context (CFG)** date de `S -> aSb | λ`
  - Aceasta generează limbajul L = {a<sup>n</sup>b<sup>n</sup> | n ≥ 0}.
- un **generator de cuvinte** ce fac parte din această gramatică
  - Generatorul creează maxim 10 cuvinte de lungime maximă 10.
- o funcție ce afișează pașii de **derivare a unui cuvânt dat**
  - Sunt afișate cuvintele obținute prin aplicarea succesivă a producțiilor până la obținerea cuvântului dorit.
- o funcție ce testează **dacă un cuvânt face sau nu parte din gramatica dată**.

## 💻 Rulare

1. clonare repository:
   ```
   git clone https://github.com/biancalautaru/CFG-implementation
   ```
2. rulare program:
   ```
   python3 main.py
   ```

---

## 📖 Exemplu output

```
task 1: ({'S'}, {'b', 'a'}, {'S': {'', 'aSb'}}, 'S')

task 2: ['aabb', 'aaabbb', 'aaaabbbb', 'aaaaabbbbb', 'ab', '']

task 3:
Derivare pentru 'aabb': aSb, aaSbb, aabb
Derivare pentru 'aaabbb': aSb, aaSbb, aaaSbbb, aaabbb
Derivare pentru 'aaaabbbb': aSb, aaSbb, aaaSbbb, aaaaSbbbb, aaaabbbb
Derivare pentru 'aaaaabbbbb': aSb, aaSbb, aaaSbbb, aaaaSbbbb, aaaaaSbbbbb, aaaaabbbbb
Derivare pentru 'ab': aSb, ab
Derivare pentru '': 

task 4:
'aabb' apartine gramaticii.
'aaabbb' apartine gramaticii.
'aaaabbbb' apartine gramaticii.
'aaaaabbbbb' apartine gramaticii.
'ab' apartine gramaticii.
'' apartine gramaticii.
'aabbbb' nu apartine gramaticii.
'aba' nu apartine gramaticii.
'aaaaaabbbbbb' apartine gramaticii.
'aaaaaabbbcbb' nu apartine gramaticii.
```
