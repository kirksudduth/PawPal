from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ...models import *

@csrf_exempt
def create_activity(request, activity_type_id):

    if request.method == "POST":
        form_data = request.POST
        activity_type = ActivityType.objects.get(id=activity_type_id)
        parent = Parent.objects.get(id=request.user.id)
        parent_pawpal = ParentPawPal.objects.filter(parent_id=request.user.id)
        pawpal = PawPal.objects.get(id=parent_pawpal[0].pawpal_id)
        new_activity = Activity.objects.create(
            activity_type_id = activity_type_id,
            note = form_data['note'],
            parent_id = parent.id,
            pawpal_id = pawpal.id
        )

        return redirect("/")
    else:
        form = AddActivityForm()
        parent_pawpal = ParentPawPal.objects.filter(parent_id=request.user.id)
        pawpal = PawPal.objects.get(id=parent_pawpal[0].pawpal_id)
        activity_type = ActivityType.objects.get(id=activity_type_id)



        return render(request, "activities/form.html", {'pawpal' : pawpal, 'activity_type' : activity_type})
