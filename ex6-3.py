def count_letter(word, search):
    count = 0
    for letter in word:
        if letter == search:
            count += 1
    print(count)
fruit = input("Enter a fruti: ")
chosen = input("Which letter should I look for: ")
count_letter(fruit, chosen)