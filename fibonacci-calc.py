# Return x number of the Fibonacci sequence

def sum_two_last_numbers(sequence: list):
    n1 = sequence[len(sequence) - 1]
    n2 = sequence[len(sequence) - 2]
    new_number = n1 + n2
    return new_number

def calc_x_fib_number():
    sequence = [0, 1]
    num = int(input("Which number of the Fibonacci secuence do you want to calculate? -> "))

    while True:
        new_number = sum_two_last_numbers(sequence)
        sequence.append(new_number)

        if len(sequence) == num:
            break
    
    print(f"The {num}th number of the Fibonacci secuence is {sequence[len(sequence) - 1]}")

calc_x_fib_number()
