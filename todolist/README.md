# Link Herokuapp
https://rafighalibinpbptugas2.herokuapp.com/todolist/login/?next=/todolist/

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF token adalah Cross-Site Request Forgery token yang berfungsi untuk memastikan HTTP request yang datang benar dari aplikasi yang kita buat bukan dari penyerang. sehingga jika {% csrf_token %} dihapus aplikasi tidak akan bisa memverivikasi HTTP request dan akan menghasilkan HTTP request kita di batalkan.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya kita bisa, dengan menggunakan wrapper <form> dan setelah itu kita menentukan attribut method dan action dengan value yang sesuai. attribut action digunakan untuk menspesifikasikan endpoint request yang akan diberikan. attribut method digunakan untuk menspesifikasi HTTP method yang akan digunakan untuk mengirim request ke server. setelah itu kita memasukkan elemen <input> kedalam wrapper <form> dan kita dapat memilih attribut type pada inout untuk menentukan tipe input yang akan dibuat. kemudian kita memberikan attribut name yang nanti akan menjadi key dari value yang didapatkan dari input. terakhir kita membuat sebuah button untuk men-submit form yang sudah di isi.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
saat user melakukan submit form akan terjadi HTTP request ke server dengan method dan action yang ada di form. kemudian action akan memetakan request ke URL, sesuai dengan yang ada di urls.py. kemudian akan dilanjutkan ke method yang sesuai di views.py yang kemudian akan men render data di html.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
