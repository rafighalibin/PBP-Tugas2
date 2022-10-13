from re import I
from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from todolist.models import Task
from datetime import date, datetime

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task_list = Task.objects.filter(id=id)
    task = task_list[0]
    task.delete()   
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def update_task(request, id):
    task_list = Task.objects.filter(id=id)
    task = task_list[0]
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')
    
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'desc'
        ]

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Task telah berhasil dibuat!')
            return redirect('todolist:show_todolist')
    context = {'form':form}
    return render(request, 'create-task.html', context)


@login_required(login_url='/todolist/login/')
def create_task_json(request):
    if request.method == "POST":
        task = Task(
            title = request.POST["title"],
            desc = request.POST["desc"],
            user = request.user,
        )
        task.save()
        return HttpResponse(
            serializers.serialize("json", [task]),
            content_type="application/json",
        )
    return HttpResponse("Invalid method", status_code=405)

@login_required(login_url="/todolist/login")
def delete_todo(request, id):
    print(request.method)
    if request.method == "DELETE":
        task = Task.objects.filter(id=id).first()
        if task:
            task.delete()
            messages.success(request, "Berhasil dihapus!")
        else:
            messages.error(request, "Task tidak ditemukan!")

    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
        'username': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response