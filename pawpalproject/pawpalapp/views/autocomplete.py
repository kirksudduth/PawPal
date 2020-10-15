from django.shortcuts import render
from models import AutoComplete

def auto_search(request):
    result = AutoComplete.objects.all()
    return render(request, 'parents/profile.html', {"autocomplete":result})