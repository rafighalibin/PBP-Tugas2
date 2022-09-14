https://rafighalibinpbptugas2.herokuapp.com/katalog/

```mermaid
flowchart TB;
    HTTP_Request-->urls.py;
    direction BT;
    urls.py-->|Forward request to approproate view|views.py;
    views.py<-->|read/write data|models.py;
    views.py-->HTTP_Response;
    katalog.html-->views.py;
```

