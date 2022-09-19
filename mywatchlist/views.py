from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

data_film_watchlist = MyWatchList.objects.all()
def show_watchlist(request):
    sudah=0
    belum=0
    pesan = ""
    for film in data_film_watchlist:
        if film.watched:
            sudah+=1
        else:
            belum+=1
    if sudah>belum:
        pesan = "kamu belum nonton banyak"
    else:
        pesan = "kamu sudah nonton banyak"
    context = {
        'list_film': data_film_watchlist,
        'nama': 'Rafi Ghalibin Abrar',
        'id': '2106751354',
        'pesan' : pesan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")