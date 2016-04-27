from django.shortcuts import render
from .models import *
from .forms import *

####
from django.contrib.auth import authenticate,login,logout
from hello import settings
from django.contrib.auth.models import User

# Create your views here.

def home(request):

    all_object = blog.objects.all()

    zero_object = all_object[0]
    
    form = BlogPost(request.POST or None) #this is the form

    #save#
    if form.is_valid():
        var = form.save(commit = 'false')
        var.save()
    #save

    template="home.html"
    context = {
    "form": form,
    "all_object": all_object,
    "zero_object": zero_object,
    }
    return render(request, template, context)

