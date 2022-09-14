
# Link Herokuapp
https://rafighalibinpbptugas2.herokuapp.com/katalog/

# Bagan Request Client
```mermaid
flowchart TB;
    HTTP_Request-->urls.py;
    urls.py-->|Forward request to approproate view|views.py;
    views.py<-->|read/write data|models.py;
    views.py-->HTTP_Response;
    katalog.html-->views.py;
```
Penjelasan:
Request diminta oleh user ke server, kemudian urls.py akan mengarahkan request ke views.py. Method yang ada di views.py akan mencetak data-data di katalog.html. Data disimpan dalam bentuk class CatalogItem yang ada di models.py. Kemudian server akan mengembalikan Response ke user.

# Mengapa Kita Perlu Menggunakan Virtual Environment?
Dengan menggunakan virtual environment kita akan mendapatkan semacam ruang isolasi untuk menginstall libraries yang dibutuhkan projek kita. Dengan adanya virtual environment kita tidak akan menginstall libraries di sistem operasi kita secara langsung. Keuntungan dari virtual environment kita dapat menggunakan liblary dengan versi yang berbeda untuk projek yang berbeda. Selain itu kita juga bisa dengan muda menduplikat projek karena kita tahu libraries apa saja yang digunakan karena sudah terkumpul di satu ruangan yang terisolasi. Tanpa virtual environment kita masih bisa membuak projek Django namun kita tidak akan mendapatkan keuntungan yang disebutkan diatas.
# Cara Implementasi
