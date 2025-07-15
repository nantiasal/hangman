import random
import signal
def timeout_handler(signum, frame):
    raise TimeoutError
words = ['python', 'banana', 'coffee', 'laptop','monitor', 'laptop', 'creator', 'database',]
secret_word = random.choice(words)
print("the random word :", secret_word)
guessed_letters = []
tries = 6
def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else: 
           display += "_ "  
    return display
total_attempts = 0    
signal.signal(signal.SIGALRM, timeout_handler)
   # Βασικό loop του παιχνιδιού
while tries > 0:
    print("\nWord:", display_word(secret_word, guessed_letters))
    print("Yoy have already choose:", " ".join(guessed_letters))
    try:
        signal.alarm(10)
        guess = input("Guess a letter, you have 10sec: ").lower()
        signal.alarm(0)
    except TimeoutError:
        print("Time over!!!")    
        tries -= 1
        continue
        
    
    total_attempts += 1

    if guess in guessed_letters:
        print("You have already choose it.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Right!")
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulation! You find it:", secret_word)
            print("Total tries:", total_attempts, "tries.")
            break
    else:
        tries -= 1
        print("ΛWrong. Left", tries, "tries.")

if tries == 0:
    print("\nLose! ΗThe right word was:", secret_word)
 
