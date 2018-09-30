from check_highest import CheckHighest
from master_roll import Roll
import json

def Stage(roll_name,staged_dicelist,number_of_rolls):
 
    highest_results_dictionary = {  
    'd4_hits':0,
    'd6_hits':0,
    'd8_hits':0,
    'd10_hits':0,   
    'd12_hits':0,
    'd20_hits':0,  
    'double_hit':0,
    'triple_hit':0,
    'quad_hit':0,
    'quint_hit':0, 
    '1s':0,
    '2s':0,
    '3s':0,
    '4s':0,
    '5s':0,
    '6s':0,
    '7s':0,
    '8s':0,
    '9s':0,
    '10s':0,
    '11s':0,
    '12s':0,
    '13s':0,
    '14s':0,
    '15s':0,
    '16s':0,
    '17s':0,
    '18s':0,
    '19s':0,
    '20s':0}

    for roll in range(number_of_rolls):
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
        highest_results_list = CheckHighest(d4s,d6s,d8s,d10s,d12s,d20s)
        
        # zip highest list into highest dictionary
        list_counter = 0  
        for k, v in highest_results_dictionary.items():
            if highest_results_list[list_counter] != 0:
                highest_results_dictionary[k] += highest_results_list[list_counter]
            list_counter += 1   

    with open("results.txt", "a+") as file:
        file.write(roll_name + (json.dumps(highest_results_dictionary)) + '\n')
    
    return()

