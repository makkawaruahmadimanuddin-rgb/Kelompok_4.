# Menggunakan for (jumlah sudah pasti 12 kali)
for i in range(12)
    print("Perulangan ke-", i)

print("----")

# Menggunakan while
i=0 
while i < 12:
    print("Perulangan ke-", i)
    i += 1 

# break 
saat i == 8
for i in range(15):
    if i == 8
    break
    print(i)

# continue
saat i == 4
for i in range(10):
    if i == 4:
        continue
    print(i) 

# elsse dijalankan jika loop selesai tanpa break
for i in range(6):
   print(i)
  else:
    print("Perulangan selesai tanpa break")

# nested loop 
for i in range(4):
    for j in range(5):
        print("i =", i, "j =", j)

# pola bintang
for i in range(7):
    for j in range(i + 1):
        print("*", end="")
    print()

# menghitung jumlah total
angka = [5, 15, 25, 35, 45]
total = 0

for nilai in angka:
    total += nilai

print("Total:", total)

n = 6
faktorial = 1

for i in range(1, n + 1):
    faktorial *=i

print("Faktorial:", faktorial)

# validasi input dengan while
angka = -1

while angka < 0:
    angka = int(input("Masukkan angka positif: "))

print("Anda memasukkan:", angka)