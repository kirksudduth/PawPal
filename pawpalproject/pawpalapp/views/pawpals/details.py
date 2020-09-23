from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ...models import PawPal, ActivityType, Activity, Message

@login_required
def pawpal_details(request, pawpal_id):
    pawpal = PawPal.objects.get(id=pawpal_id)
    activity_types = list(ActivityType.objects.filter(pawpal_id=pawpal_id))
    activities = Activity.objects.filter(pawpal_id=pawpal_id)
    messages = Message.objects.filter(pawpal_id=pawpal_id).order_by('when')
    


    template = 'pawpals/details.html'

    context = {
        'pawpal' : pawpal,
        'activity_types' : activity_types,
        'activities' : activities,
        'messages' : messages,
    }

    return render(request, template, context)