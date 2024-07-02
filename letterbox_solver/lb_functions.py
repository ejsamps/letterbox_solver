from itertools import permutations


letterfreq = {
  'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
  'F': 2.230, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
  'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
  'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
  'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974,
  'Z': 0.074
}


"""This function simply returns the list of words that you are allowed to spell given the box
configuration. The letters variable is just a string of the letters in an order."""
def get_possible_words(letters): #letters should be a list containing 4 lists
    with open("dictionary.txt", 'r') as infile:
        file = infile.readlines()
        possibles1 = [word.rstrip() for word in file]

    l1, l2, l3, l4 = letters[:3], letters[3:6], letters[6:9], letters[9:]
    possibles2 = []

    #if the word has a letter that isnt even an option, remove it
    for word in possibles1:
        if set(word).issubset(set(letters)):
            possibles2.append(word)

    #get all the not allowed sequences of letters
        #aka the combinations of two letters from the same side
    bad_sequences = []
    for l in [l1,l2,l3,l4]:
        bads = list(permutations(l,2))
        for seq in bads:
            bad_sequences.append(seq)

    for letta in letters:
        bad_sequences.append((letta, letta))
    
    #now we are going to go through and eliminate words that have unallowed sequences
        #if the word has a sequence that is not allowed, remove it
    possibles2copy = possibles2.copy()
    for word in possibles2copy:
        for bad_seq in bad_sequences:
            bs = bad_seq[0] + bad_seq[1]

            if bs in word:
                 possibles2.remove(word)
                 break
                 
    return possibles2



"""Give a score that counts how many desired letters a word has in it. The desried letters 
come from the desired variable that is a string of letters"""
def get_score1(word, letters):
    #they get points for each desired letter they have
    return len(set(word) & letters)

            

def get_score2(word, letters):
    score1 = get_score1(word, letters)

    firstletter = word[0]
    lastletter = word[-1]
    #starts with rare is good
    score1 += (1 / letterfreq[firstletter])
    #ends with common is good
    score1 += (letterfreq[lastletter] / 10)




    return score1



def get_score3(word, letters):
    score = 0
    shared_letters = (set(word) & letters)
    for l in shared_letters:
        score += (1/letterfreq[l])
    return score










    





#get the words sorted by their score
    
def order(score_dict):
    return sorted(list(score_dict.keys()), key = lambda word: score_dict[word], reverse=True)
    


    









