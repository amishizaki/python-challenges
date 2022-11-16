# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('What calculation would you like to do? (add, sub, mult, div): ')
num_one = input('What is number 1? ')
num_two = input('What is number 2? ')

if (operator == 'add'):
    result = int(num_one) + int(num_two)
elif (operator == 'sub'):
    result = int(num_one) - int(num_two)
elif (operator == 'mult'):
    result = int(num_one) * int(num_two)
elif (operator == 'div'):
    result = int(num_one) / int(num_two)
print(result)