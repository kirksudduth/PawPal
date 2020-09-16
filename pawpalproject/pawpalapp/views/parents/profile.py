from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ...models import PawPal, Parent, ParentPawPal

@login_required
def profile(request):
    if request.method == 'GET':
        parent = Parent.objects.get(user_id=request.user.id)
        parent_pawpal_set = list(ParentPawPal.objects.filter(parent_id=request.user.id))
        print("PAWPALS:", parent_pawpal_set)
        profile_view = {}
        profile_view['parent'] = parent
        profile_view['parent_pawpals'] = parent_pawpal_set
        
        template_name = 'parents/profile.html'

        context = {
            'profile_view' : profile_view
        }

        return render(request, template_name, context)


@login_required
def profile_edit(request):
    if request.method == "GET":
        user = User.objects.get(id=request.user.id)

        template = 'parents/edit.html'

        context = {
            'user' : user
        }

        return render(request, template, context)