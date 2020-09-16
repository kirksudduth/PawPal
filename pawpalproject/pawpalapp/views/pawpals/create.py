from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ...forms.pawpal.add_form import AddPawPalForm
from ...models import PawPal, ParentPawPal, Parent

@csrf_exempt
def create_pawpal(request):

    if request.method == "POST":
        form = AddPawPalForm(request.POST)
        if form.is_valid():
            form.save()
            created_pawpal = PawPal.objects.all().last()
            parent = Parent.objects.get(user_id=request.user.id)
            ParentPawPal.objects.create(pawpal=created_pawpal, parent=parent)
            return redirect("/")
    else:
        form = AddPawPalForm()

        return render(request, "pawpals/add.html", {"form": form})