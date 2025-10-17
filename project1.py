#  PROJECT 1 ---> Fake & Funny News Headlines Generator.

# STEP 1 --> import the random module
import random

# STEP 2 --> create subjects
subjects = [
    "Shahrukh Khan", "Nitish Kumar", "Lalu Yadav", "Virat Kohli", "A group of Monkeys",
    "A Thief", "Donald Trump"
]

actions = [
    "launches", "cancels", "declares war on", "celebrates", "dances with", "ate", "stealing"
]

places_or_things = [
    "the India Gate",
    "the Red Fort",
    "a plate of Samosa",
    "IPL match",
    "inside parliament",
    "in stadium",
    "group of people",
    "mango"
]

# STEP 3 --> start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another funny headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

# STEP 4 --> Thanking You message.
print("\nThanks for using.")
