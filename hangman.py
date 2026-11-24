import random

current_word = ["python", "coding", "script", "ArithmeticError", "hangman", "programming", "function", "variable", "loop", "condition", "list", "dictionary", "tuple", "set", "string", "integer", "float", "boolean", "class", "object"]
selected_word = random.choice(current_word)
guessed_words = set()
max_attempts = 6

while max_attempts > 0:
    # Show guessed letters and underscores for hidden ones
    display = [letter if letter in guessed_words else "_" for letter in selected_word]
    print(" ".join(display))

    if "_" not in display:
        print("You won!")
        break

    predict_word = input("Enter a word :  ").lower()
    guessed_words.add(predict_word)

    if predict_word not in selected_word:
        max_attempts -= 1
        print(f"Wrong! Attempts left: {max_attempts}")

if max_attempts == 0:
    print(f"Game over! The word was {selected_word}.")