import math


a = int(input("Input a number: "))
b = int(input("Input b number: "))
c = int(input("Input c number: "))

if (a+b>c) and (a+c>b) and (b+c>a):
    s = (a + b + c)/2
    print(f"Area: {math.sqrt(s * (s - a) * (s - b) * (s - c))}")
else: 
    print ("Khong phai 3 canh cua tam giac") 