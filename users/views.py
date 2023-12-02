from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from .forms import ProfileForm
from django.contrib import messages
from .models import Profile
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect


def index(request):
    return render(request, 'users/base.html')



def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'users/login.html')   
    return render(request, "users/register.html")


def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'users/login.html')   
    return render(request, "users/login.html")

def Logout(request):
    logout(request)
    return redirect('/login/')  

def crete_profile(request, id):
    if request.method =='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            u_model = Profile.objects.get_or_create(id=id)
            profile.user = u_model.user
            profile.save()
            messages.success(request, f"Profile Created for {profile.user}")
            return redirect(f'/profile/{request.user.id}')
        else:
            print("form errors", form.errors)
    
    form = ProfileForm()
    return render(request,'users/add_profile.html',{'form': form})

def profile_update(request, id):
    profile = get_object_or_404(Profile, id=id)
    form = ProfileForm(instance=profile)
    if request.method =='POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully!")
            return redirect(f'/profile/{request.user.id}')
    context={"form":form}
    return render(request,'users/update_profile.html',context) 

def profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    if profile:
        return render(request,'users/profile.html',{'dat': profile})
    
        
    else:
        return HttpResponseRedirect('/')
        


    


