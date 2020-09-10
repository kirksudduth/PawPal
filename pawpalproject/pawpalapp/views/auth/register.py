from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from pawpalapp.models import Parent


def register_user(request):

    if request.method == "POST":

        new_user = User.objects.create_user(
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
        )

        authenticated_user = authenticate(
            username=request.POST['username'], password=request.POST['password'])

        if authenticated_user is not None:
            login(request, authenticated_user)

            return redirect(reverse('pawpalapp:home'))

    else:
        template = 'registration/register.html'

    return render(request, template, {})
