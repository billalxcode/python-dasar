# Ganjil Genap
Program ini dibuat untuk mengecek apakah angka tersebut merupakan angka ganjil atau genap.

# Bagaimana cara kerja?
Kita tahu bahwa angka ganjil merupakan angka yang tidak habis dibagi 2. Disini kita menggunakan operator modulus, yaitu operator untuk mengetahui sisa bagi dari angka yang kita masukan. 
Contoh nya:
1. Pertama angka `10` tidak bisa dibagi dengan angka `2`
2. Kedua angka `5` bisa dibagi dengan angka `2`

Jika di bahasa pemrogramman python anda bisa menggunakan operator modulus dengan simbol `%` yang dapat diimplementasikan sebagai berikut
```python
angka % 2
```

**INGAT!!** Jika kode tersebut mengeluarkan angka `0` sudah dipastikan kode tersebut tidak bisa dibagi `2`. Maka, sebaliknya jika kode tersebut mengeluarkan angka `1` sudah dipastikan kode tersebut bisa dibagi `2`.

Hal ini dapat anda pelajari dalam [Sistem Bilangan Biner](https://id.wikipedia.org/wiki/Sistem_bilangan_biner)

Sebagai contoh
```python3
hasil = 10 % 2
```
Maka kode diatas akan menghasilkan angka `0` yang berarti bahwa kode tersebut merupakan angka genap. Kenapa? karena keluaran nya merupakan angka `0` jika di dalam [Sistem Bilangan Biner](https://id.wikipedia.org/wiki/Sistem_bilangan_biner) angka `0` adalah `false` atau `salah`, yang artinya bahwa angka 10 merupakan angka genap. Kenapa? karena jika kode menghasilkan angka `1` maka angka tersebut merupakan angka ganjil.

## Penutup
Terima kasih sudah berkunjung dalam repostory ini, semoga bermanfaat. Jika ada kesalahan, kekurangan, maupun ketidak pahaman silahkan membuat issue [Disini](https://github.com/billalxcode/python-dasar/issues)