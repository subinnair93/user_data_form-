from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import UserDataForm, form_user, movie_form
from .models import form_user_data
from django.contrib import messages



# Create your views here.

def hello_world(request):
    return render(request, 'myapp/helloworld.html')

def userdata(request):
    if request.method == 'POST':
        form = movie_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submit')
    return render(request, 'myapp/user_data.html')

def name(request):
    if request.method == 'POST':
        form = form_user(request.POST)
        if form.save():
            return redirect('data')
        else:
            print(form.errors)
    
    return render(request, 'myapp/name.html')

def home(request):
    if request.POST:
        form = UserDataForm(request.POST)
        form.save()
        return redirect('submit')

    return render(request, 'myapp/home.html')


def submit(request):
    return render(request, 'myapp/submit.html')

def sample(request):
    return render(request, 'myapp/submit.html')


# fetching data from database and populating it in web 
def get_data(request):
    data = form_user_data.objects.all()
    return render (request, 'myapp/display.html', {'data' : data})

# editing the user list 
def edit(request,pk):
    instance_to_edit = form_user_data.objects.get(pk = pk)
    form  = form_user(instance = instance_to_edit)
    return render(request,'myapp/name.html',{'instance_to_edit':instance_to_edit})


# deleting the user list 
def user_delete(request,pk):
    instance_to_delete = form_user_data.objects.get(pk = pk)
    instance_to_delete.delete()
    return redirect('data')


