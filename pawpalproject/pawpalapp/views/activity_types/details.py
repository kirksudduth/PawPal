from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from ...models import ActivityType, Activity

@login_required
def activity_type_details(request, activity_type_id):
    if request.method == 'GET':
        
        
        activity_type = ActivityType.objects.get(id=activity_type_id)
        pawpal = activity_type.pawpal

        template = 'activity_types/detail.html'
        
        context = {
            'activity_type': activity_type,
            'pawpal' : pawpal
        }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST
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
