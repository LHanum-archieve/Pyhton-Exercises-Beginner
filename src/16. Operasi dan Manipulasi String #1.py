# 16. OPERASI DAN MANIPULASI STRING #1
print("15. OPERASI DAN MANIPULASI STRING #1")
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Menyambung String (concatenate)
nama1 = "Baby"
nama2 = "Boba"
nama3 = "Ivan"
nama_lengkap = nama1 + " " + nama2 + " " + nama3
print("Nama Lengkap =",nama_lengkap)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Menghitung panjang string 
panjang = len(nama_lengkap)
print("Panjang Nama =",panjang)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Operator untuk string
### Cek apakah ada komponen char atau string di string
b = "b"
status = b in nama_lengkap
print(b +" "+"ada di" +" "+ nama_lengkap +" = "+ str(status))

### Cek apakah tidak ada komponen char atau string di string
z = "z"
status = z not in nama_lengkap
print (z +" "+"tidak ada di" +" "+ nama_lengkap +" = "+ str(status))

### Mengulang string
print("boba"*8)
print("hehe"*8)

### Indexing
print("index ke-0         = " + nama_lengkap[0])     # Dimulai dari depan = 0
print("index ke-(-1)      = " + nama_lengkap[-1])    # Dimulai dari belakang
print("index ke-(0:4)     = " + nama_lengkap[0:4])   # String dengan rentang tertentu 
print("index ke-(0,2,6,8) = " + nama_lengkap[0:9:2]) # string dengan jeda

### Item paling kecil
print("Paling kecil = "+ min(nama_lengkap))

### Item paling besar
print("Paling besar = "+ max(nama_lengkap))

ascii_code = ord(" ")
data       = 117
print("ASCII code untuk spasi adalah "+ str(ascii_code))
print("Char untuk ASCII 117 adalah "+ chr(data))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Operator dalam bentuk metode
Data = "Baby Boba Ivan"
jumlah = Data.count("o")
print("Jumlah o pada "+ Data + " = "+ str(jumlah))
