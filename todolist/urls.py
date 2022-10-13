from django.urls import path
from todolist.views import create_task_json, register, show_json, delete_todo
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
    path('json/', show_json, name='show_json'),  
    path('create-task/', create_task, name='create_task'),
    path('add/', create_task_json, name='create_task_json'),
    path('delete/<int:id>', delete_todo, name='delete_todo'),
    path('update-task/<int:id>', update_task, name='update_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    
]