link : https://afero-aqil-footballnews.pbp.cs.ui.ac.id/        
Nama : Afero Aqil Roihan
NPM  : 2406352304
Kelas: PBP D

Cara saya membuat aplikasi main pada django, merouting, dan menghubungan ke PWS:
1. Membuat virtual environment dan mengunduh Dependencies yang diperlukan.
2. Membuat proyek django dengan "django-admin startproject allmighty_store" .
3. Mengonfigurasi dengan membuat file .env , pada settings.py, mengatur isi databases, dan menambahkan allowed hosts.
4. Menambahkan aplikasi main dengan "python manage.py startapp main", dan mendaftarkan aplikasi main pada settings.py. 
5. Pada direktori main, Menambahkan direktori templates, lalu di dalamnya ditambahkan lagi berkas main.html .
6. Pada direktori main, mengisi models yang diperlukan pada models.py.
7. Migrasi model.
8. Menghubungkan views dengan template dengan menggunakan fungsi render pada views.py agar dapat merender tampilan  .
9. Routing URL : Membuat berkas urls.py pada direktori main dan menambahkan url main pada berkas urls.py pada direktori proyek.
10. push ke repository dan PWS.

request client ke web aplikasi berbasis Django dan  kaitan antara urls.py, views.py, models.py, dan berkas html.:
![alt text](image.png)

sumber gambar (hal 3) : https://scele.cs.ui.ac.id/pluginfile.php/269605/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf

Alur dan hubungan antar urls.py, views.py, models.py, dan berkas html :
1. User akan mengirimkan request berupa url, lalu dicek di urls.py untuk mencari view yang sesuai.
2. Views.py yang berisi logika-logika, menentukan apa yang akan dilakukan selanjutnya (membaca atau menulis data) dan akan mengambil data-data yang diperlukan dari models.py .
3. Views.py yang sudah mendapatkan data yang diperlukan, mengirimkannya ke HTML untuk ditampilkan kepada user.

Fungsi settings.py pada proyek django: Konfigurasi utama dalam sebuah proyek django, seperti untuk mengatur  databases yang dipakai, menambahkan aplikasi, mengatur host yang dibolehkan, dan lain-lain.

Cara kerja migrasi database di django : ketika kita menjalankan perintah "python manage.py makemigrations" di terminal, sistem akan membuat file baru di folder /migrate pada direktori aplikasi (dalam projek ini, direktori main) yang berisi perbedaan model sebelum dan setelah diubah. Lalu perintah "python manage.py migrate" akan membaca file tersebut dan menerapkan perubahannya ke database.

Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak:
1. Django digunakan dengan bahasa python, yang merupakan bahasa pemrograman yang lebih relatif mudah.
2. Fitur di django sudah lengkap, sehinga tidak perlu lagi mencari library yang dibutuhka untuk keperluan tertentu.
3. Terdapat admin panel, sehingga developer pemula bisa langsung melihat hasil coding mereka.
4. Memiliki komunitas yang besar, sehingga kita dapat dengan mudah menemukan solusi dari suatu permasalahan yang ditemukan di django.
Sumber : https://www.geeksforgeeks.org/blogs/top-10-reasons-to-choose-django-framework-for-your-project/

Feedback untuk Tutorial 1: Tidak ada.
