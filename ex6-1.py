fruit = input("Enter a fruit: ")
print(fruit[:])
index = len(fruit)
while index > 0:
    letter = fruit[index-1]
    print(letter)
    index = index - 1