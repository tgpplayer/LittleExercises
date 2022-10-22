def largerNumber(numbers):
    my_list = numbers.split()
    print(my_list)
    max_number = 0.0

    for i in my_list:
        if float(i) > max_number:
            max_number = float(i)
    return max_number

numbers = "4.00232 2.2342342 4.23232 4.222334 2.5523532 1.2323"
print("The largest number from my list is " + str(largerNumber(numbers)))