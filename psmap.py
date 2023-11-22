import itertools
import json

print('''\033[36m                                                     
 ████████   █████  █████████████    ██████   ████████ 
░░███░░███ ███░░  ░░███░░███░░███  ░░░░░███ ░░███░░███
 ░███ ░███░░█████  ░███ ░███ ░███   ███████  ░███ ░███
 ░███ ░███ ░░░░███ ░███ ░███ ░███  ███░░███  ░███ ░███
 ░███████  ██████  █████░███ █████░░████████ ░███████ 
 ░███░░░  ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░░░  ░███░░░  
 ░███                                        ░███     
 █████                                       █████    
░░░░░                                       ░░░░░       
                                                               		 
                     \033[36m By Lucas R. Luque 
''')



# Function to gather user information
def get_user_info():
    user_info = {}

    print("Please provide the following information (press ENTER to skip if unknown):")

    user_info['name'] = input("\n\033[36m[?] Name: ") or None
    user_info['surname_1'] = input("\n\033[36m[?] First Surname: ") or None
    user_info['surname_2'] = input("\n\033[36m[?] Second Surname: ") or None
    user_info['birth_day'] = input("\n\033[36m[?] Birth Date Day (num): ") or None
    user_info['birth_month'] = input("\n\033[36m[?] Birth Date Month (num): ") or None
    user_info['birth_year'] = input("\n\033[36m[?] Birth Date Year (num): ") or None

    pet_names = input("\n\033[36m[?] Pet names (comma-separated): ")
    user_info['pets'] = pet_names.split(',') if pet_names else None

    children_names = input("\n\033[36m[?] Children names (comma-separated): ")
    user_info['children'] = children_names.split(',') if children_names else None

    user_info['phone_number'] = input("\n\033[36m[?] Phone number: ") or None

    other_words = input("\n\033[36m[?] Other relevant words (comma-separated): ")
    user_info['other_words'] = other_words.split(',') if other_words else None

    return user_info

# Function to save user information to a JSON file
def save_to_json(data, filename='user_info.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"\n\033[36m[!] User information has been saved to {filename}")

# Function to generate wordlist
def generate_wordlist(user_info, file_name):
    word_list = []
    keys = [key for key, value in user_info.items() if value and value != '-']

    for r in range(2, 4):
        for combination in itertools.combinations(keys, r):
            for permuted_data in itertools.permutations(combination):
                wordLower = ''
                wordUpper = ''
                wordCap = ''

                for item in permuted_data:
                    if isinstance(user_info[item], list):
                        wordLower += ''.join(user_info[item]).lower()
                        wordUpper += ''.join(user_info[item]).upper()
                        wordCap += ''.join(user_info[item]).capitalize()
                    else:
                        wordLower += str(user_info[item]).lower()
                        wordUpper += str(user_info[item]).upper()
                        wordCap += str(user_info[item]).capitalize()

                word_list.extend([wordLower, wordUpper, wordCap])

    return word_list

# Get user information
user_data = get_user_info()

# Prompt user for the desired filename to save the JSON file
file_name = input("\n\033[36m[?] Enter the desired filename (without extension) for JSON file: ") or 'user_info'

# Save user information to a JSON file
json_file_name = f"{file_name}.json"
save_to_json(user_data, json_file_name)

# Generate wordlist from user information
wordlist = generate_wordlist(user_data, file_name)

# Save wordlist to a text file using the same name as the JSON file
wordlist_file_name = f"{file_name}_wordlist.txt"
with open(wordlist_file_name, 'w') as file:
    for word in wordlist:
        file.write(f"{word}\n")

print(f"\n\033[36m[!] Wordlist has been generated and saved to '{wordlist_file_name}'")
