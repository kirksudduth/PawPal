from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ...forms.registration.form import RegisterForm

@csrf_exempt
def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            
            login(request, authenticated_user)

            return redirect("/")

    else:
        form = RegisterForm()
        context = {
            'form' : form
        }

        return render(request, "registration/register.html", context)
