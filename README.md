# Pertemuan 06 - Nested Loop, Pola, Akumulasi, dan Pencacahan

**Nama:** Siti Amaliah
**NIM:** 2225250223
**Kelas:** 3E

## Tujuan

Mempelajari dan menerapkan nested loop, pola, akumulasi, dan pencacahan menggunakan Python di VS Code.

## Struktur Program

Program yang dibuat terdiri dari beberapa latihan dan satu tugas utama:

* `latihan/01_pasangan_indeks.py`
* `latihan/02_pola_segitiga.py`
* `latihan/03_jumlah_per_baris.py`
* `latihan/04_hitung_pasangan.py`
* `tugas/tabel_perkalian_dan_statistik.py`

## Cara Menjalankan

Program dijalankan menggunakan Python melalui terminal VS Code.

Contoh menjalankan Tugas 3:

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

1. Membaca nilai `n`.
2. Memastikan nilai `n` merupakan bilangan positif.
3. Membuat variabel `total_semua` untuk menghitung total seluruh hasil perkalian.
4. Membuat `count_genap` untuk menghitung banyak hasil perkalian yang genap.
5. Menggunakan nested loop, yaitu loop luar untuk baris dan loop dalam untuk kolom.
6. Menghitung hasil perkalian `i × j`.
7. Menambahkan hasil ke jumlah pada setiap baris dan total keseluruhan.
8. Jika hasil perkalian genap, maka `count_genap` bertambah satu.
9. Menampilkan jumlah setiap baris.
10. Menampilkan total seluruh hasil perkalian dan banyak hasil genap.

## Hasil Pengujian

| Input n | Jumlah Pasangan | Total Semua | Hasil Genap | Status   |
| ------- | --------------: | ----------: | ----------: | -------- |
| 1       |               1 |           1 |           0 | Berhasil |
| 2       |               4 |           9 |           3 | Berhasil |
| 3       |               9 |          36 |           5 | Berhasil |

## Analisis Efisiensi

Untuk input `n`, nested loop menjalankan bagian dalam sebanyak `n × n` kali. Jadi, semakin besar nilai `n`, semakin banyak perulangan yang dilakukan.

## Refleksi

Kesalahan yang perlu diperhatikan dalam nested loop adalah posisi inisialisasi variabel. `total_baris` harus diatur kembali menjadi 0 pada setiap baris, sedangkan `total_semua` dan `count_genap` harus tetap berjalan sampai seluruh perulangan selesai.
