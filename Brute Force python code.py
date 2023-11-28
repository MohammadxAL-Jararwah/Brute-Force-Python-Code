import string

letters = string.printable # you can change this to the password domain
len_pass = int(input("len_pass = "))
len_pass = [0] * len_pass

def count_slice(lis):
    counter = len(lis) - 1

    for i in range(len(lis)-1,0,-1):
        if lis[i] >= len(letters)-1:
            lis[i] = 0
            counter -= 1
        else:
            break

    lis[counter] = (lis[counter] + 1) % len(letters)

    return lis

while True:
    """
    change the if statment to any valid thing you want
    """
    password = [letters[i] for i in len_pass]
    print("".join(password))

    if "".join(password) == (letters[-1]*len(len_pass)):
        break

    len_pass = count_slice(len_pass)
