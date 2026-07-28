import random

cards = ["A", "A", "B", "B"]
random.shuffle(cards)

print(cards)

a = int(input("Enter first position (0-3): "))
b = int(input("Enter second position (0-3): "))

if cards[a] == cards[b] and a != b:
    print("✅ Match Found!")
else:
    print("❌ Not a Match!")