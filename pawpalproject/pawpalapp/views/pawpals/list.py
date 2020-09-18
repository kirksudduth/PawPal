from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import PawPal, Parent, ParentPawPal

@login_required
def pawpal_list(request):
    if request.method == "GET":
        all_pawpals = PawPal.objects.filter(parent_id=request.user.id)
