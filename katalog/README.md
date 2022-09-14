
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

# Cara Implementasi
