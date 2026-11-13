# APLIKASI NILAI MAHASISWA
# Fitur: Tambah, Lihat, Cari, Hapus, Simpan ke File

import os

NAMA_FILE = "data_nilai.txt"

def hitung_nilai_huruf(nilai):
    """Menghitung nilai huruf dari nilai angka"""
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 55:
        return "D"
    else:
        return "E"

def hitung_status(nilai):
    """Menentukan lulus / tidak lulus"""
    if nilai >= 65:
        return "LULUS ✅"
    else:
        return "TIDAK LULUS ❌"

def simpan_ke_file(daftar_mahasiswa):
    """Menyimpan data ke file .txt"""
    with open(NAMA_FILE, "w") as file:
        for mhs in daftar_mahasiswa:
            # Format: nama,nim,nilai
            file.write(f"{mhs['nama']},{mhs['nim']},{mhs['nilai']}\n")
    print("💾 Data berhasil disimpan!")

def baca_dari_file():
    """Membaca data dari file kalau ada"""
    daftar_mahasiswa = []
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    nama, nim, nilai = baris.split(",")
                    daftar_mahasiswa.append({
                        "nama": nama,
                        "nim": nim,
                        "nilai": int(nilai)
                    })
    return daftar_mahasiswa

def tambah_mahasiswa(daftar_mahasiswa):
    print("\n--- TAMBAH MAHASISWA ---")
    nama = input("Nama: ")
    nim = input("NIM: ")

    # Cek NIM duplikat
    for mhs in daftar_mahasiswa:
        if mhs["nim"] == nim:
            print("⚠️  NIM sudah ada! Gunakan NIM lain.")
            return

    try:
        nilai = int(input("Nilai (0-100): "))
    except ValueError:
        print("⚠️  Nilai harus angka!")
        return

    if nilai < 0 or nilai > 100:
        print("⚠️  Nilai harus 0 sampai 100!")
        return

    daftar_mahasiswa.append({"nama": nama, "nim": nim, "nilai": nilai})
    print(f"✅ {nama} berhasil ditambahkan!")
    simpan_ke_file(daftar_mahasiswa)

def lihat_semua(daftar_mahasiswa):
    print("\n" + "="*60)
    print("           DAFTAR NILAI MAHASISWA".center(60))
    print("="*60)

    if not daftar_mahasiswa:
        print("Belum ada data. Tambah dulu yuk!")
        return

    print(f"{'No':<4}{'Nama':<20}{'NIM':<15}{'Nilai':<7}{'Huruf':<7}{'Status':<12}")
    print("-"*60)

    total_nilai = 0
    for i, mhs in enumerate(daftar_mahasiswa, start=1):
        huruf = hitung_nilai_huruf(mhs["nilai"])
        status = hitung_status(mhs["nilai"])
        print(f"{i:<4}{mhs['nama']:<20}{mhs['nim']:<15}{mhs['nilai']:<7}{huruf:<7}{status:<12}")
        total_nilai += mhs["nilai"]

    rata_rata = total_nilai / len(daftar_mahasiswa)
    print("-"*60)
    print(f"Jumlah Mahasiswa : {len(daftar_mahasiswa)}")
    print(f"Rata-rata Kelas  : {rata_rata:.2f}")
    print(f"Nilai Tertinggi   : {max(m['nilai'] for m in daftar_mahasiswa)}")
    print(f"Nilai Terendah    : {min(m['nilai'] for m in daftar_mahasiswa)}")
    print("="*60)

def cari_mahasiswa(daftar_mahasiswa):
    print("\n--- CARI MAHASISWA ---")
    keyword = input("Masukkan Nama / NIM yang dicari: ").lower()
    ketemu = False

    for mhs in daftar_mahasiswa:
        if keyword in mhs["nama"].lower() or keyword in mhs["nim"].lower():
            huruf = hitung_nilai_huruf(mhs["nilai"])
            status = hitung_status(mhs["nilai"])
            print(f"\nDitemukan!")
            print(f"Nama   : {mhs['nama']}")
            print(f"NIM    : {mhs['nim']}")
            print(f"Nilai  : {mhs['nilai']} ({huruf}) - {status}")
            ketemu = True

    if not ketemu:
        print("❌ Data tidak ditemukan!")

def hapus_mahasiswa(daftar_mahasiswa):
    print("\n--- HAPUS MAHASISWA ---")
    nim = input("Masukkan NIM yang mau dihapus: ")

    for mhs in daftar_mahasiswa:
        if mhs["nim"] == nim:
            daftar_mahasiswa.remove(mhs)
            print(f"✅ {mhs['nama']} berhasil dihapus!")
            simpan_ke_file(daftar_mahasiswa)
            return

    print("❌ NIM tidak ditemukan!")

def main():
    daftar_mahasiswa = baca_dari_file()
    print(f"📂 Data dimuat: {len(daftar_mahasiswa)} mahasiswa")

    while True:
        print("\n" + "="*40)
        print("  APLIKASI NILAI MAHASISWA".center(40))
        print("="*40)
        print("1. Tambah Mahasiswa")
        print("2. Lihat Semua Nilai")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        print("="*40)

        pilih = input("Pilih menu (1-5): ")

        if pilih == "1":
            tambah_mahasiswa(daftar_mahasiswa)
        elif pilih == "2":
            lihat_semua(daftar_mahasiswa)
        elif pilih == "3":
            cari_mahasiswa(daftar_mahasiswa)
        elif pilih == "4":
            hapus_mahasiswa(daftar_mahasiswa)
        elif pilih == "5":
            print("\nData sudah tersimpan otomatis. Sampai jumpa! 👋")
            break
        else:
            print("⚠️  Pilih 1 sampai 5 aja!")

if __name__ == "__main__":
    main()