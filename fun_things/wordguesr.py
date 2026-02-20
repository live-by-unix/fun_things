import random
user_input = 7

words_list = [
    "mountain", "river", "forest", "ocean", "desert", 
    "valley", "canyon", "island", "glacier", "volcano", 
    "meadow", "tundra", "savanna", "prairie", "lagoon", 
    "waterfall", "cavern", "plateau", "swamp", "archipelago"
]
random_word = random.choice (words_list)
code_word_hint= "This message should not show, so STOP HACKING YOU HACKER"

if random_word == "mountain":
    code_word_hint= "Summit"
elif random_word == "river":
    code_word_hint = "Flow"
elif random_word == "forest":
    code_word_hint = "Greenery"
elif random_word == "ocean":
    code_word_hint = "Coastal"
elif random_word == "desert":
    code_word_hint = "Blazing"
elif random_word == "valley":
    code_word_hint = "Farming"
elif random_word == "canyon":
    code_word_hint = "Ravine"
elif random_word == "island":
    code_word_hint = "Hawaii"
elif random_word == "glacier":
    code_word_hint = "Ice"
elif random_word == "volcano":
    code_word_hint = "Eruption"
elif random_word == "meadow":
    code_word_hint = "Grazing"
elif random_word == "tundra":
    code_word_hint = "Polar"
elif random_word == "savanna":
    code_word_hint = "Grassland"
elif random_word == "prairie":
    code_word_hint = "Plains"
elif random_word == "lagoon":
    code_word_hint = "Reef"
elif random_word == "waterfall":
    code_word_hint = "Rapid"
elif random_word == "cavern":
    code_word_hint = "Cave"
elif random_word == "plateau":
    code_word_hint = "Highland"
elif random_word == "swamp":
    code_word_hint = "Bog"
elif random_word == "archipelago":
    code_word_hint = "chain"
else:
    print("This message shouldn't appear YOU HACKER")

print("Welcome to WordGuesr.")
print("You get 5 guesses to guess a all-lowercase word. Type wordpls to get the word.")
print(f"UR HINT IS : {code_word_hint}")


attempts = 0

for i in range (5):
    user_input = input("Enter your guess :").lower().strip()
    attempts += 1
    
    if user_input == 'wordpls':
        print(f"{random_word} is your word.")
    
    if user_input == random_word:
        print("Congrats! You won")
        break
    else:
        if attempts < 5:
            print("Incorrect! Try again.")

if attempts == 5 and user_input != random_word:
    print(f"Game Over! The word was {random_word}.")