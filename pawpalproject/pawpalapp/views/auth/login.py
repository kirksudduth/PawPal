from django.shortcuts import render


def login(request):
    if request.method == 'GET':
        template = 'registration/login.html'
        context = {}

        return render(request, template, context)