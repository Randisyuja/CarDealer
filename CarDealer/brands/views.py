from django.shortcuts import render, redirect, get_object_or_404
from CarDealer.brands.forms import BrandCreateForm, BrandUpdateForm, BrandDeleteForm
from CarDealer.brands.models import Brands
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from CarDealer.users.decorators import role_required


class AddBrand(LoginRequiredMixin, View):
    @method_decorator(role_required(['Admin', 'Staff']))
    def get(self, request):
        form = BrandCreateForm()
        context = {'form': form}
        return render(request, 'brands/add_brand.html', context=context)

    def post(self, request):
        form = BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brands_list')
        context = {'form': form}
        return render(request, 'brands/add_brand.html', context=context)


class EditBrand(LoginRequiredMixin, View):
    @method_decorator(role_required(['Admin', 'Staff']))
    def get(self, request, brand_id):
        brand = get_object_or_404(Brands, id=brand_id)
        form = BrandUpdateForm(instance=brand)
        context = {'form': form}
        return render(request, 'brands/edit_brand.html', context=context)

    def post(self, request, brand_id):
        brand = get_object_or_404(Brands, id=brand_id)
        form = BrandUpdateForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brands_list')
        context = {
            'form': form,
            'brand': brand
            }
        return render(request, 'brands/edit_brand.html', context=context)


class DeleteBrand(LoginRequiredMixin, View):
    @method_decorator(role_required(['Admin', 'Staff']))
    def get(self, request, brand_id):
        brand = get_object_or_404(Brands, id=brand_id)
        form = BrandDeleteForm(instance=brand)
        context = {'form': form}
        return render(request, 'brands/delete_brand.html', context=context)

    def post(self, request, brand_id):
        brand = get_object_or_404(Brands, id=brand_id)
        form = BrandDeleteForm(request.POST, instance=brand)
        if form.is_valid():
            brand.delete()
            return redirect('brands_list')
        context = {
            'form': form,
            'brand': brand
            }
        return render(request, 'brands/delete_brand.html', context=context)



class BrandList(LoginRequiredMixin, ListView):
    model = Brands
    template_name = 'brand_list.html'  # Nama template yang akan digunakan
    context_object_name = 'brands'
