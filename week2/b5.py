c = input("Input a letter: ")
if c != "A" and c != "a" and c.isalpha() :
    print(chr(ord(c.lower())-1))