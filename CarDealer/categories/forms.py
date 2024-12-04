from django import forms
from CarDealer.categories.models import Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateForm(CategoryBaseForm):
    pass


class CategoryEditForm(CategoryBaseForm):
    pass


class CategoryDeleteForm(CategoryBaseForm):
    pass
