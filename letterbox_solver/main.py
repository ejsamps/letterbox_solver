from itertools import permutations
import lb_functions as lbf
import sys


def solver(letters, strategy): #letters should be a list containing 4 lists
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


        

        # #get the words sorted by their score
        # def by_score(word, scores_dict):
        #     return scores_dict[word]
        # sorted_by_score = sorted(possibles, key = lambda word: scores_dict[word], reverse=True)

        # words_sorted = [item[0] for item in sorted_by_score]

        # print('')
        # print(sorted_by_score)
        


if __name__ == "__main__":
    letters = sys.argv[1]
    strategy = sys.argv[2]
    dumb = {'strategy1': lbf.get_score1,'strategy2': lbf.get_score2, 'strategy3': lbf.get_score3 }
    solver(letters, dumb[strategy])