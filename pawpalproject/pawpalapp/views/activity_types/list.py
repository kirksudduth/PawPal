from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import ActivityType, Activity, ParentPawPal

@login_required
def activity_type_list(request):
    if request.method == 'GET':
        parent_pawpal_set = ParentPawPal.objects.filter(parent_id=request.user.id)
        list_view = {}
        list_view['all_activity_types'] = list(ActivityType.objects.filter(pawpal_id=parent_pawpal_set[0].pawpal_id))
        list_view['all_activities'] = list(Activity.objects.filter(pawpal_id=parent_pawpal_set[0].pawpal_id))
        
        for activity_type in list_view['all_activity_types']:
            list_view[f'{activity_type.title}'] = []
            at_id = activity_type.id
            
            for activity in list_view['all_activities']:
                if activity.activity_type_id == at_id:
                    list_view[f'{activity_type.title}'].append(activity)
                else:
                    None


       

        template_name = 'activity_types/list.html'

        context = {
            'list_view' : list_view
        }

        return render(request, template_name, context)

    # elif request.method == 'POST':
    #     form_data = request.POST

    #     new_activity_type = ActivityType()