from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import PawPal, ParentPawPal, Parent

@login_required
def find_pawpal(request):
    if request.method == "GET":
        all_pawpals = PawPal.objects.all()

        template = 'pawpals/find.html'
        
        context = {
            'all_pawpals' : all_pawpals
        }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST
        pawpal = PawPal.objects.get(id=form_data.id)
        parent = Parent.objects.get(id=request.user.id)
        ParentPawPal.objects.create(
            pawpal=pawpal,
            parent=parent
        )