from django.shortcuts import render, redirect
from CarDealer.brands.forms import BrandsCreateForm, BrandsUpdateForm, BrandsDeleteForm
from CarDealer.brands.models import Brands


def add_brand(request):
    if request.method == 'GET':
        form = BrandsCreateForm()
    else:
        form = BrandsCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('brands_list')

    context = {
        'form': form
    }

    return render(request, template_name='brands/add_brand.html', context=context)


def brands_list(request):
    brands = Brands.objects.all()
    return render(request, template_name='brands/brands_list.html', context={'brands': brands})


def edit_brand(request, brand_id):
    brand = Brands.objects.get(pk=brand_id)
    if request.method == 'GET':
        form = BrandsUpdateForm(instance=brand)
    else:
        form = BrandsUpdateForm(request.POST, instance=brand)

        if form.is_valid():
            form.save()

            return redirect('brands_list')

    context = {
        'form': form,
        'brand': brand
    }

    return render(request, template_name='brands/edit_brand.html', context=context)


def delete_brand(request, brand_id):
    brand = Brands.objects.get(pk=brand_id)

    if request.method == 'GET':
        form = BrandsDeleteForm(instance=brand)
    else:
        form = BrandsDeleteForm(request.POST, instance=brand)

        if form.is_valid():
            brand.delete()

            return redirect('brands_list')

    context = {
        'form': form,
        'brand': brand
    }

    return render(request, template_name='brands/delete_brand.html', context=context)
