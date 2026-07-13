# Write a program to create a dictionary of Hindi Words with values as their English translation. Provide a userwith an option to look it up!

Words = {
    "Billi": "Cat",
    "Kutta": "Dog",
    "madad": "Help",
    "Kursi": "Chair",
    "Ghar": "House"
}

word = input("Enter a Hindi word:")

print("Meaning:", Words.get(word, "Word not found in dictionary"))