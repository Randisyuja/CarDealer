from django import forms

from CarDealer.brands.models import Brands


class BrandsBaseForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = '__all__'


class BrandsCreateForm(BrandsBaseForm):
    pass


class BrandsUpdateForm(BrandsBaseForm):
    pass


class BrandsDeleteForm(BrandsBaseForm):
    pass
