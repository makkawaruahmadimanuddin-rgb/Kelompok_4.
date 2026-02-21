#Example Transfer Statement
def proses_penjualan(batas_pembeli):
    stok_barang = 20
    total_terjual = 0

    for pembeli in range(1, batas_pembeli + 1):
        print("Pembeli ke-", pembeli)

        if pembeli == 3:
            pass  # Placeholder (tidak ada perlakuan khusus)

        if pembeli % 2 == 0:
            continue  # Lewati pembeli dengan nomor genap

        if stok_barang <= 0:
            break  # Hentikan jika stok habis

        jumlah_beli = 3
        stok_barang -= jumlah_beli
        total_terjual += jumlah_beli

        print("Jumlah dibeli:", jumlah_beli)
        print("Sisa stok:", stok_barang)
        print("-" * 20)

    return total_terjual  # Mengembalikan total barang terjual


# Memanggil fungsi
hasil_penjualan = proses_penjualan(10)
print("Total barang terjual:", hasil_penjualan)
