# Link Herokuapp
https://rafighalibinpbptugas2.herokuapp.com/mywatchlist/html/

# Perbedaan Antara JSON, XML, dan HTML
## JSON
JSON atau JavaScript Object Notation merupakan sebuah format text untuk menyimpan data. JSON merupakan bahasa yang "self-describing" dan mudah untuk dipelajari.

## XML
XML atau eXtensible Markup Language didesain untuk menyimpan data dan merupakan bahasa markup yang mirip seperti HTML. XML juga bersifat self-descriptive

## HTML
HTML atau HyperText Markup Language merupakan bahasa yang didesain untuk dimunculkan di web browser. HTML dapat didampingi dengan bahasa lain seperti CSS untuk mendesain halaman web dan javascrip untuk mengimplementasikan fungsi-fungsi pada halaman web.

## Perbedaan
- JSON berbeda dengan HTML dan XML karena JSON tidak mengggunakan end tag.
- HTML berbeda dengan XML dan JSON karena HTML didesain untuk menampilkan data yang sudah bagus secara estetika dan HTML tidak di desain untuk membawa data, berbeda dengan XML dan JSON.
- JSON tidak mendukung comment, sedangkan XML mendukung.
- JSON hanya mendukung encoding UTF-8, sedangkan XML mendukung berbagai macam encoding.
- data yang ada di JSON akan lebih mudah dibaca dibandingkan dengan yang ada di XML karena data-data yang ada di XML diapit oleh end tag.
- JSON mendukung penggunaan array sedangkan XML tidak.

# Pentingnya data delivery dalam pengimplementasian sebuah platform
# Pengimplementasian
1. Membuat aplikasi mywatchlist dengan menggunakan command 
```
    python manage.py startapp mywatchlist
```
dan saya mendaftarkan mywatchlist kedalam list INSTALLED_APPS yang ada di settings.py pada folder project_django
2. menambahkan path('mywatchlist/', include('mywatchlist.urls')) kedalam list urlpatterns yang ada di urls.py pada folder project_django

3. membuat model MyWatchList didalam models.py pada project mywatchlist. model ini dibuat berdasarkan deskripsi yang diberikan pada soal dan menggunakan field yang sesuai dengan data type yang dibutuhkan.

4. membuat initial data pada initial_mywatchlist_data.json yang ada di fixtures sekaligus men-load data-data tersebut dengan command python manage.py loaddata initial_catalog_data.json

5. membuat method pada views.py yang ada di folder mywatchlist. method tersebut adalah :
- show_watchlist : untuk menampilkan data pada mywatchlist.html
- generate_pesan : implementasi penghitungan jumlah film yang sudah ditonton dan mengembalikan pesan yang sesuai
- show_xml : untuk menampilkan data dalam bentuk XML
- show_json  : untuk menampilkan data dalam bentuk JSON
- show_json_by_id : untuk menampilkan sebuah data dengan id dalam bentuk JSON 
- show_xml_by_id : untuk menampilkan sebuah data dengan id dalam bentuk XML 

6. routing agar setiap data yang dibuat dari method yang ada di views memiliki pathnya sendiri dan dapat dimunculkan di web browser. memasukan semua path pada list urlpatterns yang ada di urls.py di forlder mywatchlist
```
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id')
```
7. menambahkan python manage.py loaddata initial_mywatchlist_data.json pada procfile agar saat aplikasi di deploy akan sekaligus memasukkan 10 data yang sudah dibuat ke program.

9. push ke github sekaligus men deploy aplikasi
# Mengakses URL dengan Postman
![postman](https://user-images.githubusercontent.com/101860971/191470553-f5b5e488-6add-4cfc-88da-38ce98b6b372.jpg)
