# GAME SEDERHANA - TEBAK ANGKA & BATU GUNTING KERTAS
import random

def tebak_angka():
    print("\n" + "="*40)
    print("      GAME TEBAK ANGKA 1-100".center(40))
    print("="*40)
    print("Komputer sudah memilih angka rahasia!")
    print("Kamu punya 7 kesempatan. Semangat!")

    angka_rahasia = random.randint(1, 100)
    nyawa = 7
    percobaan = 0

    while nyawa > 0:
        print(f"\nSisa nyawa: {nyawa} ❤️")
        try:
            tebakan = int(input("Tebak angka (1-100): "))
        except ValueError:
            print("⚠️  Masukkan angka dong!")
            continue

        if tebakan < 1 or tebakan > 100:
            print("⚠️  Angkanya harus 1 sampai 100!")
            continue

        percobaan += 1

        if tebakan == angka_rahasia:
            print(f"\n🎉 BENAR! Angkanya {angka_rahasia}")
            print(f"Kamu berhasil dalam {percobaan} kali percobaan!")
            # Hitung skor
            skor = nyawa * 100
            print(f"Skor kamu: {skor}")
            return
        elif tebakan < angka_rahasia:
            print("🔼 Terlalu kecil! Coba angka yang lebih besar.")
        else:
            print("🔽 Terlalu besar! Coba angka yang lebih kecil.")

        nyawa -= 1

    print(f"\n💀 Nyawa habis! Angka rahasianya adalah {angka_rahasia}")
    print("Coba lagi ya!")

def batu_gunting_kertas():
    print("\n" + "="*40)
    print("   BATU - GUNTING - KERTAS".center(40))
    print("="*40)
    print("Ketik: batu / gunting / kertas")
    print("Ketik 'keluar' untuk berhenti main")

    pilihan = ["batu", "gunting", "kertas"]
    menang = 0
    kalah = 0
    seri = 0

    while True:
        print(f"\nSkor -> Menang: {menang} | Kalah: {kalah} | Seri: {seri}")
        user = input("Pilihan kamu: ").lower()

        if user == "keluar":
            break

        if user not in pilihan:
            print("⚠️  Pilihan harus batu / gunting / kertas!")
            continue

        komputer = random.choice(pilihan)
        print(f"Komputer memilih: {komputer}")

        if user == komputer:
            print("🤝 SERI!")
            seri += 1
        elif (user == "batu" and komputer == "gunting") or \
             (user == "gunting" and komputer == "kertas") or \
             (user == "kertas" and komputer == "batu"):
            print("🎉 KAMU MENANG!")
            menang += 1
        else:
            print("😢 KAMU KALAH!")
            kalah += 1

    print("\n=== HASIL AKHIR ===")
    print(f"Menang: {menang} | Kalah: {kalah} | Seri: {seri}")
    if menang > kalah:
        print("🏆 Kamu Juara! GG!")
    elif menang < kalah:
        print("Komputer lebih jago, balas dendam yuk!")
    else:
        print("Imbang! Rematch lagi?")

def main():
    while True:
        print("\n" + "="*40)
        print("   SELAMAT DATANG DI GAME SATRIA".center(40))
        print("="*40)
        print("1. Tebak Angka")
        print("2. Batu Gunting Kertas")
        print("3. Keluar")
        print("="*40)

        pilih = input("Pilih menu (1/2/3): ")

        if pilih == "1":
            tebak_angka()
        elif pilih == "2":
            batu_gunting_kertas()
        elif pilih == "3":
            print("\nMakasih udah main! Sampai jumpa lagi! 👋")
            break
        else:
            print("⚠️  Pilih 1, 2, atau 3 aja!")

if __name__ == "__main__":
    main()