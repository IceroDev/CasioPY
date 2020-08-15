voyelles = set('aeiouy')
mot = input("\n\n\n\n\n\nEntrez un mot : ")
found = {}
for letter in mot:
    if letter in voyelles:
        found.setdefault(letter, 0)
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k,'| a ete trouve', v, 'x')