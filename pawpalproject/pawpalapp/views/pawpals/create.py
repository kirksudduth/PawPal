from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ...models import PawPal, ParentPawPal, Parent, ActivityType
from ...forms.pawpal.add_form import AddPawPalForm


@csrf_exempt
def create_pawpal(request):

    if request.method == "POST":
        form = AddPawPalForm(request.POST)
        if form.is_valid():
            form.save()
            created_pawpal = PawPal.objects.all().last()
            print("PAWPAL:", created_pawpal.image)
            ActivityType.objects.create(title="Feed", pawpal=created_pawpal)
            ActivityType.objects.create(title="Out", pawpal=created_pawpal)
            ActivityType.objects.create(title="Walk", pawpal=created_pawpal)
            ActivityType.objects.create(title="Wash", pawpal=created_pawpal)
            ActivityType.objects.create(title="Meds", pawpal=created_pawpal)
            ActivityType.objects.create(
                title="Miscellaneous", pawpal=created_pawpal)
            parent = Parent.objects.get(user_id=request.user.id)
            ParentPawPal.objects.create(pawpal=created_pawpal, parent=parent)
            return redirect("/")

        # this "else" returns the user to the page with the form filled out minus the field
        # where there was an error in the input
        else:
            return render(request, "pawpals/add.html", {'form': form})
    else:
        form = AddPawPalForm()

        return render(request, "pawpals/add.html", {"form": form})
