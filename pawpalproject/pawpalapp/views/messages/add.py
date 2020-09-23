from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ...models import Message, Parent, PawPal

@login_required
def add_message(request, pawpal_id):
    if request.method == "GET":

        template = "messages/add.html"

        return render(request, template, {'pawpal' : pawpal_id})

    if request.method == "POST":
        form_data = request.POST
        body = form_data['message']
        parent = Parent.objects.get(id=request.user.id)
        pawpal = PawPal.objects.get(id=pawpal_id)
        Message.objects.create(body=body, parent=parent, pawpal=pawpal)

        return redirect(reverse('pawpalapp:pawpal_details', args=[pawpal_id]))