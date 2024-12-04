from django import forms

from CarDealer.locations.models import Location


class LocationBaseForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class LocationCreateForm(LocationBaseForm):
    pass


class LocationUpdateForm(LocationBaseForm):
    pass


class LocationDeleteForm(LocationBaseForm):
    pass
