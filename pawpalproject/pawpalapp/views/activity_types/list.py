from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import ActivityType, Activity, ParentPawPal

@login_required
def activity_type_list(request):
    if request.method == 'GET':
        parent_pawpal_set = ParentPawPal.objects.filter(parent_id=request.user.id)
        list_view = {}
        list_view['all_activity_types'] = ActivityType.objects.filter(pawpal_id=parent_pawpal_set[0].pawpal_id)
        list_view['all_activities'] = Activity.objects.filter(pawpal_id=parent_pawpal_set[0].pawpal_id)

        # for pp in parent_pawpal_set:
        #     list_view['all_activity_types_{pp.pawpal.name}'] = ActivityType.objects.filter(pawpal_id=parent_pawpal_set[0].pawpal_id)
        #     list_view['all_activities_{pp.pawpal.name}'] = Activity.objects.filter(pawpal_id=parent_pawpal_set[0].pawpal_id)

        template_name = 'activity_types/list.html'

        context = {
            'list_view' : list_view
        }

        return render(request, template_name, context)

    # elif request.method == 'POST':
    #     form_data = request.POST

    #     new_activity_type = ActivityType()