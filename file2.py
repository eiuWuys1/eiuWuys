import random

choices = ['kéo', 'búa', 'bao']
user = input("Chọn (kéo/búa/bao): ").lower()
bot = random.choice(choices)

print(f"Bot chọn: {bot}")
if user == bot:
    print("Hòa!")
elif (user == 'kéo' and bot == 'bao') or \
     (user == 'búa' and bot == 'kéo') or \
     (user == 'bao' and bot == 'búa'):
    print("Bạn thắng!")
else:
    print("Bot thắng!")
