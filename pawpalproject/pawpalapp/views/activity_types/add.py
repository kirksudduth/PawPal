from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import ActivityType, Activity, ParentPawPal, PawPal

@login_required
def add_activity_type(request, pawpal_id):
    if request.method == "GET":

        template = "activity_types/add.html"

        return render(request, template, {})
# ADDS ACTIVITY TYPE TO THE LIST FOR ADDING ACTIVITIES
    if request.method == "POST":
        form_data = request.POST
        pawpal = PawPal.objects.get(id=pawpal_id)
        activity_type = ActivityType.objects.create(title=form_data['title'], pawpal=pawpal)
        

        return redirect('/')