from master_roll import Roll
from check_highest import CheckHighest
from check_multiples_not_crit import CheckMultiples
from check_single_crits import CheckSingleCrits
from check_double_crits import CheckDoubleCrits
from check_triple_crits import CheckTripleCrits
from check_quad_crits import CheckQuadCrits
from check_quint_crits import CheckQuintCrits
from check_six_crits import CheckSixCrits

'''
from check_highest import ClearHighest
from check_multiples_not_crit import ClearMultiples
from check_single_crits import ClearSingleCrits
from check_double_crits import ClearDoubleCrits
from check_triple_crits import ClearTripleCrits
from check_quad_crits import ClearQuadCrits
from check_quint_crits import ClearQuintCrits
from check_six_crits import ClearSixCrits
#from check_average import ClearAverage
'''

def Stage(staged_dicelist, number_of_rolls):
    
    '''
    #resets the dice metrics for the next roll
    ClearHighest()
    ClearMultiples()
    ClearSingleCrits()
    ClearDoubleCrits()
    ClearTripleCrits()
    ClearQuadCrits()
    ClearQuintCrits()
    ClearSixCrits()
    '''
    
    #resets the dice metrics for the next roll
    #highest_results_dictionary.clear()
    
    #staged_dicelist contains Dice objects and will iterate through the list rolling each one in a group then passing them to the check functions to be analyzed    
    #iterates over the actual rolls, number_of_rolls is passed from the beginning in Start_Rolls(number_of_rolls)
    for roll_number in range(number_of_rolls):
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
        print('this is the highest: %s' % highest_results_list)        
        single_crits_result = CheckSingleCrits(d4s,d6s,d8s,d10s,d12s,d20s)
        print('this is the single crits result: %s' % single_crits_result)
        double_crits_result = CheckDoubleCrits(d4s,d6s,d8s,d10s,d12s,d20s)
        print('this is the double crits result: %s' % double_crits_result)
        triple_crits_result = CheckTripleCrits(d4s,d6s,d8s,d10s,d12s,d20s)
        print('this is the triple crits result: %s' % triple_crits_result)
        quad_crits_result = CheckQuadCrits(d4s,d6s,d8s,d10s,d12s,d20s)
        print('this is the quad crits result: %s' % quad_crits_result)
        quint_crits_result = CheckQuintCrits(d4s,d6s,d8s,d10s,d12s,d20s)
        print('this is the quint crits result: %s' % quint_crits_result)
        six_crits_result = CheckSixCrits(d4s,d6s,d8s,d10s,d12s,d20s)
        print('this is the six crits result: %s' % six_crits_result)
        multiples_result = CheckMultiples(d4s,d6s,d8s,d10s,d12s,d20s)
        print('this is the multiples not crit result: %s' % multiples_result)
    
    final_return = {
        'highest_result':highest_results_list, 
        'single_crits_result':single_crits_result, 
        'double_crits_result':double_crits_result, 
        'triple_crits_result':triple_crits_result, 
        'quad_crits_result':quad_crits_result, 
        'quint_crits_result':quint_crits_result, 
        'six_crits_result':six_crits_result, 
        'multiples_result':multiples_result}    
 
    print('this is the final_return: %s' % final_return)
    
    return(final_return)
    