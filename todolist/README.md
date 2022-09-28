# Link Herokuapp
https://rafighalibinpbptugas2.herokuapp.com/todolist/login/?next=/todolist/

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF token adalah Cross-Site Request Forgery token yang berfungsi untuk memastikan HTTP request yang datang benar dari aplikasi yang kita buat bukan dari penyerang. sehingga jika {% csrf_token %} dihapus aplikasi tidak akan bisa memverivikasi HTTP request dan akan menghasilkan HTTP request kita di batalkan.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya kita bisa, dengan menggunakan wrapper <form> dan setelah itu kita menentukan attribut method dan action dengan value yang sesuai. attribut action digunakan untuk menspesifikasikan endpoint request yang akan diberikan. attribut method digunakan untuk menspesifikasi HTTP method yang akan digunakan untuk mengirim request ke server. setelah itu kita memasukkan elemen <input> kedalam wrapper <form> dan kita dapat memilih attribut type pada inout untuk menentukan tipe input yang akan dibuat

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
