from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import PawPal, ParentPawPal, Parent

@login_required
def pawpal_list(request):
    if request.method == "GET" and len(ParentPawPal.objects.filter(parent_id=request.user.id)) > 0:
        parent = Parent.objects.get(user_id=request.user.id)
        parent_pawpal_list = list(ParentPawPal.objects.filter(parent_id=parent.id))

        template = 'pawpals/list.html'

        context = {
            'parent_pawpal_list' : parent_pawpal_list,
        }

        return render(request, template, context)

    if request.method == "GET" and len(ParentPawPal.objects.filter(parent_id=request.user.id)) == 0:
        all_pawpals = PawPal.objects.all()

        template = 'pawpals/list.html'

        context = {
            'all_pawpals' : all_pawpals,
            'my_pawpals' : None
        }

        return render(request, template, context)