'''
highest_results_dictionary = {  
'd4s_highest':0,
'd6s_highest':0,
'd8s_highest':0,
'd10s_highest':0,
'd12s_highest':0,
'd20s_highest':0,
'd4_hits':0,
'd6_hits':0,
'd8_hits':0,
'd10_hits':0,   
'd12_hits':0,
'd20_hits':0,  
'quint_hit':0, 
'quad_hit':0,
'triple_hit':0,
'double_hit':0,
'max_highest':0}
'''

def CheckHighest(d4s, d6s, d8s, d10s, d12s, d20s):
    #print('made it to check highest')
    #checking for the highest roll of the bunch
    
    max_highest = 0
    
    #we want to know which dice had the highest roll (the 'hit')
    #this indicates how many time a type of dice hit the highest number of the group roll
    d4_hits = 0
    d6_hits = 0
    d8_hits = 0
    d10_hits = 0   
    d12_hits = 0
    d20_hits = 0

    #records if the rolled hit number was hit by more than one dice    
    quint_hit = 0 
    quad_hit = 0
    triple_hit = 0
    double_hit = 0  
   
    #print(d4s, d6s, d8s, d10s, d12s, d20s)
    #prepares the highest rolls from each rolled list to compare against each other
    d4s_highest = max(d4s, default=0)
    d6s_highest = max(d6s, default=0)
    d8s_highest = max(d8s, default=0)
    d10s_highest = max(d10s, default=0)
    d12s_highest = max(d12s, default=0)
    d20s_highest = max(d20s, default=0)
    
    print(d4s_highest) 
    print(d6s_highest) 
    print(d8s_highest) 
    print(d10s_highest) 
    print(d12s_highest) 
    print(d20s_highest) 

    #highest_rolls is a list of all the highest rolls combined
    highest_rolls = [d4s_highest, d6s_highest, d8s_highest, d10s_highest, d12s_highest, d20s_highest]
    print(highest_rolls)
    #max_highest is the highest dice number
    max_highest = max(highest_rolls)
    print(max_highest)
    
    #compare the rolls and record which multisided dice had the highest roll ('hit')       
    if d20s_highest == max_highest:
        d20_hits += 1
    else:
        if d12s_highest == max_highest:
            d12_hits += 1
        else:
            if d10s_highest == max_highest:
                d10_hits += 1
            else:
                if d8s_highest == max_highest:
                    d8_hits += 1                    
                else:
                    if d6s_highest == max_highest:
                        d6_hits += 1
                    else:
                        if d4s_highest == max_highest:
                            d4_hits += 1

    #checks to see if the rolled hit number was hit by more than one dice, doesn't record which other dice hit though    
    if highest_rolls.count(max_highest) == 5:
        quint_hit += 1  
    if highest_rolls.count(max_highest) == 4:
        quad_hit += 1
    if highest_rolls.count(max_highest) == 3:
        triple_hit += 1
    if highest_rolls.count(max_highest) == 2:
        double_hit += 1

    #put all the results into a list to be put into the dictionary
    highest_results_list = [
    d4s_highest,
    d6s_highest,
    d8s_highest,
    d10s_highest,
    d12s_highest,
    d20s_highest,
    d4_hits,
    d6_hits,
    d8_hits,
    d10_hits,   
    d12_hits,
    d20_hits, 
    quint_hit, 
    quad_hit,
    triple_hit,
    double_hit,
    max_highest]    

    return(highest_results_list)

'''
    list_counter = 0    
    for k, v in highest_results_dictionary.items():
        #print('this is the key: %s' % k)
        #print('this is the value: %s' % v)
        if highest_results_list[list_counter] != 0:
            print('this is the highest results list: %s' % highest_results_list[list_counter])
            highest_results_dictionary[k] += 1
        list_counter += 1 


    #this will clear out zeroed entries                
    #return_highest_results = {}
    #for (k,v) in highest_results_dictionary.items():
    #    if v != 0:
            #print('this value will be recorded: %s' % k, v)
            #return_highest_results[k] = v
            #print('this will be returned to check: %s' % return_highest_results)       
    
    print('this is the highest_results coming from highest_check: %s' % highest_results_dictionary)
    return(highest_results_dictionary)




def ClearHighest():
    highest_results_dictionary.clear()
    #print('clearing highest: %s' % highest_results_dictionary)
    
    return()
    
     
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    