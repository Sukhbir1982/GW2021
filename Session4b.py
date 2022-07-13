# Bitwise Operators and Shift Operators
# & | ^ >> <<
# Majorily used in field of security

num1 = 12
num2 = 4
                                            # 4 bit representation
print("Binary of", num1, "is:", bin(num1))   # 1 1 0 0
print("Binary of", num2, "is:", bin(num2))   # 0 1 0 0

num3 = num1 & num2
print("Binary of & of", num1, "(", bin(num1), ") and", num2, " (", bin(num2), ")", "is:", num3, "(", bin(num3), ")")    # 0 1 0 0

num4 = num1 | num2
print("Binary of | of", num1, "(", bin(num1), ") and", num2, " (", bin(num2), ")", "is:", num4, "(", bin(num4), ")")    # 1 1 0 0

num5 = num1 ^ num2
print("Binary of ^ of", num1, "(", bin(num1), ") and", num2, " (", bin(num2), ")", "is:", num5, "(", bin(num5), ")")    # 1 0 0 0

num6 = num1 >> 2
# 1 1 0 0
# 1 1 0 0 >> 2 -> _ _ 1 1 -> 0 0 1 1
print("Binary of >> 2 of", num1, "(", bin(num1), ") is:", num6, "(", bin(num6), ")")

# n >> x -> integral divide n with 2 power x
# n << x -> integral multiplication n with 2 power x

num7 = num1 << 3
# 1 1 0 0
# 1 1 0 0 << 2 -> 1 1 0 0 _ _ _  -> 1 1 0 0 0 0 0
print("Binary of << 3 of", num1, "(", bin(num1), ") is:", num7, "(", bin(num7), ")")

# Assignment: Explore what if we shift negative numbers to right and left
# e.g. -12 >> 3 or -19 << 4

n = -12
num8 = n >> 2
# 1 0 1 0 1
# 1 0 1 0 1 >> 3 -> _ _ _ 1 0 -> 0 0 0 1 0
print("Binary of", n, ">> 2 (", bin(n), ") is:", num8, "(", bin(num8), ")")

m = -19
num9 = m << 4
# 1 1 0 0
# 1 1 0 0 << 2 -> 1 1 0 0 _ _ _  -> 1 1 0 0 0 0 0
print("Binary of", m, "<< 4 (", bin(m), ") is:", num9, "(", bin(num9), ")")