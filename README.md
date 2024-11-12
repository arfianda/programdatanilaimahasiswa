# Program Pengelolaan Data Nilai Mahasiswa

Program ini dibuat untuk mengelola data nilai mahasiswa dengan kemampuan untuk menambahkan data secara dinamis dan menghitung nilai akhir berdasarkan komponen-komponen nilai yang telah ditentukan.

## Deskripsi Program

Program ini memungkinkan pengguna untuk:
1. Memasukkan data mahasiswa secara berulang
2. Menghitung nilai akhir berdasarkan bobot:
   - Tugas: 30%
   - UTS: 35%
   - UAS: 35%
3. Menampilkan hasil dalam format tabel yang rapi

### Struktur Program

Program terdiri dari dua komponen utama:

1. **Class Student**
   ```python
   class Student:
       def __init__(self, nama, nim, tugas, uts, uas):
           self.nama = nama
           self.nim = nim
           self.tugas = tugas
           self.uts = uts
           self.uas = uas
           self.nilai_akhir = self.hitung_nilai_akhir()
   ```
   - Class ini berfungsi sebagai template untuk menyimpan data setiap mahasiswa
   - Memiliki method `hitung_nilai_akhir()` untuk menghitung nilai akhir berdasarkan bobot

2. **Function main()**
   - Fungsi utama yang menjalankan logika program
   - Mengatur alur input dan output program
   - Mengelola penyimpanan data dalam list

## Flowchart Program

<img src="/img/datamahasw.drawio.png" width="500" alt="">

### Algoritma Program

1. **Inisialisasi**
   - Membuat list kosong untuk menyimpan data mahasiswa
   - Mempersiapkan variabel-variabel yang diperlukan

2. **Input Data**
   - Program meminta input data mahasiswa:
     * Nama
     * NIM
     * Nilai Tugas
     * Nilai UTS
     * Nilai UAS
   - Data divalidasi untuk memastikan format yang benar

3. **Proses Perhitungan**
   - Nilai akhir dihitung dengan rumus:
     ```
     Nilai Akhir = (Tugas × 30%) + (UTS × 35%) + (UAS × 35%)
     ```
   - Hasil perhitungan disimpan dalam objek Student

4. **Penyimpanan Data**
   - Setiap data mahasiswa disimpan dalam list
   - Program menanyakan apakah ingin menambah data lagi
   - Jika 'y', kembali ke langkah input data
   - Jika 't', lanjut ke tampilan hasil

5. **Output Hasil**
   - Menampilkan header tabel
   - Melakukan loop untuk setiap data mahasiswa
   - Menampilkan data dalam format tabel yang rapi

## Cara Penggunaan

1. **Menjalankan Program**
   ```bash
   python program_nilai.py
   ```

2. **Input Data**
   - Masukkan nama mahasiswa
   - Masukkan NIM
   - Masukkan nilai tugas (0-100)
   - Masukkan nilai UTS (0-100)
   - Masukkan nilai UAS (0-100)

3. **Menambah Data**
   - Ketik 'y' untuk menambah data baru
   - Ketik 't' untuk menampilkan hasil

4. **Melihat Hasil**
   - Program akan menampilkan tabel berisi semua data yang telah diinput
   - Format tabel menampilkan:
     * Nomor urut
     * Nama mahasiswa
     * NIM
     * Nilai Tugas
     * Nilai UTS
     * Nilai UAS
     * Nilai Akhir (hasil perhitungan)

## Contoh Output




## Requirements
- Python 3.x
- Tidak memerlukan library tambahan

## Author
ARFIANDA F SATRITAMA