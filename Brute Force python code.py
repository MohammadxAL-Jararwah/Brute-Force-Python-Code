import string

letters = string.printable # you can change this to the password domain
len_pass = int(input("len_pass = "))
len_pass = [0] * len_pass

def count_slice(lis):
    index = len(lis) - 1

    while lis[index] >= (len(letters) - 1):
        lis[index] = 0
        index -= 1

    lis[index] = (lis[index] + 1) % len(letters)
    return lis

def Brute_Forec(letters,len_pass):
    
    while True:
        """
        change the if statment to any valid thing you want
        """
        password = [letters[i] for i in len_pass]
        print("".join(password))

        if "".join(password) == (letters[-1]*len(len_pass)):
            break

        len_pass = count_slice(len_pass)

Brute_Forec(letters,len_pass)
