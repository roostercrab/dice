from master_roll import Roll
from check_highest import CheckHighest

def Stage(staged_dicelist, number_of_rolls):

    #staged_dicelist contains Dice objects and will iterate through the list rolling each one in a group then passing them to the check functions to be analyzed    
    #iterates over the actual rolls, number_of_rolls is passed from the beginning in Start_Rolls(number_of_rolls)
    roll_number = 0
    while roll_number < number_of_rolls:
        d4s = []
        d6s = []
        d8s = []
        d10s = []
        d12s = []
        d20s = []
        
        d4s = Roll(staged_dicelist[0])
        d6s = Roll(staged_dicelist[1])       
        d8s = Roll(staged_dicelist[2])
        d10s = Roll(staged_dicelist[3])
        d12s = Roll(staged_dicelist[4])
        d20s = Roll(staged_dicelist[5])
        highest_results_dictionary = CheckHighest(d4s,d6s,d8s,d10s,d12s,d20s)
        #print('this is the highest: %s' % highest_results_dictionary)        
        
        roll_number += 1

    final_return = {'highest_result':highest_results_dictionary}    
 
    #print('this is the final_return: %s' % final_return)
    
    return(final_return)
    