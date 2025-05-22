import random

words = ['python', 'guitar', 'banana', 'hangman']
word = random.choice(words)
guessed = ['_'] * len(word)
tries = 6

print("Từ cần đoán có", len(word), "chữ cái.")

while tries > 0 and '_' in guessed:
    print(" ".join(guessed))
    letter = input("Đoán một chữ cái: ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        tries -= 1
        print(f"Sai rồi! Còn {tries} lần đoán.")

if '_' not in guessed:
    print("Bạn đã thắng! Từ đó là:", word)
else:
    print("Bạn thua! Từ đó là:", word)
