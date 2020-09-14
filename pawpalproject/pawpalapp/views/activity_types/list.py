from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import ActivityType

@login_required
def activity_type_list(request):
    if request.method == 'GET':

        all_activity_types = ActivityType.objects.all()
        
        template_name = 'activity_types/list.html'

        context = {
            'all_activity_types': all_activity_types
        }

        return render(request, template_name, context)

    # elif request.method == 'POST':
    #     form_data = request.POST

    #     new_activity_type = ActivityType()