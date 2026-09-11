# Sistem Pemilihan Lagu Untuk Pembuatan Playlist
**Nama :** Nova Cynthia <br>
**NIM :** 2609116031 <br>
**Program Studi :** Sistem Informasi <br>
**Kelas :** A 2026 <br>
**Mata Kuliah :** Dasar-Dasar Pemograman <br>

## Deskripsi
Program ini dibuat untuk pengguna dapat memilih lagu dengan list lagu yang sudah tersedia sebelumnya. Pengguna juga dapat menambahkan nama playlist secara bebas (angka atau huruf atau gabungan). Agar mudah dipahami dan digunakan oleh pengguna serta tampilan sistem lebih sederhana, maka dibuatkan sistem "Menu Playlist" yang digunakan untuk menambahkan ke playlist dan menghapus lagu dari playlist. Hasil akhirnya pengguna dapat melihat daftar lagu yang ada di playlist.

## Flowchart
Berikut flowchart dari sistem pemilihan lagu untuk pembuatan playlist <br>
<br>
<img width="1460" height="2042" alt="Minpro1_DDP" src="https://github.com/user-attachments/assets/45c7fd2c-14f5-42ff-9e5f-8a4893984cc4" />

## Output
### Pemilihan nama playlist
Pengguna dapat memasukkan nama playlist secara bebas (angka atau huruf atau gabungan). Nama playlist tersebut akan ditampilkan saat ingin menghapus lagu yang sudah dipilih dan dibagian akhir ketika playlist sudah tetap atau *fiks*. <br>
<br>
<img width="800" alt="Screenshot 2026-09-11 212834 - Copy" src="https://github.com/user-attachments/assets/5c95a4bf-074b-4d70-8fb7-d41c12929267" />

### Daftar lagu
Daftar lagu ini hanya ditampilkan sekali, yaitu di awal sebagai pemberitahuan kepada pengguna tentang lagu-lagu yang tersedia
<img width="500" alt="Screenshot 2026-09-11 231119" src="https://github.com/user-attachments/assets/db616c0b-d66a-40e7-94da-eb993319f6b1" />

### Daftar menu playlist
Pada daftar menu playlist terdapat tambah lagu, hapus lagu, dan selesai. Pengguna dapat memilih dengan menginputkan berupa angka, jika pengguna menasukkan angka yang tidak ada di menu playlist maka sistem akan menampikan "Pilihan tidak tersedia" dan melakukan *looping* ke pemilihan menu playlist.
#### a. Output daftar menu playlist
<img width="500" alt="Screenshot 2026-09-11 230515" src="https://github.com/user-attachments/assets/84259f2e-762d-440d-877d-647cd08d5030" />



#### b. Output ketika pengguna memasukkan angka yang tidak ada di menu playlist
<img width="500" alt="Screenshot 2026-09-11 213556" src="https://github.com/user-attachments/assets/9db1bfc8-07a7-48c9-abb4-35dfefdb9dbc" />

### Pilihan "Tambah lagu"
Program ini berguna untuk memilih lagu yang ingin ditambahkan ke playlist sesuai daftar lagu yang ditampilkan di awal. Pengguna dapat memilih sebanyaknya, karena sistem ini menggunakan pertanyaan ***looping***. Program ini juga dirancang ketika lagu yang sudah dipilih sebelumnya akan terbaca oleh sistem dan akan menampilkan bahwa lagu tersebut sudah ditambahkan ke playlist. Pengguna memilih dengan menggunakan angka, ketika pengguna memasukkan angka yang tidak sesuai maka sistem akan menampilkan "Nomor tidak tersedia" dan ketika pengguna memasukan huruf maka sistem akan menampilkan "Harus berupa nomor!". Jika pengguna sudah selesai memilih, pengguna tinggal memasukkan angka "0" yang berarti selesai dan akan kembali ke menu playlist.
#### a. Output menambahkan lagu
<img width="500" alt="Screenshot 2026-09-11 212834" src="https://github.com/user-attachments/assets/097bdc87-4ccb-4b8c-9cd6-f6c94749283a" />


#### b. Output ketika nomor lagu yang dimasukkan pengguna pilih kembali
<img width="500" alt="Screenshot 2026-09-11 212858" src="https://github.com/user-attachments/assets/987195db-bd15-442e-b837-46b299f76b9f" />



#### c. Output ketika nomor yang dimasukkan tidak tersedia dan ketika memasukkan selain angka
<img width="500" alt="Screenshot 2026-09-11 213025" src="https://github.com/user-attachments/assets/344ec649-9978-45ad-9bee-ac097de5ad19" />


### d. Output "0" (selesai)
<img width="500" alt="Screenshot 2026-09-11 212921" src="https://github.com/user-attachments/assets/ebb7abb5-d599-4510-98f2-e33dd2e634a5" />

### Pilihan "Hapus lagu"
Program ini berguna untuk menghapus lagu yang sudah dipilih sebelumnya oleh pengguna. Jika pengguna belum menambahkan lagu ke dalam playlist maka output yang dihasilkan adalah playlist kosong dan melakukan ***looping*** ke menu playlist. Sistem pemilihan masih berupa pengguna memasukkan angka. Ketika nomor yang dimasukkan tidak ada maka program akan menampilkan "Nomor tidak tersedia" dan ketika memasukkan selain angka maka program akan menampilkan "Harus berupa nomor!". Lalu, jikalau pengguna tidak jadi menghapus lagu yang ada di playlist, pengguna tinggal mengetik "0" yang berarti batal dan melakukan ***looping*** ke menu playlist.
#### a. Output setelah menambahkan lagu ke playlist
<img width="500" alt="Screenshot 2026-09-11 213050" src="https://github.com/user-attachments/assets/3f2133d1-5500-4ac9-8d13-e0e838fa3c8b" />


#### b. Output ketika playlist kosong
<img width="500" alt="Screenshot 2026-09-11 213438" src="https://github.com/user-attachments/assets/4f476b38-6292-49ca-a5d4-231244c5632d" />


#### c. Output ketika nomor tidak ada dan ketika memasukkan selain angka
<img width="500" alt="Screenshot 2026-09-11 213244" src="https://github.com/user-attachments/assets/df18f538-0543-462a-a264-3892181a43e7" />


#### d. Output "0" (batal)
<img width="500" alt="Screenshot 2026-09-11 213212" src="https://github.com/user-attachments/assets/52778b88-d59c-4b90-93c5-570ced8117fa" />


### Pilihan "Selesai"
Program ini adalah akhir dari sistem pemilihan lagu untuk pembuatan playlis yang menampilkan isi playlist yang tetap atau *fiks*. Jika pengguna belum menambahkan lagu ke dalam playlist maka output yang dihasilkan adalah playlist kosong.
#### a. Output setelah menambahkan atau menghapus atau keduanya ke playlist
<img width="500" alt="Screenshot 2026-09-11 213319" src="https://github.com/user-attachments/assets/0f5e4149-b07a-48bc-8e29-f49c7d536a5a" />


#### b. Output ketika playlist kosong
<img width="500" alt="Screenshot 2026-09-11 213532" src="https://github.com/user-attachments/assets/c647be33-78df-451a-9b40-f50d84c0872f" />

## Nilai tambah dan hasil akhir semuanya
<img width="350" alt="Screenshot 2026-09-12 000654" src="https://github.com/user-attachments/assets/71cdcfa5-9934-45bd-aede-60fd91d17afd" />
<br>
<img width="350" alt="Screenshot 2026-09-12 000825" src="https://github.com/user-attachments/assets/b535b771-6ac5-45fa-85ca-45b93ef83334" />
<br>
<img width="350" alt="Screenshot 2026-09-12 000844" src="https://github.com/user-attachments/assets/100d32b2-ff7a-41cd-8a54-446b6d9cb4fe" />
