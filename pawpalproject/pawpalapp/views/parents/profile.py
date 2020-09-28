from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ...models import PawPal, Parent, ParentPawPal

@login_required
def profile(request):
    if request.method == 'GET':
        parent = Parent.objects.get(user_id=request.user.id)
        parent_pawpal_set = list(ParentPawPal.objects.filter(parent_id=request.user.id))
        profile_view = {}
        profile_view['parent'] = parent
        profile_view['parent_pawpals'] = parent_pawpal_set
        
        template_name = 'parents/profile.html'

        context = {
            'profile_view' : profile_view
        }

        return render(request, template_name, context)


@login_required
def profile_edit(request):
    if request.method == "GET":
        user = User.objects.get(id=request.user.id)

        template = 'parents/edit.html'

        context = {
            'user' : user
        }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST
        if ("actual_method" in form_data and form_data['actual_method'] == "PUT"):
            user = User.objects.get(id=int(form_data['id']))
            user.email = form_data['email']
            user.username = form_data['username']
            user.save()

            return redirect(reverse('pawpalapp:profile'))

# **** ADDED DELETE PAWPAL FUNCTIONALITY IN THE EDIT FUNCTION ****

            
# @login_required
# def delete_pawpal(request, pawpal_id):
#     if request.method == "GET":
#         pawpal = PawPal.objects.get(id=pawpal_id)
#         template = 'pawpals/dedpal.html'
#         context = { 'pawpal' : pawpal }

#         return render(request, template, context)

#     if request.method == "POST":
#         form_data = request.POST
#         if ("actual_method" in form_data and form_data['actual_method'] == "DELETE"):
#             PawPal.objects.delete(id=int(form_data['id']))

#             return redirect(reverse('pawpalapp:profile'))