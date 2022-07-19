from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserForm,RestourantForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return redirect(restourant_home)
@login_required(login_url=('/restourant/sign_in/'))
def restourant_home(request):
    return render(request,'restourant/home.html',{})
def restourant_sign_up(request):
    user_form=UserForm()
    restourant_form=RestourantForm()
    if request.method=="POST":
        user_form=UserForm(request.POST)
        restourant_form=RestourantForm(request.POST,request.FILES)
        if user_form.is_valid() and restourant_form.is_valid():
            new_user=User.objects.create_user(**user_form.cleaned_data)
            new_restourant=restourant_form.save(commit=False)
            new_restourant.user=new_user
            new_restourant.save()
            login(request,authenticate(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"]
            ))
            return redirect(restourant_home)

                
    return render(request,'restourant/sign_up.html',{
        "user_form":user_form,
        "restourant_form":restourant_form
    })
