from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse 

def post(request):
   if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        title = request.POST.get('title')
        image = request.POST.get('image')
        image2 = request.POST.get('image2')
        image3 = request.POST.get('image3')
        description = request.POST.get('description')
        price = request.POST.get('price')
        form.title = title
        form.image = image
        form.image2 = image2
        form.image3 = image3
        form.description = description
        form.price = price
        if form.is_valid():
           form.save()
           messages.add_message(request, messages.INFO, 'Posted Successfully /n Wait for Confirmation')
           return render(request, 'post/post.html', {'form':form})
        else:
            form = PostForm()
   else:
        return render(request,'post/post.html')