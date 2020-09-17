from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from ...models import ActivityType, Activity, ParentPawPal, PawPal

@login_required
def activity_type_details(request, activity_type_id):
    if request.method == 'GET':
        
        parent_pawpals = list(ParentPawPal.objects.filter(parent_id=request.user.id))
        
        activity_type = ActivityType.objects.get(id=activity_type_id, pawpal_id=parent_pawpals[0].pawpal_id)
        activities = list(Activity.objects.filter(activity_type_id=activity_type.id))
        pawpal = PawPal.objects.get(id=parent_pawpals[0].pawpal_id)
        print("AT:", activity_type.id)

        template = 'activity_types/detail.html'
        context = {
            'activity_type': activity_type,
            'activities' : activities,
            'pawpal' : pawpal
        }

        return render(request, template, context)
