max_highest = int(input('what is the highest roll? '))
other_list = [1,1,1,1,1,1,1]
which_number_hit = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

list_counter = 0
for number in range(1,21):
    if max_highest == number:
        which_number_hit[list_counter] += 1
        break
    else:
        list_counter +=1    

output = other_list + which_number_hit

print(output)
