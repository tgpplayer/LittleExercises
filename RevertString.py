s = input("Enter a word to revert it -> ")

def revert_string(string):
    s_reverted = []

    for i in range(len(string) - 1, -1, -1):
        s_reverted.append(string[i])
    
    reverted_string = ""
    for i in s_reverted:
        reverted_string += i
    
    return reverted_string

print(f"The reverted string of {s} is {revert_string(s)}")