# 12. LATIHAN KOMPARASI DAN LOGIKA 
print("12. LATIHAN KOMPARASI DAN LOGIKA")
print("")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Membuat gabungan area rentang dari angka (kata kunci = or)
### +++3---10+++
input_1 = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10 ="))

#### Memeriksa angka kurang dari 3
a = (input_1 < 3)
print("Kurang dari 3 =", a)

#### Memeriksa angka lebih dari 10
b = (input_1 > 10)
print("Lebih dari 10 =", b)

#### Nilai gabungan (or)
c = a or b
print("Angka yang dimasukkan =", c)
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Membuat irisan area rentang dari angka (kata kunci = and)
### ---3+++10---
input_b = float(input("Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 ="))

#### Memeriksa angka lebih dari 3
d = (input_b > 3)
print("Kurang dari 3 =", d)

#### Memeriksa angka kurang dari 10
e = (input_b < 10)
print("Lebih dari 10 =", e)

#### Nilai irisan (and)
f = d and e
print("Angka yang dimasukkan =", f)
