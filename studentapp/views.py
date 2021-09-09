from django.shortcuts import render

# Create your views here.
from . models import *
from . forms import *
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import CreateUserForm


def HomeView(request):
    return render(request, 'studentapp/home.html')


def AboutView(request):
    return render(request, 'studentapp/about.html')


def WelcomeView(request):
    return render(request, 'studentapp/welcome.html')


def ContactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully !')
        return redirect('contact')
    context = {'form': form}
    return render(request, 'studentapp/contact.html', context)


def StudentregistrationView(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your registration has been done successfully !')
        return redirect('studentregistration')
    context = {'form': form}
    return render(request, 'studentapp/studentregistration.html', context)


def StudentdetailView(request):
    s = Student.objects.all()
    context = {'data': s}
    return render(request, 'studentapp/studentdetail.html', context)


@login_required(login_url='login')
def UpdateView(request, id):
    data = get_object_or_404(Student, id=id)
    form = StudentForm(instance=data)
    if (request.method == 'POST'):
        form = StudentForm(request.POST, request.FILES, instance=data,)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your detail has been updated successfully !')
        return redirect("studentdetail")
    context = {'form': form}
    return render(request, "studentapp/update.html", context)


@login_required(login_url='login')
def DeleteView(request, id):
    data = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        data.delete()
        messages.success(
            request, 'Your record has been deleted successfully !')
        return redirect('studentdetail')
    context = {}
    return render(request, "studentapp/delete.html", context)


def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'studentapp/register.html', context)


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                messages.info(request, 'Username or Password is Incorrect')

        context = {}
        return render(request, 'studentapp/login.html', context)


def LogoutView(request):
    logout(request)
    return redirect('login')
