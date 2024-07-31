from itertools import permutations
import lb_functions as lbf
import sys


def solver(letters, strategy=lbf.get_score3): #letters should be a list containing 4 lists
    words = lbf.get_possible_words(letters)
    sequence = []
    

    first = True
    letter_set = set(letters)   
    while letter_set:
        # print(letter_set)
        if first:
            score_dict = {word: strategy(word,letter_set) for word in words}
            
            ranked = lbf.order(score_dict)
            first = False
            
            #choose top word
            chosen = ranked[0]
            words.remove(chosen)
            
            sequence.append(chosen)

            #update letter_set
            for l in (letter_set & set(chosen)):
                letter_set.remove(l)
                
                
            
        else:
            #filter out words that don't start with starting_letter
            filtered_words = filter(lambda word: chosen[-1] == word[0], words)
            

            score_dict = {word: strategy(word,letter_set) for word in filtered_words}
            ranked = lbf.order(score_dict)

            if len(ranked) == 0:
                return False
            chosen = ranked[0]
            words.remove(chosen)
            
            sequence.append(chosen)

            #update letter_set
            for l in (letter_set & set(chosen)):
                letter_set.remove(l)
                

    # print(sequence)
    return sequence



####################################
#different strategy
####################################






def checkleft(words, chosen, letter_set,  check_left):
    if check_left:
        left_words = filter(lambda word: chosen[0] == word[-1], words)
        left_dict = {word: lbf.get_score1(word,letter_set) for word in left_words}
        left_ranked = lbf.order(left_dict)
        if len(left_ranked) == 0:
            return None


        best_left = left_ranked[0]

        return best_left
    else:
        return None
    

def checkright(words, chosen, letter_set,  check_right):
    if check_right:
        right_words = filter(lambda word: chosen[-1] == word[0], words)
        right_dict = {word: lbf.get_score1(word,letter_set) for word in right_words}
        right_ranked = lbf.order(right_dict)
        if len(right_ranked) == 0:
            return None

        best_right = right_ranked[0]

        return best_right
    else:
        return None



        

def solver2(letters):
    #get all possible words
    words = lbf.get_possible_words(letters)
    sequence = []
    letter_set = set(letters)

    #chose the best word
    score_dict = {word: lbf.get_score1(word,letter_set) for word in words}  
    ranked = lbf.order(score_dict)
    print(ranked)
    chosen = ranked[2]
    sequence.append(chosen)
    words.remove(chosen)

    #update letter_set
    for l in (letter_set & set(chosen)):
        letter_set.remove(l)




    check_left, check_right = True, True
    while letter_set:
        #chose the best left and right
        best_left = checkleft(words, chosen, letter_set, check_left)
        best_right = checkright(words, chosen, letter_set, check_right)

        #you dont need to compare when you arent even making a choice
        #check if we have already chosen a direction


        #if we need to compare the choices
        if check_left and check_right:
            #if left is better
            if len((letter_set & set(best_left))) > len((letter_set & set(best_right))):
                sequence.insert(0, best_left)
                words.remove(best_left)

                #update letter_set
                for l in (letter_set & set(best_left)):
                    letter_set.remove(l)
                
                chosen = best_left
                check_right = False


            else: 
                sequence.append(best_right)
                words.remove(best_right)

                #update letter_set
                for l in (letter_set & set(best_right)):
                    letter_set.remove(l)
                
                chosen = best_right
                check_left = False

        #we don't need to compare
        elif check_left:
            sequence.insert(0, best_left)
            words.remove(best_left)
            
            #update letter_set
            for l in (letter_set & set(best_left)):
                letter_set.remove(l)    
            chosen = best_left
        
        elif check_right:
                sequence.append(best_right)
                words.remove(best_right)

                #update letter_set
                for l in (letter_set & set(best_right)):
                    letter_set.remove(l)
                chosen = best_right




            




        # print(f"best: {chosen}")
        # print(f"left: {best_left}")
        # print(f"right: {best_right}")
        # print(f"best sequence is: {sequence}")
        # print(letter_set)
    
    
       
    return sequence

    

    









if __name__ == "__main__":
    letters = sys.argv[1]
    strategy = sys.argv[2]
    dumb = {'1': lbf.get_score1,'2': lbf.get_score2, '3': lbf.get_score3, '4': lbf.get_score4 }
    #print(solver(letters, dumb[strategy]))

    print(solver2(letters))