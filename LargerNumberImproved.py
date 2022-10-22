def largerNumber(numbers):
    my_list = numbers.split()
    my_list_to_float = []
    for i in my_list:
        my_list_to_float.append(float(i))
    return max(my_list_to_float)

numbers = "4.00232 2.2342342 4.23232 4.222334 2.5523532 1.2323"
print("The largest number from my list is " + str(largerNumber(numbers)))