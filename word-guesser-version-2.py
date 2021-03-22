import random

def main():
    word_list = ["antidisestablishmentarianism", "supercalifragilisticexpialidocious",
            "incomprehensibility", "honorificabilitudinitatibus",
            "subdermatoglyphic","onomatopoeia"]

    word = random.choice(word_list)
    count = 0
    guess = 15
    display = '-'*len(word)
    print("The word is " + display)
    while count < guess:
        user_input = input("Choose a letter (guess #{})".format(count+1))
        if len(user_input) == 1:
            num_occurrences = word.count(user_input)
            pos = -1;
            for i in range(num_occurrences):
                pos = word.find(user_input, pos+1)
                display = display[:pos] + user_input +display[pos+1:]


                if '-' not in display:
                    print("Congratulations!")
                    break
            print(display)
            count += 1

    if '-' in display:
        print("You're lost. The word is " + word)

    loop()

def loop():
    is_played = input("Do you want to play the game again? Y / N \n")

    while is_played not in ["y", "Y", "n", "N"]:
        is_played = input("Do you want to play the game again? Y / N \n")
    if is_played == "y" or "Y":
        main()
    if is_played == "n" or "N":
        exit()

if __name__ == "__main__":
    main()
