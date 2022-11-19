from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import Employee_database, Language
from django.contrib.auth.decorators import login_required


# CRUD- OPERATIONS START
@login_required(login_url='login')
def home(request):
    obj= Employee_database.objects.all()
    context= {'alldata':obj}
    return render(request, 'employee_app/home.html', context)

@login_required(login_url='login')
def add_new(request):
    if request.method== 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        employee_id= request.POST.get('employee_id')
        designation= request.POST.get('designation')
        langauge= request.POST.get('langauge')
        l_name= Language.objects.get(id= langauge)
        data= Employee_database.objects.create(name= name,email= email, employee_id= employee_id, designation= designation,lang= l_name)
        data.save()
        #messages.success(request, 'RECORD CREATED SUCCESSFULLY.')
        return redirect('home')
    return render(request, 'employee_app/new_record.html')

@login_required(login_url='login')
def update_record(request, pk):
    obj= Employee_database.objects.get(id=pk)
    context= {'emp':obj}
    if request.method== 'POST':
        obj= Employee_database.objects.filter(id=pk)
        name= request.POST.get('name')
        email= request.POST.get('email')
        employee_id= request.POST.get('employee_id')
        designation= request.POST.get('designation')
        result= obj.update(id=pk, name= name,email= email, employee_id= employee_id, designation= designation)
        return redirect('home')
    return render(request, 'employee_app/update.html', context)

@login_required(login_url='login')
def delete_record(request, pk):
    data= Employee_database.objects.get(id=pk)
    data.delete()
    return redirect('home')
# CRUD- OPERATIONS END

def user_login(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.success(request, 'USER ALREADY EXISTS.')
            return redirect('login')

        user_obj= authenticate(username= username, password= password)

        if user_obj:
            login(request, user_obj)
            return redirect('home')
        #messages.error(request, 'INVALID PASSWORD.')

    return render(request, 'employee_app/login.html')


def register(request):
    if request.method=='POST':
        username= request.POST.get('username')
        name= request.POST.get('name')
        password= request.POST.get('password')

        if User.objects.filter(username=username).exists():
            #messages.success(request, 'USER ALREADY EXISTS.')
            return redirect('login')
        user_obj= User.objects.create( username=username, first_name=name)
        user_obj.set_password(password)
        user_obj.save()
        return redirect('login')
        #messages.success(request, 'RECORD CREATED SUCCESSFULLY.')

    return render(request, 'employee_app/register.html')

def logout_page(request):
    logout(request)
    return redirect('login')