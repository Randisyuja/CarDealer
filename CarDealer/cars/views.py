from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CarDealer.cars.forms import CarCreateForm, CarUpdateForm, CarDeleteForm
from CarDealer.cars.models import Cars


@login_required()
def add_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('cars_list')

    context = {
        'form': form,
    }

    return render(request, template_name='cars/add_car.html', context=context)


@login_required()
def edit_car(request, car_id):
    car = Cars.objects.get(id_cars=car_id)

    if request.method == 'GET':
        form = CarUpdateForm(instance=car)
    else:
        form = CarUpdateForm(request.POST, instance=car)

        if form.is_valid():
            form.save()

            return redirect('cars_list')

    context = {
        'form': form,
        'car': car
    }

    return render(request, template_name='cars/edit_car.html', context=context)


@login_required()
def delete_car(request, car_id):
    car = Cars.objects.get(id_cars=car_id)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)

        if form.is_valid():
            car.delete()

            return redirect('cars_list')

    context = {
        'form': form,
        'car': car
    }

    return render(request, template_name='cars/delete_car.html', context=context)


@login_required()
def cars_list(request):
    cars = Cars.objects.all()
    return render(request, template_name='cars/cars_list.html', context={'cars': cars})


@login_required()
def car_detail(request, car_id):
    car = Cars.objects.get(id_cars=car_id)

    context = {
        'car': car,
    }

    return render(request, template_name='cars/car_detail.html', context=context)
    
