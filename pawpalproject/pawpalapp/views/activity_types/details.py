from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from ...models import ActivityType, Activity, ParentPawPal, PawPal

@login_required
def activity_type_details(request, activity_type_id):
    if request.method == 'GET':
        
        parent_pawpals = list(ParentPawPal.objects.filter(parent_id=request.user.id))
        
        activity_type = ActivityType.objects.get(id=activity_type_id)
        activities = list(Activity.objects.filter(activity_type_id=activity_type.id))
        pawpal = PawPal.objects.get(id=activity_type.pawpal_id)

        template = 'activity_types/detail.html'
        context = {
            'activity_type': activity_type,
            'activities' : activities,
            'pawpal' : pawpal
        }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST
        print("DATA:", form_data)
        if (
            "actual_method" in form_data and form_data['actual_method'] == "DELETE"
        ):
            Activity.objects.get(id=int(form_data['id'])).delete()
        
            return redirect(reverse('pawpalapp:activity_type_details', args=[activity_type_id]))

        if (
            "actual_method" in form_data and form_data['actual_method'] == "PUT"
        ):
            activity = Activity.objects.get(id=int(form_data['id']))
            activity.note = form_data['note']
            activity.save()

            return redirect(reverse('pawpalapp:activity_type_details', args=[activity_type_id]))
