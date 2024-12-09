from django import forms

from CarDealer.brands.models import Brands


class BrandBaseForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = '__all__'
        label = {
            'name': "Brand's name",
            'year_established': "Year Established",
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter brand's name", 'class': 'form-control'}),
            'year_established': forms.NumberInput(attrs={'placeholder': "Enter Year", 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': "Enter brand's name", 'class': 'form-control'}),
        }


class BrandCreateForm(BrandBaseForm):
    pass


class BrandUpdateForm(BrandBaseForm):
    pass


class BrandDeleteForm(BrandBaseForm):
    pass
