# app.py

import array

# Create an array of Unicode characters
my_array = array.array('u')

# Append characters to the array
my_array.append('h')
my_array.append('e')
my_array.append('l')
my_array.append('l')
my_array.append('o')

# Join the array elements with a space and print
output = ' '.join(my_array)
print("Array with spaces:", output)
