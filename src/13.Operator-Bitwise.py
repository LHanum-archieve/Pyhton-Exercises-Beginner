# 13. OPERATOR BITWISE (BINER) 
print("13. OPERATOR BITWISE (BINER)")
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
a = 9
b = 5

# Bitwise OR (|)
c = a | b
print("OR (|)")
print("nilai  : ", a, ", binary :", format(a,'08b'))
print("nilai  : ", b, ", binary :", format(b,'08b'))
print("-------------------------------(|)")
print("nilai  :", c, ", binary :", format(c,'08b'))
print("")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Bitwise AND (&)
c = a & b
print("AND (&)")
print("nilai  :", a, ", binary :", format(a,'08b'))
print("nilai  :", b, ", binary :", format(b,'08b'))
print("-------------------------------(&)")
print("nilai  :", c, ", binary :", format(c,'08b'))
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Bitwise OR (^)
c = a ^ b
print("XOR (^)")
print("nilai  : ", a, ", binary :", format(a,'08b'))
print("nilai  : ", b, ", binary :", format(b,'08b'))
print("-------------------------------(^)")
print("nilai  :", c, ", binary :", format(c,'08b'))
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Bitwise NOT (~)
c = ~a
d = 0b0000001001
e = 0b1111111111
print("NOT (~)")
print("nilai  : ", a, ", binary :", format(a,'08b'))
print("nilai  : ", b, ", binary :", format(b,'08b'))
print("-------------------------------(~)")
print("nilai  :", c, ", binary :", format(c,'08b'))
print("-------------------------------(^)")
print("nilai  :", e^d, ", binary :", format(e^d,'08b'))
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Bitwise Shift Right (>>)
c = a >> 2
print("Shift Right (>>)")
print("nilai  :", a, ", binary :", format(a,'08b'))
print("-------------------------------(>>)")
print("nilai  :", c, ", binary :", format(c,'08b'))
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Bitwise Shift Left (<<)
c = a << 2
print("Shift Right (<<)")
print("nilai  :", a, ", binary :", format(a,'08b'))
print("-------------------------------(<<)")
print("nilai  :", c, ", binary :", format(c,'08b'))
print("")
