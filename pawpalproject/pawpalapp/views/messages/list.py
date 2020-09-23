from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ...models import Message

@login_required
def message_list(request, pawpal_id):
    messages = Message.objects.filter(pawpal_id=pawpal_id).order_by('when')

    template = 'messages/list.html'

    return render(request, template, {'messages' : messages})