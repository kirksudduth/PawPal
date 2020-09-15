from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import ActivityType, Activity

@login_required
def activity_type_list(request):
    if request.method == 'GET':
        print("USER:", request.user.id)
        # add pawPal_id=request.user.id ?? in filter.() OR something like that
        all_activity_types = ActivityType.objects.filter()
        all_activities = Activity.objects.filter()
        list_view = {}
        list_view['all_activity_types'] = ActivityType.objects.filter()
        list_view['all_activities'] = Activity.objects.filter()

        template_name = 'activity_types/list.html'

        context = {
            'list_view' : list_view
        }

        return render(request, template_name, context)

    # elif request.method == 'POST':
    #     form_data = request.POST

    #     new_activity_type = ActivityType()