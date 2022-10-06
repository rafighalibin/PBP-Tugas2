# Link Herokuapp
https://rafighalibinpbptugas2.herokuapp.com/todolist/login/?next=/todolist/

# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Pada inline CSS style didefinisikan pada tag sehingga jika terlalu banyak akan cukup membingunkan dan akan sangat repetitif jika lebih dari 1 elemen. Namun metode ini cukup bagus untuk pengimplementasian style hanya pada 1 elemen karena tidak perlu mendefinisikan pada style internal

2. Pada internal CSS kita mendefinisikan style didalam tag `<style>`. Kelebihan dari metode ini akan sangat bagus untuk pengimplementasian pada banyak elemen karena akan tidak repetitif. Namun metode ini akan menambah waktu untuk mengakses halaman.


3. Pada internal CSS kita mendefinisikan style didalam file .css dan mengimportnya kedalam file hlml dengan `<link rel="stylesheet" href="style.css">`. dengan ini kita dapat mengimplementasikan style yang sama pada file-file html yang berbeda. Kekurangan dari metode ini kita perlu mengunggu file CSS selesai dipanggil agar dapat dirender dengan sempurna.

# Jelaskan tag HTML5 yang kamu ketahui.
1. `<h1>` sampai `<h6>` : mendefinisikan header, `<h1>` paling besar hingga `<h6>` yang paling kecil
2. `<td>` : mendefinisikan sebuah cell
3. `<script>` : mendefinisikan sebuah script
4. `<p>` : mendefinisikan sebuah paragraf
5. `<body>` : mendefisikan badan html


# Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. `:hover` : mendefinisikan attribut-attribut yang diaplikasikan saat object di hover
2. `*` : semua elemen
3. `p` : elemen p, berlaku untuk semua elemen
4. `#n` : elemen dengan id n, berlaku untuk semua id yang didefinisikan
5. `.classn` : elemen dengan class n, berlaku untuk semua class yang didefinisikan

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. pertama saya mengimplementasikan bootstrap pada base.html agar bootsrap dapat digunakan pada semua template
2. Kemudian saya sapat mengkostumisasi template tugas 4 sesuai ketentuan tugas 5
3. untuk mengimplenetasikan card pada task yang ada saya menggunakan class card. secara garis besar card sama seperti container lainya.
4. untuk mengimplementasikan hover saya menambahkan 
```.card:hover{
        transform: scale(1.05);
    }
```
