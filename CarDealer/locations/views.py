from django.shortcuts import render, redirect
from CarDealer.locations.forms import LocationCreateForm, LocationDeleteForm, LocationUpdateForm
from CarDealer.locations.models import Location
from django.contrib.auth.decorators import login_required
from CarDealer.users.decorators import role_required


@role_required(['Admin'])
@login_required()
def add_location(request):
    if request.method == 'GET':
        form = LocationCreateForm
    else:
        form = LocationCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('locations_list')

    context = {
        'form': form
    }

    return render(request, template_name='locations/add_location.html', context=context)


@login_required()
def locations_list(request):
    locations = Location.objects.all()
    return render(request, template_name='locations/locations_list.html', context={'locations': locations})


@role_required(['Admin', 'Staff'])
@login_required()
def edit_location(request, location_id):
    location = Location.objects.get(id=location_id)

    if request.method == 'GET':
        form = LocationUpdateForm(instance=location)
    else:
        form = LocationUpdateForm(request.POST, instance=location)

        if form.is_valid():
            form.save()

            return redirect('locations_list')

    context = {
        'form': form,
        'location': location
    }

    return render(request, template_name='locations/edit_location.html', context=context)


@role_required(['Admin'])
@login_required()
def delete_location(request, location_id):
    location = Location.objects.get(id=location_id)
    if request.method == 'GET':
        form = LocationDeleteForm(instance=location)
    else:
        form = LocationDeleteForm(request.POST, instance=location)

        if form.is_valid():
            location.delete()

            return redirect('locations_list')

    context = {
        'form': form
    }

    return render(request, template_name='locations/delete_location.html', context=context)
