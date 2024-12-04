from django.shortcuts import render, redirect, get_object_or_404
from CarDealer.categories.forms import CategoryCreateForm, CategoryEditForm, CategoryDeleteForm
from CarDealer.categories.models import Category


def add_category(request):
    if request.method == 'GET':
        form = CategoryCreateForm
    else:
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('category_list')

    context = {'form': form}

    return render(request, template_name='categories/add_category.html', context=context)


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = CategoryEditForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Ganti dengan URL yang sesuai
    else:
        form = CategoryEditForm(instance=category)

    context = {
        'form': form,
        'category': category
    }

    return render(request, 'categories/edit_category.html', context=context)


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = CategoryDeleteForm(request.POST, instance=category)

        if form.is_valid():
            category.delete()

            return redirect('category_list')

    else:
        form = CategoryDeleteForm(instance=category)

    context = {
        'form': form,
        'category': category
    }

    return render(request, 'categories/delete_category.html', context=context)


# views.py
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})
