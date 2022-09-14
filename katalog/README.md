
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


```mermaid
flowchart LR;
HTTP_Request-->urls.py;
```
1.

```mermaid
flowchart LR;
urls.py-->|Forward request to approproate view|views.py;
```
2.

```mermaid
flowchart LR;
views.py<-->|read/write data|models.py;
```
3.

```mermaid
flowchart LR;
views.py-->HTTP_Response;
```
4.

```mermaid
flowchart LR;
katalog.html-->views.py;
```
5.

# Mengapa Kita Perlu Menggunakan Virtual Environment?
Dengan menggunakan virtual environment kita akan mendapatkan semacam ruang isolasi untuk menginstall libraries yang dibutuhkan projek kita. Dengan adanya virtual environment kita tidak akan menginstall libraries di sistem operasi kita secara langsung. Keuntungan dari virtual environment kita dapat menggunakan liblary dengan versi yang berbeda untuk projek yang berbeda. Selain itu kita juga bisa dengan muda menduplikat projek karena kita tahu libraries apa saja yang digunakan karena sudah terkumpul di satu ruangan yang terisolasi. Tanpa virtual environment kita masih bisa membuak projek Django namun kita tidak akan mendapatkan keuntungan yang disebutkan diatas.
# Cara Implementasi
