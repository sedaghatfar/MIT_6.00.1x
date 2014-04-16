#RADIATION EXPOSURE
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    amt = 0
    while start < stop:
        amt += (f(start)*step)
        start += step
    return amt
    
#HANGMAN PART 1: IS THE WORD GUESSED?
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    newList = []
    for i in secretWord:
        newList.append(i)        
    recreated = []    
    for i in secretWord:
        if i in lettersGuessed:
            recreated.append(i)
    return recreated == newList
    
    
#PRINTING OUT THE USER'S GUESS

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    final =''
    newList = []
    for i in secretWord:
        newList.append(i)        
    recreated = []    
    for i in secretWord:
        if i in lettersGuessed:
            recreated.append(i)
        else:
            recreated.append(' _ ')
    final = ''.join(recreated)
    return final
    
#PRINTING OUT ALL AVAILABLE LETTERS  

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    return "".join([letter if letter not in lettersGuessed else "" for letter\
    in string.ascii_lowercase])
    
#HANGMAN PART 2: THE GAME

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+ str(len(secretWord)) +' letters long.')
    
    lettersGuessed = []
    mistakesMade = 0
    
    while mistakesMade < 8:
        availableLetters = getAvailableLetters(lettersGuessed)
        print('-------------')
        print('You have ' + str(8-mistakesMade) + ' guesses left.')
        print('Available letters: ' + availableLetters)
        guess = raw_input('Please guess a letter: ').lower()
        
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed += guess
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
              break
        else:
            lettersGuessed += guess
            mistakesMade += 1
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
 
    win = isWordGuessed(secretWord, lettersGuessed)
    print('-----------')
    if win:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was else. ')

