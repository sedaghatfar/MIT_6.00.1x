#WORD SCORES

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score
#DEALING WITH HANDS

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handcopy = hand.copy()
    for char in word:
        if char in handcopy.keys():
            handcopy[char] -= 1
    newhand={ key : handcopy[key] for key in handcopy.keys() if handcopy[key]!=0}
    return newhand
    
#VALID WORDS

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handcopy=hand.copy()
    for char in word:
    	if char not in handcopy or handcopy[char]<=0:
    		return False
    	else:
    		handcopy[char] -=1
    if word in wordList:
    	return True
    return False
    
#HAND LENGTH

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    count = 0
    for keys in hand.keys():
        count += hand[keys]
    return count

#PLAYING A HAND

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    score = 0
    while calculateHandlen(hand) > 0:
    	print 'Current Hand: ',
    	displayHand(hand)
    	word = str(raw_input('Enter word, or a "." to indicate that you are finished: '))
    	if word == '.':
    		print 'Goodbye! Total score: '+str(score)+' points.'
    		return
    	if isValidWord(word,hand,wordList):
    		score += getWordScore(word,n)
    		hand=updateHand(hand,word)    		
    		print '"'+word+'" earned '+str(getWordScore(word,n))+' points. Total: '+str(score)+' points'
    	else:
    		print 'Invalid word, please try again.'
    print 'Run out of letters. Total score: '+str(score)+' points.'

#PLAYING A GAME

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    preChoice = 'f'
    while True:
    	choice = str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
    	if choice == 'n':
    		hand=dealHand(HAND_SIZE)
    		handCopy=hand.copy()
    		playHand(handCopy,wordList,HAND_SIZE)
    		print
    		preChoice = choice
    	elif choice == 'r': 
		if preChoice == 'f':
    			print 'You have not played a hand yet. Please play a new hand first!'
    			print
    		else:
    			handCopy=hand.copy()
   			playHand(handCopy,wordList,HAND_SIZE)
   			print
    	elif choice == 'e':
    		return
    	else:
    		print 'Invalid command.'
    		
#COMPUTER CHOOSES A WORD

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    bestScore = 0

    bestWord = None

    for word in wordList:

        if isValidWord(word, hand, wordList):

            score = getWordScore(word, n)

            if score > bestScore:

                bestScore = score
                bestWord = word

    return bestWord
    
#COMPUTER PLAYS A HAND

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    bestScore = 0

    bestWord = None

    for word in wordList:

        if isValidWord(word, hand, wordList):

            score = getWordScore(word, n)

            if score > bestScore:

                bestScore = score
                bestWord = word

    return bestWord



def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    def displayHand2(hand):
      displayed = ''
      for letter in hand.keys():
        for j in range(hand[letter]):
             displayed += letter + ' '
      return displayed
    totalScore = 0
    handed = hand.copy()
    while compChooseWord(handed, wordList, n):
        print "Current Hand:  " + displayHand2(handed)
        askInput = compChooseWord(handed, wordList, n)
        scored = getWordScore(askInput, n)
        totalScore += scored
        print '"'+ askInput + '" ' + "earned " + str(scored) + " points. Total: " + str(totalScore) + " points\n"
        handed = updateHand(handed, askInput)
    if sum(handed.values()) != 0:
      print "Current Hand:  " + displayHand2(handed)
    print "Total score: " + str(totalScore) + " points"
    
#YOU AND YOUR COMPUTER

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    def displayHand2(hand):
      displayed = ''
      for letter in hand.keys():
            for j in range(hand[letter]):
                 displayed += letter + ' '
      return displayed
    hand = False
    while True:
      ans = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
      if ans == "n":
        hand = dealHand(HAND_SIZE)

        tester1 = True
        while tester1:
          ans2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
          if ans2 == "u":
            playHand(hand, wordList, HAND_SIZE)
            tester1 = False
          elif ans2 == "c":
            compPlayHand(hand, wordList, HAND_SIZE)
            tester1 = False
          else:
            print "Invalid command."
      elif ans == "r":
        if hand:
          ans2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
          if ans2 == "u":
            playHand(hand, wordList, HAND_SIZE)
          elif ans2 == "c":

            compPlayHand(hand, wordList, HAND_SIZE)
          else:
            print "Invalid command."
        else:
          print "You have not played a hand yet. Please play a new hand first!"
      elif ans == "e":
        break
      else:
        print "Invalid command."
