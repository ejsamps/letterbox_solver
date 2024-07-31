from itertools import permutations
import lb_functions as lbf
import sys



def chosebest(words, letter_set, i):
    score_dict = {word: lbf.get_score1(word,letter_set) for word in words}  
    ranked = lbf.order(score_dict)
    
    if len(ranked) == 0:
        return None
    
    chosen = ranked[i]

    return chosen


def update_letters(letter_set, chosen):
    for l in (letter_set & set(chosen)):
        letter_set.remove(l)
    return letter_set



def checkleft(words, chosen, letter_set):
    left_words = filter(lambda word: chosen[0] == word[-1], words)
    return chosebest(left_words, letter_set, 0)
    #bestleft is either the best left word or None if there are no words to the left


def checkright(words, chosen, letter_set):
    right_words = filter(lambda word: chosen[-1] == word[0], words)
    return chosebest(right_words, letter_set, 0)
    #bestright is either the best right word or None if there are no words to the right



def checkdone(letter_set, root, addition):
    if len(letter_set) == len(letter_set & set(root + addition)):
        return True
    else:
        return False
    



def iterate(letters):
    #get all spellable words
    words = lbf.get_possible_words(letters)
    letter_set = set(letters)

    for i in range(1000):
        #chose the ith best word
        root = chosebest(words,letter_set,i)
        sequence = [root]


        #find best left
        bestleft = checkleft(words,root,letter_set)
        if bestleft:
            if checkdone(letter_set,root,bestleft):
                sequence.insert(0, bestleft)
                return sequence, i



        
        #find the best right
        bestright = checkright(words, root, letter_set)
        if bestright:
            if checkdone(letter_set, root, bestright):
                sequence.append(bestright)
                return sequence, i
    


if __name__ == "__main__":
    letters = sys.argv[1]
    print(iterate(letters))



