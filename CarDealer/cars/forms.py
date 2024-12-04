from django import forms
from CarDealer.cars.models import Cars


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass


class CarUpdateForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    pass
