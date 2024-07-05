### find duplicates or remove duplicates

def test_function(input_list):
    element_count = {}

    for element in input_list:
        if element in element_count:
            element_count[element] +=1
        else:
            element_count[element] =1

    #duplicate = [element for element, count in element_count.items() if count > 1]

    no_duplicates = [element for element in input_list if element_count[element] == 1]


    if no_duplicates:
        print("remove duplciates", no_duplicates)
    else:
        print("no duplicates")

abc1 = [1,2,3,4,5,6,7,8,7,6,5,4]
test_function(abc1)




#### reverse a list

def test_function(input_list):
    #reversed_list = []

    reversed_string = ''

    # for i in range(len(input_list) -1, -1, -1):
    #     reversed_list.append(input_list[i])

    for i in range(len(input_list) - 1, -1, -1):
        reversed_string += input_list[i]
    
    return reversed_string

#abc1 = [1,2,3,4,5]
abc1 = 'hello'
reversed = test_function(abc1)


print("reversed list", reversed)


import array
my_array = array.array('u')  # 'i' for integer array
my_array.append('h')
my_array.append('e')

output = ' '.join(my_array)
print("Array:", output)