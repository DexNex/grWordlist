import random
import subprocess

# Fungsi untuk menghasilkan angka acak dalam rentang tertentu
def generate_random_numbers(start, end, output_file):
    with open(output_file, 'w') as f:
        for i in range(start, end + 1):
            f.write(str(i) + '\n')

# Fungsi untuk menghasilkan kombinasi kostum dari angka
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
            if spaces == 'ya':
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
    # Gunakan subprocess untuk menjalankan figlet dan lolcat untuk output teks yang bergaya
    figlet_text = subprocess.Popen(['figlet', 'grWordlist'], stdout=subprocess.PIPE, text=True)
    figlet_text = subprocess.Popen(['lolcat'], stdin=figlet_text.stdout, text=True)
    figlet_text.communicate()

    print("\nby DEXNEX")
    print("V1.0")
    print("Instagram : @one.persen.man\n")

if __name__ == "__main__":
    print_welcome_message()

    print("Pilih opsi untuk wordlist:")
    print("1. Number")
    print("2. All")

    choice = input("Masukkan pilihan Anda: ")

    if choice == '1':
        print("Pilih opsi untuk Number:")
        print("1. Acak")
        print("2. Kostum")

        sub_choice = input("Masukkan pilihan Anda: ")

        if sub_choice == '1':
            range_input = input("Masukkan rentang (misalnya 1-1000): ")
            start, end = map(int, range_input.split('-'))
            output_file = "random_numbers.txt"
            generate_random_numbers(start, end, output_file)
            print(f"Wordlist angka acak telah dibuat dan disimpan di {output_file}")

        elif sub_choice == '2':
            number = input("Masukkan nomor (misalnya 1234): ")
            limit = int(input("Jumlah baris: "))
            output_file = "custom_numbers.txt"
            generate_custom_numbers(number, limit, output_file)
            print(f"Wordlist kombinasi kostum angka telah dibuat dan disimpan di {output_file}")

        else:
            print("Pilihan tidak valid.")

    elif choice == '2':
        print("Pilih opsi untuk All:")
        print("1. Random")
        print("2. Kostum")

        sub_choice = input("Masukkan pilihan Anda: ")

        if sub_choice == '1':
            number = input("Nomor: ")
            alphabet = input("Abjad: ")
            spaces = input("Spasi atau tidak (ya/tidak): ")
            characters = input("Karakter: ")
            num_lines = int(input("Jumlah baris: "))
            output_file = "random_all.txt"
            generate_random_all(number, alphabet, spaces, characters, num_lines, output_file)
            print(f"Wordlist acak telah dibuat dan disimpan di {output_file}")

        elif sub_choice == '2':
            number = input("Nomor: ")
            alphabet = input("Abjad: ")
            characters = input("Karakter: ")
            num_lines = int(input("Jumlah baris: "))
            output_file = "custom_all.txt"
            generate_custom_all(number, alphabet, characters, num_lines, output_file)
            print(f"Wordlist kostum telah dibuat dan disimpan di {output_file}")

        else:
            print("Pilihan tidak valid.")

    else:
        print("Pilihan tidak valid.")
