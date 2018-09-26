quint_crits_results = {
'd4_quint_crit':0,
'd6_quint_crit':0,
'd8_quint_crit':0,
'd10_quint_crit':0,
'd12_quint_crit':0,
'd20_quint_crit':0}

def CheckQuintCrits(d4s, d6s, d8s, d10s, d12s, d20s):
    #print('made it to check quint crits')
    
    list_to_check_crits = [d4s, d6s, d8s, d10s, d12s, d20s]
    dice_sides_list = [4, 6, 8, 10, 12, 20]
    
    list_counter = 0
    sides_counter = 0
    
    for k, v in quint_crits_results.items():
        #print('this is the key: %s' % k)
        #print('this is the value: %s' % v)
        if list_to_check_crits[list_counter].count(dice_sides_list[sides_counter]) == 5: 
            #print('list_to_check_crits[list_counter] is: %s' % list_to_check_crits[list_counter])
            #print('dice_sides_list[sides_counter] is: %s' % dice_sides_list[sides_counter])
            quint_crits_results[k] += 1
            #print('match')
        #else:
            #print('no match')
        list_counter += 1
        sides_counter += 1            
    
    '''
    quint_crits_return = {}

    #this will clear out zeroed entries
    for (k,v) in quint_crits_results.items():
        if v != 0:
            #print('this value will be recorded: %s' % k, v)
            quint_crits_return[k] = v
            #print('this will be returned to check: %s' % quint_crits_return)
         

    return(quint_crits_return)
    '''
    
    #print(quint_crits_results)
    return(quint_crits_results)
    
    
def ClearQuintCrits():
    quint_crits_results.clear()
    print('clearing quint crits: %s' % quint_crits_results)
    
    return()