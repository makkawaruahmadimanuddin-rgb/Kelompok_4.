#Example if, elif, else
nilai = 67
if nilai >= 90:
    print("Grade: A++")
elif nilai >= 80:
    print("Grade: A+")
else:
    print("Grade: E")

#Menggunakan Input Dari Pengguna
kaii = int(input("Masukkan nilai kaii: "))
if kaii > 67:
    print("kaii lebih besar dari 67")
elif kaii == 67:
    print("kaii sama dengan 67")
else:
    print("kaii lebih kecil dari 67")

#MENGGUNAKAN IF BERSARANG (NESTED IF)
print("=== MESIN DETEKSI KLIEN DESAIN GRAFIS ===")
revisi = int(input("Berapa kali klien minta revisi logo hari ini? "))
if revisi > 5:
    print("Peringatan level waspada! Kesabaran terancam habis.")
    if revisi % 2 == 0:
        print("Jumlah revisinya genap. Klien ini pasti sebenarnya robot yang lagi ngetes kamu.")
    else:
        print("Jumlah revisinya ganjil. Fix, klien ini minta ubah warna cuma karena lagi gabut.")
elif revisi == 0:
    print("Nol revisi?! Ini pasti mimpi atau kliennya lupa belum ngecek file.")
else:
    print("Revisi masih di bawah 5. Cukup wajar, silakan lanjut minum kopi dan kerjakan!")

#MENGGUNAKAN TERNARY OPERATOR (IF DALAM SATU BARIS)
print("=== MESIN DETEKSI KLIEN (VERSI RINGKAS) ===")

revisi = int(input("Berapa kali klien minta revisi logo hari ini? "))

# Syarat Ganda 1: Revisi di atas 5 DAN angkanya genap
if revisi > 5 and revisi % 2 == 0:
    print("Peringatan waspada! Revisi lebih dari 5 dan genap. Klien ini pasti robot yang lagi ngetes kamu.")

# Syarat Ganda 2: Revisi di atas 5 DAN angkanya ganjil
elif revisi > 5 and revisi % 2 != 0:
    print("Peringatan waspada! Revisi lebih dari 5 dan ganjil. Fix, klien ini minta ubah warna cuma karena lagi gabut.")

# Pintu Alternatif 1: Revisi persis 0
elif revisi == 0:
    print("Nol revisi?! Ini pasti mimpi atau kliennya lupa belum ngecek file.")

# Pintu Alternatif 2: Kalau semua di atas tidak terpenuhi (berarti revisi 1 sampai 5)
else:
    print("Revisi masih 5 atau ke bawah. Cukup wajar, silakan lanjut minum kopi dan kerjakan!")

