#Hangman game for 2 players

def chancecount(astring):
    chance = 0
    if len(astring) >= 20:
        chance = 20
    elif len(astring) < 10:
        chance = 10
    else:
        chance = len(astring)+5
    return chance

def feedback(char, astring):
    if char in astring:
        return True
    return False

def guess(astring_stars, char, astring):
    for i in range(len(astring)):
        if astring[i] == char:
            astring_stars = wordSoFar(astring_stars, i, char)
    return astring_stars

def wordSoFar(astring_stars, num_index, char):
    word_so_far = astring_stars[:num_index]+ str(char)+ astring_stars[num_index+1:]
    return word_so_far


play = "y"
while play == "y":
    word = raw_input("Enter the secret word (all in lowercase): ")
    print(50*"\n")
    wordShow = len(word)*"*"
    chanceToPlay = chancecount(word)
    for i in range(chanceToPlay):
        print("\nWord so far: " +str(wordShow))
        guess_char = raw_input("take a guess number " +str(i+1)+ ": ")
        if feedback(guess_char, word):
            print("\nGot it!")
            wordShow = guess(wordShow, guess_char, word)
            if wordShow == word:
                print("\nCongratulations. You correctly guessed the word: " +str(word))
                break
        else:
            print("\nSorry.")
    if wordShow != word:
        print("\nTime Over")
    print("\nThe secret word is: " +word)
    play = raw_input("\nDo you want to play one more time? y/n? ")
    print("")
