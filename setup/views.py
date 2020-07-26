from datetime import date
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from .models import UserInfo
from .forms import Register,UserInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django import template
from django.contrib import messages
from .models import UserInfo, User
from django.core.exceptions import ValidationError

from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
def index(request):

    return render(request, 'setup/template/index.html', {})
    # return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'setup/template/index.html')
    # return HttpResponseRedirect(reverse('setup/template/index.html'))
def user_profile(request):
    # user = request.user
    # profile = UserInfo.objects.filter(id = id)
    # user_details = UserInfo.objects.get(user = request.user)

    return render(request, 'setup/template/profile.html', {})




def feed(request):
    data = UserInfo.objects.all()

    return render(request, 'setup/template/feed.html', {'data':data})
    # return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    user_details = Register()
    # bio_details = UserInfoForm()
    if request.method == 'POST':
        user_details = Register(request.POST)
        # bio_details = UserInfoForm(request.POST)
        if user_details.is_valid():
            user_instance = user_details.save()
            user_instance.set_password(user_instance.password)
            user_instance.save()
            registered = True
            messages.success(request, f'Account created for {user_instance.username}')

            return  redirect('/user_login/')

        else:
            print(user_details.errors)

    return render(request,'setup/template/register.html',
                  {'user_details':user_details})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request, 'setup/template/index.html')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'setup/template/login.html', {})


def post(request):

    user_profile = UserInfoForm()
    if request.method == 'POST':
        user_profile = UserInfoForm(request.POST)
        # file_obj = request.FILES['myfile']
        if user_profile.is_valid():
            instance = user_profile.save(commit=False)
            instance.user = request.user
            instance.save()
            # profile = UserInfo()
            # profile.image = UserInfoForm.cleaned_data["image"]
            # print((request.POST))
            # profile.save()
            # fs = FileSystemStorage()
            # fs.save(file_obj.name, file_obj)
            # user_profile.save()
            print("hi")
            return redirect('/post/')
        else:
            return HttpResponse("sth wrong")
    return render(request, 'setup/template/index.html', {'user_profile': user_profile})
def edit_profile(request):
    current_user = request.user
    user_object = get_object_or_404(User, id=current_user.id)
    if request.method == 'POST':
        form =  Register(
            request.POST, instance=user_object
        )
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            user_instance = form.save()
            user_instance.set_password(user_instance.password)
            user_instance.save()
        return HttpResponseRedirect("/user_login/")
    else:
        form = Register()

    return render(request,'setup/template/editprofile.html', {'form': form})

def delete_profile(request):
    current_user = request.user
    user_object = get_object_or_404(User, id=current_user.id)
    user_object.delete()
    return HttpResponseRedirect("/register/")

