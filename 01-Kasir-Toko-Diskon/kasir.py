def hitung_diskon(total):
    """Menghitung diskon berdasarkan total belanja"""
    if total >= 500000:
        return 0.20  # Diskon 20%
    elif total >= 200000:
        return 0.10  # Diskon 10%
    elif total >= 100000:
        return 0.05  # Diskon 5%
    else:
        return 0     # Tidak ada diskon

def tampilkan_struk(daftar_belanja, total, diskon_persen, potongan, total_bayar, uang, kembalian):
    print("\n" + "="*40)
    print("         STRUK BELANJA".center(40))
    print("="*40)
    print(f"{'Barang':<15}{'Qty':<5}{'Harga':<10}{'Subtotal':<10}")
    print("-"*40)
    for nama, qty, harga, subtotal in daftar_belanja:
        print(f"{nama:<15}{qty:<5}{harga:<10}{subtotal:<10}")
    print("-"*40)
    print(f"Total Belanja : Rp {total}")
    print(f"Diskon {int(diskon_persen*100)}%    : -Rp {potongan}")
    print(f"Total Bayar   : Rp {total_bayar}")
    print(f"Uang Bayar    : Rp {uang}")
    print(f"Kembalian     : Rp {kembalian}")
    print("="*40)
    print(" Terima kasih sudah berbelanja! ".center(40))
    print("="*40)

def main():
    print("="*40)
    print("  SELAMAT DATANG DI TOKO SATRIA  ".center(40))
    print("="*40)

    daftar_belanja = []
    total = 0

    while True:
        nama = input("\nNama barang (ketik 'selesai' untuk selesai): ")
        if nama.lower() == 'selesai':
            break

        try:
            harga = int(input("Harga barang: Rp "))
            qty = int(input("Jumlah: "))
        except ValueError:
            print("⚠️  Harga dan jumlah harus angka! Coba lagi.")
            continue

        if harga <= 0 or qty <= 0:
            print("⚠️  Harga dan jumlah harus lebih dari 0!")
            continue

        subtotal = harga * qty
        daftar_belanja.append((nama, qty, harga, subtotal))
        total += subtotal
        print(f"✅ {nama} ditambahkan! Subtotal: Rp {subtotal}")

    if not daftar_belanja:
        print("\nTidak ada barang yang dibeli. Program selesai.")
        return

    # Hitung Diskon
    diskon_persen = hitung_diskon(total)
    potongan = int(total * diskon_persen)
    total_bayar = total - potongan

    print(f"\nTotal Belanja: Rp {total}")
    print(f"Kamu dapat diskon {int(diskon_persen*100)}% ! Potongan: Rp {potongan}")
    print(f"Total yang harus dibayar: Rp {total_bayar}")

    # Input Uang Bayar
    while True:
        try:
            uang = int(input("\nMasukkan uang bayar: Rp "))
            if uang < total_bayar:
                print(f"⚠️  Uang kurang! Kurang Rp {total_bayar - uang}")
            else:
                break
        except ValueError:
            print(" ⚠️  Masukkan angka yang valid!")

    kembalian = uang - total_bayar
    tampilkan_struk(daftar_belanja, total, diskon_persen, potongan, total_bayar, uang, kembalian)

if __name__ == "__main__":
    main()