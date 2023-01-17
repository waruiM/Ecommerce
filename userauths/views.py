from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
#import the user model directly from models
from userauths.models import User


#creating the variable 

# Create your views here.
def register_view(request):
    if request.method=="POST":

        form= UserRegisterForm(request.POST or None)

        #check if data is valid/contains no maliscious data
        if form.is_valid():
            new_user=form.save()
            username= form.cleaned_data.get("username")
            messages.success(request,f"Welcome {username}, your account has been generated succesfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
     
            login(request,new_user)
            return redirect("core:index")
    else:
       
        form= UserRegisterForm()

    context= {
        #name provided for the user register form above 
        'form': form
    }
    return render(request,"userauths/sign-up.html",context)


##login
def login_view(request):
    #check if user is loged in
    if request.user.is_authenticated:

       return redirect("core:index")
        # context={

        # }
        
        # return render(request,"core:index",context)


    #check if the details provided are in the database
    if request.method == "POST":
        #check if the email in the form matches to the email existing to the database
        email= request.POST.get("email")
        password= request.POST.get("password")

        try:
            #get email from the database that matches the one provided
            user=User.objects.get(email = email)
            user = authenticate(request, email=email , password=password)
            #log in messages
            if user is not None:
                login(request,user)
                messages.success(request, "You have logged in successfully")
                return redirect("core:index")
            else:
                messages.warning(request, "User does not exist")

        except:
            messages.warning(request,f"User with email {email} does not exist")

        
            #provide the template for sign-in 

    
    return render(request,"userauths/sign-in.html")
    
def logout_view(request):
    logout(request)
    messages.success(request,"logout succeful")
    return redirect("userauths:sign-in")
