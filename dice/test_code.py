
dictionary_with_values = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0 }

list_to_check = [4,5,3,4,5,3]

list_counter = 0
for k, v in dictionary_with_values.items():
    if list_to_check[list_counter] == 4: 
        dictionary_with_values[k] += 1

    list_counter += 1
    
print(dictionary_with_values)

dictionary_with_values.clear()

print(dictionary_with_values)
