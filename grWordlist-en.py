import random
import subprocess

# Function to generate random numbers within a specified range
def generate_random_numbers(start, end, output_file):
    with open(output_file, 'w') as f:
        for i in range(start, end + 1):
            f.write(str(i) + '\n')

# Function to generate custom combinations of numbers
def generate_custom_numbers(number, limit, output_file):
    digits = [str(digit) for digit in range(10)]
    with open(output_file, 'w') as f:
        for _ in range(limit):
            custom_number = ''.join(random.choices(digits, k=len(number)))
            f.write(custom_number + '\n')

def generate_random_all(number, alphabet, spaces, characters, num_lines, output_file):
    def generate_combinations(length):
        return [''.join(random.choices(number, k=length)) for _ in range(num_lines)]

    def shuffle_list(lst):
        return random.sample(lst, len(lst))

    numbers = generate_combinations(len(number))
    alphabets = shuffle_list(generate_combinations(len(alphabet)))
    chars = shuffle_list(generate_combinations(len(characters)))

    with open(output_file, 'w') as f:
        for _ in range(num_lines):
            num = random.choice(numbers)
            alpha = random.choice(alphabets)
            char = random.choice(chars)
            if spaces == 'yes':
                line = f"{num} {alpha} {char}"
            else:
                line = f"{num}{alpha}{char}"
            f.write(line + '\n')

def generate_custom_all(number, alphabet, characters, num_lines, output_file):
    def generate_repeated_patterns(lst, times):
        return [item * times for item in lst]

    numbers = generate_repeated_patterns([number], 1)
    alphabets = generate_repeated_patterns([alphabet], 1)
    chars = generate_repeated_patterns([characters], 1)

    with open(output_file, 'w') as f:
        for _ in range(num_lines):
            f.write(f"{number} {alphabet} {characters}\n")
            f.write(f"{alphabet} {number} {characters}\n")
            f.write(f"{number}{alphabet}{characters}\n")
            f.write(f"{characters}{number}{alphabet}\n")

def print_welcome_message():
    # Use subprocess to run figlet and lolcat for styled text output
    figlet_text = subprocess.Popen(['figlet', 'grWordlist'], stdout=subprocess.PIPE, text=True)
    figlet_text = subprocess.Popen(['lolcat'], stdin=figlet_text.stdout, text=True)
    figlet_text.communicate()

    print("\nby DEXNEX")
    print("V1.0")
    print("Instagram : @one.persen.man\n")

if __name__ == "__main__":
    print_welcome_message()

    print("Select an option for the wordlist:")
    print("1. Number")
    print("2. All")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Select an option for Number:")
        print("1. Random")
        print("2. Custom")

        sub_choice = input("Enter your choice: ")

        if sub_choice == '1':
            range_input = input("Enter range (e.g., 1-1000): ")
            start, end = map(int, range_input.split('-'))
            output_file = "random_numbers.txt"
            generate_random_numbers(start, end, output_file)
            print(f"Random number wordlist has been created and saved to {output_file}")

        elif sub_choice == '2':
            number = input("Enter number (e.g., 1234): ")
            limit = int(input("Number of lines: "))
            output_file = "custom_numbers.txt"
            generate_custom_numbers(number, limit, output_file)
            print(f"Custom number combination wordlist has been created and saved to {output_file}")

        else:
            print("Invalid choice.")

    elif choice == '2':
        print("Select an option for All:")
        print("1. Random")
        print("2. Custom")

        sub_choice = input("Enter your choice: ")

        if sub_choice == '1':
            number = input("Number: ")
            alphabet = input("Alphabet: ")
            spaces = input("Spaces or not (yes/no): ")
            characters = input("Characters: ")
            num_lines = int(input("Number of lines: "))
            output_file = "random_all.txt"
            generate_random_all(number, alphabet, spaces, characters, num_lines, output_file)
            print(f"Random wordlist has been created and saved to {output_file}")

        elif sub_choice == '2':
            number = input("Number: ")
            alphabet = input("Alphabet: ")
            characters = input("Characters: ")
            num_lines = int(input("Number of lines: "))
            output_file = "custom_all.txt"
            generate_custom_all(number, alphabet, characters, num_lines, output_file)
            print(f"Custom wordlist has been created and saved to {output_file}")

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")
