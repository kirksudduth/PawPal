from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ...models import PawPal, Parent, ParentPawPal

@login_required
def delete_pawpal(request):
    if request.method == "GET":
        form_data = request.GET
        pawpal = PawPal.objects.get(id=int(form_data['id']))
        template = 'pawpals/dedpal.html'
        context = { 'pawpal' : pawpal }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST
        if ("actual_method" in form_data and form_data['actual_method'] == "DELETE"):
            PawPal.objects.get(id=int(form_data['id'])).delete()

            return redirect(reverse('pawpalapp:profile'))