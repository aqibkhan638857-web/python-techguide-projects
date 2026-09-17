#Project 3 "Password Generator"
import random
import string

print("--- Robust Password Generator ---")

# 1. Get password configuration inputs from the user
try:
    length = int(input("Enter desired password length (minimum 4): "))
    if length < 4:
        print("Password length too short! Setting it to a safe default of 12.")
        length = 12
except ValueError:
    print("Invalid number entered! Using default length of 12.")
    length = 12

print("\nInclude which characters? (y/n)")
use_upper   = input("Uppercase letters (A-Z)? ").strip().lower() == 'y'
use_lower   = input("Lowercase letters (a-z)? ").strip().lower() == 'y'
use_digits  = input("Numbers (0-9)? ").strip().lower() == 'y'
use_symbols = input("Special characters (!@#$%^&*)? ").strip().lower() == 'y'

# 2. Build the pool of available characters based on choices
character_pool = ""
mandatory_chars = []

if use_upper:
    character_pool += string.ascii_uppercase
    mandatory_chars.append(random.choice(string.ascii_uppercase))
if use_lower:
    character_pool += string.ascii_lowercase
    mandatory_chars.append(random.choice(string.ascii_lowercase))
if use_digits:
    character_pool += string.digits
    mandatory_chars.append(random.choice(string.digits))
if use_symbols:
    character_pool += string.punctuation
    mandatory_chars.append(random.choice(string.punctuation))

# Default fallback if the user types 'n' to every option
if character_pool == "":
    print("\nNo characters selected! Defaulting to alphanumeric password.")
    character_pool = string.ascii_letters + string.digits
    mandatory_chars = [random.choice(string.ascii_lowercase), random.choice(string.digits)]

# 3. Generate the password string
# Fill remaining empty spaces with completely random selections from the pool
remaining_length = length - len(mandatory_chars)
random_picks = [random.choice(character_pool) for _ in range(remaining_length)]

# Combine mandatory structural characters with general random picks
password_list = mandatory_chars + random_picks

# Shuffle everything together so mandatory characters don't always sit at the front
random.shuffle(password_list)
final_password = "".join(password_list)

# 4. Print results
print("\n" + "=" * 30)
print(f"Generated Password: {final_password}")
print("=" * 30)