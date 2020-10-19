from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import PawPal, ParentPawPal, Parent

@login_required
def find_pawpal(request):
    if request.method == "GET":
        all_pawpals = PawPal.objects.all()

        template = 'pawpals/find.html'
        
        context = {
            'all_pawpals' : all_pawpals
        }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST

        # Was getting a 'Queryset has no attribute 'id' error when 
        # I was trying to get the value of the select option in the form
        # in the templates/parents/profile.html -- found the name attribute
        # of select element is what i needed to use to send the data 
        # i.e. pawpal id to the views/pawpals/find.py 
        # 
        # form_data['pawpal'] instead of form_data['pawpal'][0](??)
        # estaba muy confudido

        pawpal = PawPal.objects.get(id=int(form_data['pawpal']))
        parent = Parent.objects.get(id=request.user.id)
        ParentPawPal.objects.create(
            pawpal=pawpal,
            parent=parent
        )

        # had to change from form_data.id to pawpal.id 
        # here as well

        return redirect(reverse('pawpalapp:pawpal_details', args=[pawpal.id]))