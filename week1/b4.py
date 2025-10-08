int_table = [int(item) for item in str.split(input("Enter a1 b1 c1 a2 b2 a3 :")," ")]
TB = (((int_table[0] + int_table[1] + int_table[2]) + (int_table[3] + int_table[4]) * 2 + int_table[5] * 3)/10)
print(f"{TB:.1f}")