from django.shortcuts import render,redirect
from thoughtsapp.forms import CustomUserForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import createpostform
from .forms import User_detailsform


# Create your views here.


def home(request):
    posts=post.objects.all()
    details=User_details()
    image=details.image
    createposts=createpost.objects.all()
    return render(request,'index.html',{"posts":posts,"createposts":createposts,"details":image})


def user_page(request):
    if request.user.is_authenticated:
        details=User_details.objects.all()
        userpost=createpost.objects.filter(user=request.user)
        return render(request,'user.html',{"userpost":userpost,"details":details})
    else:
        return redirect("/")



def create_post(request):
     if request.user.is_authenticated:
        forms=createpostform()
        if request.method=='POST':
            forms=createpostform(data=request.POST, files=request.FILES)
            if forms.is_valid():
                catagory=forms.cleaned_data['catagory']
                title=forms.cleaned_data['title']
                body=forms.cleaned_data['body']
                author=forms.cleaned_data['author']
                images=forms.cleaned_data['images']
                type=forms.cleaned_data['type']
                item=createpost.objects.create(user=request.user, catagory=catagory ,title=title, body=body, author=author, type=type, images=images)
                item.save()
                messages.success(request,"Post created succesfully.")
                return redirect("/")
             
        return render(request,'createpost.html',{"form":forms})



def add_catagory(request):
    if request.method=='POST':
        cat=request.POST['catagory']
        get=Catagory.objects.filter(new_cat=cat)
        if get:
            return redirect("addcatagory")
        else:
            new=Catagory()
            new.new_cat=cat
            new.save()
            messages.success(request,"Catagory added successfully.")
            return redirect("createpost")

    return render(request,'addcatagory.html')
        
def user_details(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=User_detailsform(data=request.POST,files=request.FILES)
            if form.is_valid():
                about=form.cleaned_data['About']
                image=form.cleaned_data['image']
                item=User_details.objects.create(user=request.user,About=about,image=image)
                item.save()
                messages.success(request,"User details added succesfully.")
                return redirect("user_page")
        else:
            form=User_detailsform()
            messages.error(request,"Encountered a error.")
    return render(request,'User_details.html',{'forms':form})



def save_user_Details(request,id):
    if request.user.is_authenticated:
        saved=User_details.objects.all()
        if request.method=='POST' and request.FILES:
            about=request.POST.get('about')
            img=request.FILES['image']
            saved=User_details.objects.get(id=id)
            saved.About=about
            saved.image=img
            saved.user=request.user
            saved.save()
            messages.success(request,"User details  succesfully updated.")
            return redirect("user_page")
    return render(request,'User_update.html',{'saved':saved})      

def update_post(request,id):
    if request.user.is_authenticated:
        up=createpost.objects.filter(id=id)
        if request.method=='POST' and request.FILES:
            c=request.POST.get('catagory')
            t=request.POST.get('title')
            b=request.POST.get('body')
            a=request.POST.get('author')
            i=request.FILES['image']
            ty=request.POST.get('type')
            up=createpost.objects.get(id=id)
            up.title=t
            up.author=a
            up.body=b
            up.images=i
            up.type=ty
            up.user=request.user
            up.save()
            messages.success(request,"Post Updated succesfully.")
            return redirect("user_page")

    return render(request,"update_post.html",{'update':up})
      
    

def delete_post(request,id):
    if request.user.is_authenticated:
        deletepost=createpost.objects.filter(id=id)
        deletepost.delete()
        messages.success(request,"Post deleted succesfully.")
        return redirect("user_page")
    




def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in succesfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid credentials")
                return redirect("/login")
        return render(request,"login.html")




def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out succesfully")
    return redirect("/")




def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User succesfully Registered")
            return redirect('login')
    return render(request,"register.html",{"form":form})