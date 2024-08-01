from itertools import permutations
import lb_functions as lbf
import sys



def solver(letters):
    #get all spellable words
    words = lbf.get_possible_words(letters)

    for i in range(500):
        letter_set = set(letters).copy()
        #chose the ith best word
        root = lbf.chosebest(words,letter_set,i)
        sequence = [root]
        lbf.update_letters(letter_set,root)
        


        #find best left
        bestleft = lbf.checkleft(words,root,letter_set)
        
        if bestleft:
            if len(letter_set) == len(letter_set & set(root + bestleft)):
                sequence.insert(0, bestleft)
                return sequence, i



        
        #find the best right
        bestright = lbf.checkright(words, root, letter_set)
        
        if bestright:
            if len(letter_set) == len(letter_set & set(root + bestright)):
                sequence.append(bestright)
                return sequence, i
    


if __name__ == "__main__":
    letters = sys.argv[1]
    
    print(solver(letters,))



