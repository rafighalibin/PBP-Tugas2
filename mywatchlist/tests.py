from urllib import response
from django.test import TestCase, Client
from django.urls import resolve
#from .views import show_watchlist

class MyWatchlistTest(TestCase):
    def test_mywatchlist_html_url_exist(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_xml_url_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_json_url_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    # def test_mywatchlist_using_to_do_list_template(self):
    #     response = Client().get('/mywatchlist/')
    #     self.assertTemplateUsed(response, 'mywatchlist.html')


