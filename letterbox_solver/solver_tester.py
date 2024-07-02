from random import sample
import sys
import letterbox_solver as ls
import lb_functions as lbf


import random
from collections import Counter


letter_frequencies = {
  'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
  'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 7.546, 'J': 0.153,
  'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
  'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.024, 'T': 9.056,
  'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974,
  'Z': 0.074
}

def generate_unique_string_by_frequency(length=12):

  total_letters = sum(letter_frequencies.values())
  letter_probabilities = {letter: freq / total_letters for letter, freq in letter_frequencies.items()}
  available_probabilities = letter_probabilities.copy()
  unique_string = ""

  while len(unique_string) < length:
    # Randomly choose a letter based on probabilities
    chosen_letter = random.choices(list(available_probabilities.keys()), weights=list(available_probabilities.values()))[0]
    # Add the letter to the string and remove it from available options
    unique_string += chosen_letter
    del available_probabilities[chosen_letter]
  return unique_string




def tester(n):
    avg = 0
    for _ in range(n):
        box = generate_unique_string_by_frequency()
        if (out := ls.solver(box, lbf.get_score1)) != False:
            avg += len(out)
        
    
    print(avg/n)
    return avg/n
        
        

if __name__ == "__main__":
    n = int(sys.argv[1])
    tester(n)