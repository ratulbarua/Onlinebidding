from django.shortcuts import render,redirect
from .models import ContactUs
from django.contrib.auth import authenticate
from django.contrib import messages

def about(request):
    if request.method == "POST":
        contact = ContactUs()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        messages.add_message(request, messages.INFO, 'Query Posted Successfully')
        return redirect('/')
    else:
        contact= ContactUs()
    return render(request, 'about.html', {'form': contact})
