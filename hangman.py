
import string , random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append('_ ')

    return "".join(guessed_word)    


    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    for letter in letters_guessed:
        letters = letters.replace(letter, "")
    return letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman")
    print(f"I am thinking of a word that is {len(secret_word)} long.")
    print("---------------------------------------")

    while True:
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guessed_letter = input("Please guess a letter: ")[0]
        if not str.isalpha(guessed_letter):
            warnings -= 1
            if warnings <= 0:
                guesses -= 1
            print(f"Oops! That not a vaild letter. You have {0 if  warnings <= 0  else warnings} wanings left.")
            print(get_guessed_word(secret_word, letters_guessed))
      
        else:
        
            if str.lower(guessed_letter) not in get_available_letters(letters_guessed):
                warnings -= 1
                if warnings <= 0:
                    guesses -= 1
                print(f"Oops! You've already guessed that letter. You have {0 if  warnings <= 0  else warnings} warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
        
          
            else:
                letters_guessed.append(str.lower(guessed_letter))  
                if str.lower(guessed_letter) in secret_word:
                    print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            
                else:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    guesses -= 1
        
        print("-----------------------------------------")  

       
      
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations you won the game.")
            unique_letters = set(secret_word)
            print(f"Your Score is {len(unique_letters) * guesses}")
            break
        
        if guesses <= 0:
            print("Sorry, You lost the game.")
            print(f"The word was {secret_word}.")
            break

if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)



