from statistics import mean

def CheckAverage(d4s, d6s, d8s, d10s, d12s, d20s):    
    
    d4_string = str(d4s)
    d6_string = str(d6s)
    d8_string = str(d8s)
    d10_string = str(d10s)
    d12_string = str(d12s)
    d20_string = str(d20s)
    
    combined_rolls = [d4_string + d6_string + d8_string + d10_string + d12_string + d20_string]
    print('this is combined rolls: %s' % combined_rolls)
    
    #converting list into string because apparently that's neccessary...https://stackoverflow.com/questions/38836795/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
    stringify_combined = ''.join(combined_rolls) 
    print('this is stringify_combined: %s' % stringify_combined)
    
    ready_to_average = int(stringify_combined)
    print('this is ready_to_average: %s' % ready_to_average)
    
    average_of_rolls = mean(ready_to_average)
    
    return(average_of_rolls)