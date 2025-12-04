# 14. OPERATOR ASSIGNMENT
# Operasi yang dilakukan dengan penyingkatan
print("14. OPERATOR ASSIGNMENT")
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Operasi Aritmatika Biasa
a = 27   # Assignment
print("Operasi Aritmatika Biasa")
print("Nilai a   =", a)

# Penyingkatan pada penambahan
a += 1  # Artinya a = a + 1
print("Nilai a  += 1, nilai a menjadi",a)

# Penyingkatan pada pengurangan
a -= 2  # Artinya a = a - 2
print("Nilai a  -= 2, nilai a menjadi",a)

# Penyingkatan pada perkalian
a *= 5  # Artinya a = a * 5
print("Nilai a  *= 5, nilai a menjadi",a)

# Penyingkatan pada pembagian
a /= 2  # Artinya a = a / 2
print("Nilai a  /= 2, nilai a menjadi",a)

# Penyingkatan pada modulus
a %= 3  # Artinya a = a % 3
print("Nilai a  %= 3, nilai a menjadi",a)

# Penyingkatan pada floor division
a //= 2  # Artinya a = a // 2
print("Nilai a //= 2, nilai a menjadi",a)

# Penyingkatan pada pangkat
a **= 2  # Artinya a = a ** 2
print("Nilai a **= 2, nilai a menjadi",a)
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Operasi Bitwise
print("Operasi Bitwise")

### OR
b  = True 
b |= False
print("OR")
print("Nilai b  =", b)
print("Nilai b |= False, nilai b menjadi",b)

b  = False
b |= False
print("Nilai b  =", b)
print("Nilai b |= False, nilai b menjadi",b)

### AND
c  = True 
c &= False
print("\nAND")
print("Nilai c  =", c)
print("Nilai c &= False, nilai c menjadi",c)

c  = True 
c &= True
print("Nilai c  =", c)
print("Nilai c &= True, nilai c menjadi",c)

### XOR
d  = True 
d ^= False
print("\nXOR")
print("Nilai d  =", d)
print("Nilai d ^= False, nilai d menjadi",d)

d  = True 
d ^= True
print("Nilai d  =", d)
print("Nilai d ^= True, nilai d menjadi",d)

### Shift Right and Left
e = 0b0100
print("\nShift Right and Left")
print("Nilai e =", format(e,'04b'))
e >>= 2
print("Nilai e >>= 2, nilai e menjadi",format(e,'04b'))
e <<= 1
print("Nilai e <<= 1, nilai e menjadi",format(e,'04b'))
