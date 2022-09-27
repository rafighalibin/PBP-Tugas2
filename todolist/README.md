# Link Herokuapp
https://rafighalibinpbptugas2.herokuapp.com/todolist/login/?next=/todolist/


# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF token adalah Cross-Site Request Forgery token yang berfungsi untuk memastikan HTTP request yang datang benar dari aplikasi yang kita buat bukan dari penyerang. sehingga jika {% csrf_token %} dihapus aplikasi tidak akan bisa memverivikasi HTTP request dan akan menghasilkan HTTP request kita di batalkan.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.


# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


#Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
