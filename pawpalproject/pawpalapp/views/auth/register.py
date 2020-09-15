from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ...forms.registration.form import RegisterForm

@csrf_exempt
def register(request):
    print("REQUEST:", request)

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            
            login(request, authenticated_user)

            return redirect("/")

    else:
        form = RegisterForm()
        print("FORM:", form)

        return render(request, "registration/register.html", {"form": form})

    #     new_user = User.objects.create_user(
    #         username=request.POST['username'],
    #         email=request.POST['email'],
    #         password=request.POST['password'],
    #         first_name=request.POST['first_name'],
    #         last_name=request.POST['last_name']
    #     )
        

    #     authenticated_user = authenticate(
    #         username=request.POST['username'], password=request.POST['password'])

    #     if authenticated_user is not None:
    #         # token = Token.objects.get(user=authenticated_user)
    #         # data = json.dumps({"valid": True, "token": token.key})
    #         print("REQUEST:", request)
    #         login(request, authenticated_user)
    #         return HttpResponse(data, content_type='application/json')

    #         return redirect(reverse('pawpalapp:home'))

    # else:
    #     template = 'registration/register.html'

    # return render(request, template, {})

