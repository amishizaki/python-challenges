# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = input("Give me a string to alphabetize: ")
make_list = []

for letter in word:
    make_list.append(letter)

print(make_list)

alphabetize = sorted(make_list)
print(alphabetize)

bring_together = ' '.join(alphabetize)
print(bring_together)
