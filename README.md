<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20,25,30&height=320&section=header&text=Project%20Semester%201&fontSize=55&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Satria%20Bagas%20Sejati%20%E2%80%A2%20552012610009%20%E2%80%A2%20Teknik%20Informatika&descAlignY=62&descSize=20" />

<div align="center">
  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=36BCF7&center=true&vCenter=true&width=435&lines=Halo%2C+Saya+Satria+Bagas+Sejati;Mahasiswa+Teknik+Informatika;Belajar+Python+Semester+1;Ngoding+Sambil+Ngopi+%F0%9F%94%A5)](https://git.io/typing-svg)
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Semester%201-FF6B00?style=for-the-badge&logo=bookstack&logoColor=white" />
  <img src="https://img.shields.io/badge/Monorepo-3_Projects-00FFAB?style=for-the-badge&logo=stackblitz&logoColor=black" />
  <img src="https://img.shields.io/badge/Status-On_Fire-FF00FF?style=for-the-badge&logo=fire&logoColor=white" />
</p>
<br>

<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%">

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 👨‍💻 Identitas
- **Nama:** Satria Bagas Sejati
- **NIM:** 552012610009
- **Prodi:** Teknik Informatika - Semester 1
- **Universitas:** Cahaya Surya Kediri
- **Repo:** `python-semester-1` - Kumpulan Project Python dari Nol

> "Ini bukan sekedar tugas, tapi jejak pertama saya di dunia developer."

---

## 📚 Daftar Project Semester 1

Repo ini adalah monorepo - semua project Python semester 1 aku kumpulin di sini biar rapi dan jadi portofolio.

| No | Folder | Nama Project | Fokus Materi | Status |
| :--- | :--- | :--- | :--- | :--- |
| 01 | [`01-Kasir-Toko-Diskon`](./01-Kasir-Toko-Diskon/) | Kasir Toko + Diskon | Function, While, Validasi Input | ✅ Done |
| 02 | [`02-Game-Sederhana`](./02-Game-Sederhana/) | Tebak Angka & Batu Gunting Kertas | Random, While, Skor | ✅ Done |
| 03 | [`03-Nilai-Mahasiswa`](./03-Nilai-Mahasiswa/) | Aplikasi Nilai Mahasiswa | List, Dict, File Handling | ✅ Done |

---

## 🔍 Detail Project

### 01 - Kasir Toko + Diskon
File: `kasir.py`

**Fitur Utama:**
1. Tambah banyak barang sekaligus, ketik `selesai` untuk hitung
2. Hitung total, diskon, dan kembalian otomatis
3. Validasi input (huruf / angka negatif ditolak)
4. Cetak struk belanja yang rapi

**Alur Pengembangan:**
1. Rancang fungsi `hitung_diskon()` untuk aturan diskon bertingkat
2. Pakai `while` untuk input barang terus-menerus
3. Hitung subtotal tiap barang dan total belanja
4. Validasi uang bayar, kalau kurang diulang lagi
5. Cetak struk pakai fungsi `tampilkan_struk()`

**Logika Diskon:**
- Total >= Rp 500.000 = Diskon 20%
- Total >= Rp 200.000 = Diskon 10%
- Total >= Rp 100.000 = Diskon 5%
- Total < Rp 100.000 = 0%

### 02 - Game Sederhana
File: `game.py`

**Fitur Utama:**
1. **Tebak Angka:** Tebak angka 1-100, punya 7 nyawa, ada sistem skor
2. **Batu Gunting Kertas:** Lawan komputer, ada rekap Menang / Kalah / Seri

**Alur Pengembangan:**
1. Buat menu utama pakai `while` biar bisa pilih game
2. Game Tebak Angka pakai `random.randint(1, 100)`
3. Kasih clue "terlalu besar / terlalu kecil" tiap tebakan
4. Game Batu Gunting Kertas pakai `random.choice()`
5. Buat logika menang/kalah pakai `if-elif` dan hitung skor

### 03 - Aplikasi Nilai Mahasiswa
File: `nilai_mahasiswa.py`

**Fitur Utama:**
1. Tambah, Lihat, Cari, dan Hapus Mahasiswa
2. Otomatis hitung Nilai Huruf (A-E) & Status Lulus / Tidak Lulus
3. Hitung Rata-rata Kelas, Nilai Tertinggi & Terendah
4. Data tersimpan di `data_nilai.txt`, jadi tidak hilang saat program ditutup

**Alur Pengembangan:**
1. Simpan data pakai `list` + `dict`
2. Buat fungsi `hitung_nilai_huruf()` dan `hitung_status()`
3. Buat fungsi `simpan_ke_file()` dan `baca_dari_file()` biar data permanen
4. Cek NIM duplikat sebelum tambah data
5. Tampilkan tabel nilai yang rapi pakai formatting

**Aturan Nilai:**
- 85 - 100 = A (LULUS)
- 75 - 84 = B (LULUS)
- 65 - 74 = C (LULUS)
- 55 - 64 = D (TIDAK LULUS)
- 0 - 54 = E (TIDAK LULUS)

---

## ✨ Harapan & Journey di GitHub

Sebagai mahasiswa baru, ini langkah pertama ku:
1. **Belajar Open Source:** Paham Git & version control
2. **Bangun Portofolio Digital:** Dokumentasi belajar dari nol
3. **Feedback:** Terbuka buat masukan dosen & teman
4. **Konsistensi:** Komitmen upload setiap project kecil selama kuliah
5. **Motivasi:** Kode yang di-publish = motivasi buat nulis kode rapi

---

## 💻 Cara Menjalankan

Pastikan sudah install Python.

```bash
# Clone repo
git clone https://github.com/SatriaXD766/python-semester-1.git
cd python-semester-1

# Run Kasir
cd 01-Kasir-Toko-Diskon
python kasir.py

# Run Game
cd ../02-Game-Sederhana
python game.py

# Run Nilai Mahasiswa
cd ../03-Nilai-Mahasiswa
python nilai_mahasiswa.py
