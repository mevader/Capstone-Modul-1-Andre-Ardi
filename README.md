**DATABASE YELLOW PAGES MENGGUNAKAN PYTHON**

**ANDRE ARDI**

-TUJUAN DARI PROGRAM: Memudahkan user/admin dalam memanfaatkan database Yellow Pages 

-Yellow Pages disini saya definisikan sebagai buku telepon modern yang memasukkan nomor handphone dan alamat email di samping alamat dan pekerjaan

-Program ini didasarkan pada empat fitur utama:
1. Read
2. Create
3. Update
4. Delete

-Keempat fitur tersebut akan diterjemahkan ke dalam sepuluh menu utama, sebagai berikut:
![image](https://github.com/mevader/Capstone-Modul-1-Andre-Ardi/assets/160390827/c2d09e63-55fa-4fdf-91f6-066b8ec68dd7)

-Menu-menu tersebut dapat diakses dengan menggunakan input nomor menu

-Tabel data Yellow Pages yang akan ditampilkan adalah sebagai berikut:
![image](https://github.com/mevader/Capstone-Modul-1-Andre-Ardi/assets/160390827/51dee82c-c2de-4d50-9484-68892a48f968)

-Selanjutnya bagaimana isi dari menu-menu di atas:

**Menu 1. Menampilkan seluruh daftar**

-Menu ini bertujuan menampilkan keseluruhan data dari Yellow Pages
   
**Menu 2. Menampilkan data berdasarkan nomor Yellow Pages**

-Menu ini bertujuan memanggil data berdasarkan nomor unik/id dari daftar nama di Yellow Pages

-Di dalamnya terdapat opsi masukkan nomor Yellow Pages

-Tampil data dari nomor yang dipanggil

-Bila nomor yang dimasukkan tidak ada maka akan muncul keterangan

-Lalu opsi lanjut atau tidak 

**Menu 3. Menampilkan data berdasarkan nama tertentu**

-Menu ini akan memanggil dan menampilkan data berdasarkan nama yang diinput

-Bila nama tidak ditemukan akan muncul keterangan

-Terdapat opsi untuk keluar/lanjut

**Menu 4. Menampilkan data berdasarkan alamat tertentu**

-Menu ini akan memanggil dan menampilkan data berdasarkan alamat yang diinput

-Bila alamat tidak ditemukan akan muncul keterangan

-Terdapat opsi untuk keluar/lanjut

**Menu 5. Menampilkan data berdasarkan pekerjaan tertentu**

-Menu ini akan memanggil dan menampilkan data berdasarkan alamat yang diinput

-Bila alamat tidak ditemukan akan muncul keterangan

-Terdapat opsi untuk keluar/lanjut

**Menu 6. Menambah data**

-Merupakan menu yang bertujuan menambahkan data pada urutan akhir daftar

-Di dalamnya akan menambahkan data baru pada seluruh kolom key data, yaitu:

-Nomor Yellow Pages
1. Nama
2. Alamat
3. Pekerjaan
4. Nomor HP
5. email
-Selesai data dimasukkan akan muncul opsi lanjut/tidak

**Menu 7. Memperbarui data tertentu**

-Fitur ini akan menambahkan data ‘value’ baru pada kolom ‘key’ yang dipilih berdasarkan ‘index’ yang diinput
-Bila ‘index’ tidak ditemukan maka akan muncul keterangan
-Bila ‘key’ tidak ditemukan juga akan muncul keterangan
-Selanjutnya ‘value’ baru diinput berdasarkan ‘key’ pilihan
-Selesai data dimasukkan akan muncul opsi lanjut/tidak

**Menu 8. Menghapus data tertentu**

-Fitur ini akan menghapus dictionary data tertentu berdasarkan nomor index yang dipilih
-Selesai data dihapus akan muncul opsi lanjut hapus/tidak

**Menu 9. Menghapus seluruh data**

-Fitur ini akan menghapus seluruh data di dalam Yellow Pages 
-Sebelum penghapusan akan muncul pertanyaan untuk memastikan bahwa user benar-benar yakin akan menghapus seluruh data
 
**Menu 10. Keluar**

-Fitur ini akan mengeluarkan user dari program database Yellow Pages
