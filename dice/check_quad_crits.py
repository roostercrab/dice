quad_crits_results = {
'd4_quad_crit':0,
'd6_quad_crit':0,
'd8_quad_crit':0,
'd10_quad_crit':0,
'd12_quad_crit':0,
'd20_quad_crit':0}

def CheckQuadCrits(d4s, d6s, d8s, d10s, d12s, d20s):
    #print('made it to check quad crits')
    
    list_to_check_crits = [d4s, d6s, d8s, d10s, d12s, d20s]
    dice_sides_list = [4, 6, 8, 10, 12, 20]
    
    list_counter = 0
    sides_counter = 0
    
    for k, v in quad_crits_results.items():
        #print('this is the key: %s' % k)
        #print('this is the value: %s' % v)
        if list_to_check_crits[list_counter].count(dice_sides_list[sides_counter]) == 4: 
            #print('list_to_check_crits[list_counter] is: %s' % list_to_check_crits[list_counter])
            #print('dice_sides_list[sides_counter] is: %s' % dice_sides_list[sides_counter])
            quad_crits_results[k] += 1
            #print('match')
        #else:
            #print('no match')
        list_counter += 1
        sides_counter += 1            
                
    #print(quad_crits_results)          
    
    '''
    quad_crits_return = {}

    #this will clear out zeroed entries
    for (k,v) in quad_crits_results.items():
        if v != 0:
            #print('this value will be recorded: %s' % k, v)
            quad_crits_return[k] = v
            #print('this will be returned to check: %s' % quad_crits_return)
         

    return(quad_crits_return)
    '''
    
    #print(quad_crits_results) 
    return(quad_crits_results) 
    
    
def ClearQuadCrits():
    quad_crits_results.clear()
    print('clearing quad crits: %s' % quad_crits_results)
    
    return()