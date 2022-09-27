from django.urls import path
from todolist.views import register 
from todolist.views import login_user
from todolist.views import logout_user 
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import update_task
from todolist.views import delete_task


app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('', show_todolist, name='show_todolist'),  
    path('create-task/', create_task, name='create_task'),
    path('update-task/<int:id>', update_task, name='update_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    
]