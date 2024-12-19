from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CarDealer.cars.forms import CarCreateForm, CarUpdateForm, CarDeleteForm, TestDriveForm, TestDriveUpdateForm
from CarDealer.cars.models import Cars, TestDrive
from CarDealer.users.decorators import role_required
from django.db.models import Q


@role_required(['Admin'])
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


@role_required(['Admin', 'Staff'])
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


@role_required(['Admin'])
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


@login_required
def book_test_drive(request, car_id):
    car = Cars.objects.get(id_cars=car_id)

    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars_list')  # Ganti dengan URL sesuai dengan nama view Anda
    else:
        form = TestDriveForm()

    context = {
        'form': form,
        'car': car
    }
    
    return render(request, template_name = 'cars/book_test_drive.html', context=context)


@login_required
def test_drive_user(request):
    # Menampilkan daftar test drive yang dipesan oleh pengguna yang sedang login
    test_drives = TestDrive.objects.filter((Q(status='Pending') | Q(status='Confirmed')) & Q(user=request.user.id))
    return render(request, 'cars/test_drive_user.html', {'test_drives': test_drives})


@login_required
def test_drive_list(request):
    # Menampilkan daftar test drive yang dipesan oleh pengguna yang sedang login
    test_drives = TestDrive.objects.filter(Q(status='Pending') | Q(status='Confirmed'))
    return render(request, 'cars/test_drive_list.html', {'test_drives': test_drives})


@login_required
def test_drive_history_user(request):
    # Menampilkan riwayat test drive yang pernah dipesan oleh pengguna
    test_drives = TestDrive.objects.filter((Q(status='Completed') | Q(status='Cancelled')) & Q(user=request.user.id))
    return render(request, 'cars/test_drive_history_user.html', {'test_drives': test_drives})


@login_required
def test_drive_history(request):
    # Menampilkan riwayat test drive yang pernah dipesan oleh pengguna
    test_drives = TestDrive.objects.filter(Q(status='Completed') | Q(status='Cancelled'))
    return render(request, 'cars/test_drive_history.html', {'test_drives': test_drives})


@login_required
def delete_test_drive(request, test_drive_id):
    try:
        test_drive = TestDrive.objects.get(id=test_drive_id)
    except TestDrive.DoesNotExist:
        return JsonResponse({"error": "Test drive tidak ditemukan"}, status=404)

    test_drive.delete()  # Menghapus pemesanan test drive
    return redirect('test_drive_list')  # Redirect kembali ke halaman daftar test drive


@login_required
def cancel_test_drive(request, test_drive_id):
    try:
        test_drive = TestDrive.objects.get(id=test_drive_id)
    except TestDrive.DoesNotExist:
        return JsonResponse({"error": "Test drive tidak ditemukan"}, status=404)

    test_drive.delete()  # Menghapus pemesanan test drive
    return redirect('test_drive_user')  # Redirect kembali ke halaman daftar test drive


@login_required
def edit_test_drive_status(request, test_drive_id):
    test_drive = TestDrive.objects.get(id=test_drive_id)

    if request.method == "POST":
        status = request.POST.get("status")
        test_drive.status = status
        test_drive.save()
        return redirect('test_drive_list')

    context = {
        'test_drive': test_drive
    }

    return render(request, 'cars/edit_test_drive_status.html', context=context)
