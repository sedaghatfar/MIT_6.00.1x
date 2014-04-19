#PROBLEM 1: ENCRYPTION
#You'll now write a program to encrypt plaintext into ciphertext using the Caesar cipher.

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    
    both = string.ascii_lowercase + string.ascii_uppercase
    ignore = string.punctuation + ' ' + string.digits
    return dict(zip(both, (string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] \
    + string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift])))
    
#Next, define the function applyCoder, which applies a coder to a string of text.

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    
    return "".join([coder.get(letter,letter) for letter in text])
    
#Once you have written buildCoder and applyCoder, you should be able to use them to encode strings.

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

#PROBLEM 2: DECRYPTION

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    words = text.split(" ")
    for shift in range(26):
        coder = buildCoder(shift)
        if sum(isWord(wordList, applyCoder(word, coder)) for word in words) > len(words) / 2:
            return shift
    return 0
    
#decrypt Story

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    return applyShift(getStoryString(), findBestShift(loadWords(), getStoryString()))
