from django.shortcuts import render
from katalog.models import CatalogItem

data_barang_katalog = CatalogItem.objects.all()
def show_katalog(request):
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Rafi Ghalibin Abrar',
        'id': '2106751354'
    }
    return render(request, "katalog.html", context)