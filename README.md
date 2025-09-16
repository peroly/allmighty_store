link : https://afero-aqil-allmightystore.pbp.cs.ui.ac.id/    
Nama : Afero Aqil Roihan
NPM  : 2406352304
Kelas: PBP D

Tugas 2

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
<

Tugas 3

Manfaat Data Delivery :
- Pengguna mendapat data yang paling terbaru, sehingga tidak tertinggal pada data yang lama.
- Platform menjadi lebih interaktif karena pertukaran antar data.

Menurut saya, XML atau JSON : Saya lebih memilih JSON karena lebih mudah untuk dibaca.
Alasan JSON lebih popular dibandingkan XML : Lebih mudah dibaca manusia dibandingkan XML, karena syntax JSON lebih sederhana.

Fungsi dari method is_valid() pada django : untuk mengecek apakah data pada form sudah benar. Tujuannya untuk memastikan data yang dikirim ke server sudah sesuai format. Contoh : User tidak mengisi data pada form yang seharusnya diisi, maka is_valid() akan return false.

Mengapa kita membutuhkan csrf_token saat membuat form di Django : Kita membutuhkannya untuk mencegah serangan berbahaya saat form dikirimkan. Jika kita tidak menggunakan csrf_token, django akan memberikan ERROR seperti terlihat di gambar di bawah ini :
![alt text](image-1.png)

Jika django tidak memberikan ERROR saat tidak memakai CSRF, server mengandalkan session/cookies untuk mengetahui identitas dari pengirim form. Sehingga ketika penyerang mendapatkan session/cookies pengguna tersebut lalu mengirimkan request ke server, server akan mengira bahwa penyerang adalah user yang sama.

Cara saya menambahkan 4 fungsi views baru(show_xml,show_json,show_xml_id,show_json_id) dan routing urlnya:
1. Buat masing2 fungsinya di views.py .
2. Pada urls.py, direktori main, tambahkan from main.views import show_xml,show_json,show_xml_id,show_json_id, lalu tambahkan path url masing-masing fungsi ke dalam urlpatterns.

Menampilkan tombol add yang akan menambahkan product dan tombol detail pada setiap objek untuk melihat detailnya.
1. Untuk tombol add:
<a href="{% url 'main:create_product' %}">
    <button>+ Add Product</button>

2. Untuk tombol detail :
    <p><a href="{% url 'main:show_product' product.id %}"><button>Detail</button></a></p>

Membuat halaman form dan halaman detail:
1. Setelah tombol ADD Product ditekan, maka akan menjalankan fungsi ini :

    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)

    Selanjutnya fungsi akan membuka create_product.html yang merupakan tampilan untuk add product, lalu jika form valid, form akan disimpan dan kembali ke menu utama.

    Sehingga yang harus saya buat adalah fungsi  create_product() (beserta mengaitkan urls) serta membuat create_product.html.

2. Stelah tombol Detail ditekan, maka akan menjalankan fungsi ini :

   def show_product(request, id):
        product = get_object_or_404(Product, pk=id)
        # product.increment_views()

        context = {
            'product': product
        }

        return render(request, "product_detail.html",    context)

    Selanjutnya fungsi akan membuka product_detail.html yang merupakan tampilan untuk detail produk.

    Sehingga yang harus saya buat adalah fungsi  show_product() (beserta mengaitkan urls) serta membuat product_detail.html.

Foto Postman :
XML
![alt text](image-2.png)

JSON
![alt text](image-3.png)

XML by ID
![alt text](image-5.png)

JSON by ID
![alt text](image-4.png)




