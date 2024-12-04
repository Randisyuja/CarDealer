from django.shortcuts import render, redirect, get_object_or_404
from CarDealer.users.forms import UserRegistrationForm, UserEditForm, UserDeleteForm
from CarDealer.users.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_list')  # Ganti dengan URL yang sesuai
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Ganti dengan URL yang sesuai
    else:
        form = UserEditForm(instance=user)

    return render(request, 'users/edit_user.html', {'form': form, 'user': user})


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'GET':
        form = UserDeleteForm(instance=user)
    else:
        form = UserDeleteForm(request.POST, instance=user)

        if form.is_valid():
            user.delete()

            return redirect('user_list')

    context = {
        'form': form,
        'user': user
    }

    return render(request, template_name='users/delete_user.html', context=context)
