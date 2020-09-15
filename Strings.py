phrase = "Giraffe Academy"
print(phrase + " is cool")

print("Giraffe\n Academy")  # \n \" --> inserts new line
print("Giraffe\"Academy")

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))  # 15
print(phrase[0])  # G
print(phrase.index("Academy"))  # 8
print(phrase.replace("Giraffe", "Elephant"))  # Elephant Academy