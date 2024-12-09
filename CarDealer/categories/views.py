from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from CarDealer.categories.forms import CategoryCreateForm, CategoryEditForm, CategoryDeleteForm
from CarDealer.categories.models import Category
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class AddCategory(LoginRequiredMixin, View):
    def get(self, request):
        form = CategoryCreateForm()
        context = {'form': form}
        return render(request, 'categories/add_category.html', context=context)

    def post(self, request):
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        context = {'form': form}
        return render(request, 'categories/add_category.html', context=context)


class EditCategory(LoginRequiredMixin, View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryEditForm(instance=category)
        context = {'form': form}
        return render(request, 'categories/edit_category.html', context=context)

    def post(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryEditForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        context = {
            'form': form,
            'category': category
            }
        return render(request, 'categories/edit_category.html', context=context)


class DeleteCategory(LoginRequiredMixin, View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryDeleteForm(instance=category)
        context = {'form': form}
        return render(request, 'categories/delete_category.html', context=context)

    def post(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryDeleteForm(request.POST, instance=category)
        if form.is_valid():
            category.delete()
            return redirect('category_list')
        context = {
            'form': form,
            'category': category
            }
        return render(request, 'categories/delete_category.html', context=context)



class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'  # Nama template yang akan digunakan
    context_object_name = 'categories'
