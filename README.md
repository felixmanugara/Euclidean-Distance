# Script untuk menghitung jarak error antara koordinat GPS

karena saya tidak bisa menghitung jarak error antara koordinat GPS tanpa membuat kesalahan, maka dari itulah script ini dibuat. Script ini dibuat berdasarkan sebuah formula yang saya dapatkan dari jurnal berjudul "Implementasi Internet of Things pada Sistem Informasi Pelacakan Kendaraan Bermotor Menggunakan GPS Berbasis Web".

berikut adalah formula yang digunakan untuk menghitung koordinat: 

$ Z=\sqrt{(B-A)^2-(D-C)^2}$

A = nilai latitude yang sebenarnya
\
B = nilai latitude dari modul
\
C = nilai longitude yang sebenarnya
\
D = nilai longitude dari modul
\
1 derajat di maps = 111.322 kilometer



## Journal Link
Jurnal bisa didapatkan pada [jtika.if.unram.ac.id](https://bit.ly/3jALUFb)


# Requirements 
Berikut adalah requirements yang dibutuhkan untuk menjalankan script ini

- pip
- matplotlib
- numpy
- math
