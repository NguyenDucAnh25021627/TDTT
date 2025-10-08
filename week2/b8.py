ten = input("Ten chu ho: ")
chisothangtruoc = int(input("Chi so thang truoc: "))
chisothangnay = int(input("Chi so thang nay: "))

price = 0
if 0 <=  chisothangnay <= 50000:
    price = 1984
elif chisothangnay <= 100000:
    price = 2050
elif chisothangnay <= 200000:
    price = 2380
elif chisothangnay <= 300000:
    price = 2998
elif chisothangnay <= 400000:
    price = 3350
else:
    price = 3460
print(price)
print(f"Ho va ten: {ten}\nTien phai tra la: {(chisothangnay  -chisothangtruoc) * price * 1.08}")