#this is the count for doubles that weren't crits
doubles={
    'doubles_on_1s':0, 
    'doubles_on_2s':0, 
    'doubles_on_3s':0, 
    'doubles_on_4s':0, 
    'doubles_on_5s':0, 
    'doubles_on_6s':0, 
    'doubles_on_7s':0, 
    'doubles_on_8s':0, 
    'doubles_on_9s':0, 
    'doubles_on_10s':0, 
    'doubles_on_11s':0, 
    'doubles_on_12s':0, 
    'doubles_on_13s':0, 
    'doubles_on_14s':0, 
    'doubles_on_15s':0, 
    'doubles_on_16s':0, 
    'doubles_on_17s':0, 
    'doubles_on_18s':0, 
    'doubles_on_19s':0, 
    'doubles_on_20s':0}
doubles_any_number_per_roll = sum(doubles.values())

#this is the count for triples that weren't crits
triples={
    'triples_on_1s':0, 
    'triples_on_2s':0, 
    'triples_on_3s':0, 
    'triples_on_4s':0, 
    'triples_on_5s':0, 
    'triples_on_6s':0, 
    'triples_on_7s':0, 
    'triples_on_8s':0, 
    'triples_on_9s':0, 
    'triples_on_10s':0, 
    'triples_on_11s':0, 
    'triples_on_12s':0, 
    'triples_on_13s':0, 
    'triples_on_14s':0, 
    'triples_on_15s':0, 
    'triples_on_16s':0, 
    'triples_on_17s':0, 
    'triples_on_18s':0, 
    'triples_on_19s':0, 
    'triples_on_20s':0}
triples_any_number_per_roll = sum(triples.values())

#this is the count for quadruples that weren't crits
quadruples={
    'quadruples_on_1s':0, 
    'quadruples_on_2s':0, 
    'quadruples_on_3s':0, 
    'quadruples_on_4s':0, 
    'quadruples_on_5s':0, 
    'quadruples_on_6s':0, 
    'quadruples_on_7s':0, 
    'quadruples_on_8s':0, 
    'quadruples_on_9s':0, 
    'quadruples_on_10s':0, 
    'quadruples_on_11s':0, 
    'quadruples_on_12s':0, 
    'quadruples_on_13s':0, 
    'quadruples_on_14s':0, 
    'quadruples_on_15s':0, 
    'quadruples_on_16s':0, 
    'quadruples_on_17s':0, 
    'quadruples_on_18s':0, 
    'quadruples_on_19s':0, 
    'quadruples_on_20s':0}
quadruples_any_number_per_roll = sum(quadruples.values())

#this is the count for quintuples that weren't crits
quintuples={
    'quintuples_on_1s':0, 
    'quintuples_on_2s':0, 
    'quintuples_on_3s':0, 
    'quintuples_on_4s':0, 
    'quintuples_on_5s':0, 
    'quintuples_on_6s':0, 
    'quintuples_on_7s':0, 
    'quintuples_on_8s':0, 
    'quintuples_on_9s':0, 
    'quintuples_on_10s':0, 
    'quintuples_on_11s':0, 
    'quintuples_on_12s':0, 
    'quintuples_on_13s':0, 
    'quintuples_on_14s':0, 
    'quintuples_on_15s':0, 
    'quintuples_on_16s':0, 
    'quintuples_on_17s':0, 
    'quintuples_on_18s':0, 
    'quintuples_on_19s':0, 
    'quintuples_on_20s':0}
quintuples_any_number_per_roll = sum(quintuples.values())

#this is the count for sixtuples that weren't crits
sixtuples={
    'sixtuples_on_1s':0, 
    'sixtuples_on_2s':0, 
    'sixtuples_on_3s':0, 
    'sixtuples_on_4s':0, 
    'sixtuples_on_5s':0, 
    'sixtuples_on_6s':0, 
    'sixtuples_on_7s':0, 
    'sixtuples_on_8s':0, 
    'sixtuples_on_9s':0, 
    'sixtuples_on_10s':0, 
    'sixtuples_on_11s':0, 
    'sixtuples_on_12s':0, 
    'sixtuples_on_13s':0, 
    'sixtuples_on_14s':0, 
    'sixtuples_on_15s':0, 
    'sixtuples_on_16s':0, 
    'sixtuples_on_17s':0, 
    'sixtuples_on_18s':0, 
    'sixtuples_on_19s':0, 
    'sixtuples_on_20s':0}
sixtuples_any_number_per_roll = sum(sixtuples.values())


def CheckMultiples(d4s, d6s, d8s, d10s, d12s, d20s):


    #print('made it to check multiple')
    #print('check multiple will use this: %s %s %s %s %s %s' % (d4s, d6s, d8s, d10s, d12s, d20s))
    
    #this will remove crits from the rolled dicelists in order to check for reugular doubles, triples, etc...    
    
    d4s_wo_crit = d4s
    d6s_wo_crit = d6s
    d8s_wo_crit = d8s
    d10s_wo_crit = d10s
    d12s_wo_crit = d12s
    d20s_wo_crit = d20s
    
    #because I don't know list comprehension and eliminating integers with .remove changes the positions of the list that I'm iterating through I have to hack this by replacing any crit with a 0
    for n, i in enumerate(d4s_wo_crit):
        if i == 4:
            d4s_wo_crit[n] = 0
    
    for n, i in enumerate(d6s_wo_crit):
        if i == 6:
            d6s_wo_crit[n] = 0
    
    for n, i in enumerate(d8s_wo_crit):
        if i == 8:
            d8s_wo_crit[n] = 0
    
    for n, i in enumerate(d10s_wo_crit):
        if i == 10:
            d10s_wo_crit[n] = 0
    
    for n, i in enumerate(d12s_wo_crit):
        if i == 12:
            d12s_wo_crit[n] = 0
    
    for n, i in enumerate(d20s_wo_crit):
        if i == 20:
            d20s_wo_crit[n] = 0
        
    rolled_dice_not_crit = d4s_wo_crit + d6s_wo_crit + d8s_wo_crit + d10s_wo_crit + d12s_wo_crit + d20s_wo_crit  
    
    #this counts through all the numbers from 1 - 20 to check to see if there are any doubles, triples, etc after the crits have been removed
    x = 1 
    for k, v in doubles.items():
        #print('checking %s' % x)
        if rolled_dice_not_crit.count(x) == 2:
            #print('%s has a double' % x)
            doubles[k] += 1
        
        x += 1
    
    #print(doubles)
    
    
    x = 1 
    for k, v in triples.items():
        #print('checking %s' % x)
        if rolled_dice_not_crit.count(x) == 3:
            #print('%s has a triple' % x)
            triples[k] += 1
        
        x += 1
    
    #print(triples)
    
    x = 1 
    for k, v in quadruples.items():
        #print('checking %s' % x)
        if rolled_dice_not_crit.count(x) == 4:
            #print('%s has a quadruple' % x)
            quadruples[k] += 1
        
        x += 1
    
    #print(quadruples)
    
    x = 1 
    for k, v in quintuples.items():
        #print('checking %s' % x)
        if rolled_dice_not_crit.count(x) == 5:
            #print('%s has a quadruple' % x)
            quintuples[k] += 1
        
        x += 1
    
    #print(quintuples)
    
    x = 1 
    for k, v in sixtuples.items():
        #print('checking %s' % x)
        if rolled_dice_not_crit.count(x) == 6:
            #print('%s has a quadruple' % x)
            sixtuples[k] += 1
        
        x += 1
    
    #print(sixtuples)
    '''
    #this will zero out fields
    return_doubles_results = {}
    return_triples_results = {}
    return_quadruples_results = {}
    return_quintuples_results = {}
    return_sixtuples_results = {}
    
    for (k,v) in doubles.items():
        if v != 0:
            #print('this value will be recorded: %s' % k, v)
            return_doubles_results[k] = v
            #print('this will be returned to check: %s' % return_doubles_results)
            
    for (k,v) in triples.items():
        if v != 0:
            #print('this value will be recorded: %s' % k, v)
            return_triples_results[k] = v
            #print('this will be returned to check: %s' % return_triples_results)
            
    for (k,v) in quadruples.items():
        if v != 0:
            #print('this value will be recorded: %s' % k, v)
            return_quadruples_results[k] = v
            #print('this will be returned to check: %s' % return_quadruples_results)
    
    for (k,v) in quintuples.items():
        if v != 0:
            #print('this value will be recorded: %s' % k, v)
            return_quintuples_results[k] = v
            #print('this will be returned to check: %s' % return_quintuples_results)
    
    for (k,v) in sixtuples.items():
        if v != 0:
            #print('this value will be recorded: %s' % k, v)
            return_sixtuples_results[k] = v
            #print('this will be returned to check: %s' % return_sixtuples_results)
    
    
    multiples_results_dictionary = [return_doubles_results, return_triples_results, return_quadruples_results, return_quintuples_results]
    '''
    
    multiples_results_dictionary = [doubles, triples, quadruples, quintuples, sixtuples]
    
    return(multiples_results_dictionary)
    

def ClearMultiples():
    doubles.clear()
    triples.clear()
    quadruples.clear()
    quintuples.clear()
    sixtuples.clear()

    print('clearing multiples not crit: doubles: %s, triples: %s, quadruples: %s, quintuples: %s, sixtuples: %s' % (doubles, triples, quadruples, quintuples, sixtuples))    
    return()


