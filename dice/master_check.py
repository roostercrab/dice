from check_highest import CheckHighest
from check_multiples_not_crit import CheckMultiples
from check_single_crits import CheckSingleCrits
from check_double_crits import CheckDoubleCrits
from check_triple_crits import CheckTripleCrits
from check_quad_crits import CheckQuadCrits
from check_quint_crits import CheckQuintCrits
from check_six_crits import CheckSixCrits
#from check_average import CheckAverage


#checks a single rolling of a group of multisided dice against each other 
def Check(d4s, d6s, d8s, d10s, d12s, d20s):
    
    
    print('this is the rolls before going to check highest: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    highest_result = CheckHighest(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the highest result dictionary: %s' % highest_result)

    print('this is the rolls before going to check crits: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    single_crits_result = CheckSingleCrits(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the crits result dictionary: %s' % single_crits_result)

    print('this is the rolls before going to check double crits: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    double_crits_result = CheckDoubleCrits(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the crits result dictionary: %s' % double_crits_result)
    
    print('this is the rolls before going to check triple crits: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    triple_crits_result = CheckTripleCrits(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the crits result dictionary: %s' % triple_crits_result)

    print('this is the rolls before going to check quad crits: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    quad_crits_result = CheckQuadCrits(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the crits result dictionary: %s' % quad_crits_result)

    print('this is the rolls before going to check crits: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    quint_crits_result = CheckQuintCrits(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the crits result dictionary: %s' % quint_crits_result)
    
    print('this is the rolls before going to check crits: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    six_crits_result = CheckSixCrits(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the crits result dictionary: %s' % six_crits_result)
    
    print('this is the rolls before going to check multiples: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))
    multiples_result = CheckMultiples(d4s, d6s, d8s, d10s, d12s, d20s)
    print('this is the multiples result dictionary: %s' % multiples_result)

    #print('this is the rolls before going to check average: %s %s %s %s %s %s' %(d4s, d6s, d8s, d10s, d12s, d20s))   
    #roll_average = CheckAverage(d4s, d6s, d8s, d10s, d12s, d20s)
    
    final_return = {'highest_result':highest_result, 'single_crits_result':single_crits_result, 'double_crits_result':double_crits_result, 'triple_crits_result':triple_crits_result, 'quad_crits_result':quad_crits_result, 'quint_crits_result':quint_crits_result, 'six_crits_result':six_crits_result, 'multiples_result':multiples_result}
    
    return(final_return)
    




    