# UTS_ComputerVision

Nama    : ERLANGGA LUTFI ARDANA
NIM     : 43050230031
KELAS   : TI/5B

1. Penjelasan singkat karakter yang dibuat
- Deskripsi Karakter Stickman
    Karakter yang dibuat merupakan stickman sederhana, yaitu representasi manusia menggunakan garis dan lingkaran.
    Stickman ini berfungsi sebagai objek latihan dasar Computer Vision untuk memahami bagaimana menggambar bentuk dan melakukan transformasi citra menggunakan OpenCV.
    
- Komponen Karakter
    1. Kepala → Dibuat dengan fungsi cv2.circle() berwarna putih.
        → Melambangkan bagian kepala manusia.
    2. Badan → Digambar dengan cv2.line() secara vertikal dari leher ke pinggang.
    3. Tangan → Dua garis diagonal dari badan, melambangkan tangan kiri dan kanan.
    4. Kaki → Dua garis diagonal ke bawah dari ujung badan, sebagai kaki kiri dan kanan.
    5. Teks Nama → Ditambahkan tulisan “Stickman Gor” menggunakan cv2.putText() agar karakter memiliki identitas.

- Tujuan Pembuatan
    1. Karakter ini digunakan untuk demonstrasi transformasi citra digital menggunakan OpenCV:
    2. Translasi → Menggeser posisi stickman di kanvas.
    3. Rotasi → Memutar karakter terhadap titik pusatnya.
    4. Resize dan Crop → Mengubah ukuran serta memotong sebagian gambar.
    Dengan karakter sederhana seperti ini, mahasiswa dapat lebih mudah memahami konsep dasar transformasi geometrik dalam pengolahan citra digital.
