from django.shortcuts import render,redirect

from django.views.generic import View
from user_app.models import User
from user_app.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login


# Create your views here.

class RegisterView(View):

    def get(self,request):

        form = UserRegistrationForm()

        return render(request,"signup.html",{"form":form})
    
    def post(self,request):

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            User.objects.create_user(username = form.cleaned_data.get("username"),
                                     first_name = form.cleaned_data.get("first_name"),
                                     last_name = form.cleaned_data.get("last_name"),
                                       password =form.cleaned_data.get("password"),
                                      email =form.cleaned_data.get("email")
                                    )
        
        form = UserRegistrationForm()
        
        return render(request,"signup.html",{"form":form})
    

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("signup")
        return render(request,"login.html")
    

    

                

        
    
