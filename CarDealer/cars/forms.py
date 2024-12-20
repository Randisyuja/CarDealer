from django import forms
from CarDealer.cars.models import Cars, TestDrive
from CarDealer.users.models import User


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
        label = {
            'car_image': 'Car Image',
            'cars_name': "Car's name",
            'brand': 'Brand',
            'category': 'Category',
            'warna': 'Warna',
            'tahun': 'Tahun',
            'CC': 'CC',
            'price': 'Price',
            'location': 'Location',
            'description': 'Description'
        }
        widgets = {
            'car_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cars_name': forms.TextInput(attrs={'placeholder': "Enter car's name", 'class':'form-control'}),
            'brand': forms.Select(attrs={'placeholder': "Enter car's brand", 'class':'form-control'}),
            'category': forms.Select(attrs={'placeholder': "Enter car's category", 'class':'form-control'}),
            'warna': forms.TextInput(attrs={'placeholder': "Enter car's color", 'class':'form-control'}),
            'tahun': forms.NumberInput(attrs={'placeholder': "Enter years", 'class':'form-control'}),
            'CC': forms.TextInput(attrs={'placeholder': "Enter CC", 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': "Enter price", 'class':'form-control'}),
            'location': forms.Select(attrs={'placeholder': "Enter car's location", 'class':'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': "Enter car's description", 'class':'form-control'}),
        }


class CarCreateForm(CarBaseForm):
    pass


class CarUpdateForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    widgets = {
            'car_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cars_name': forms.TextInput(attrs={'placeholder': "Enter car's name", 'class':'form-control'}),
            'brand': forms.Select(attrs={'placeholder': "Enter car's brand", 'class':'form-control'}),
            'category': forms.Select(attrs={'placeholder': "Enter car's category", 'class':'form-control'}),
            'warna': forms.TextInput(attrs={'placeholder': "Enter car's color", 'class':'form-control'}),
            'tahun': forms.NumberInput(attrs={'placeholder': "Enter years", 'class':'form-control'}),
            'CC': forms.TextInput(attrs={'placeholder': "Enter CC", 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': "Enter years", 'class':'form-control'}),
            'location': forms.Select(attrs={'placeholder': "Enter car's price", 'class':'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': "Enter car's description", 'class':'form-control'}),
        }


class TestDriveBaseForm(forms.ModelForm):
    class Meta:
        model = TestDrive
        fields = '__all__'
        label = {

        }
        widgets = {
            'car': forms.TextInput(attrs={'placeholder': "Enter car's name", 'class':'form-control', 'readonly': True}),
            'user': forms.TextInput(attrs={'placeholder': "Enter car's name", 'class':'form-control'}),
            'test_drive_date': forms.TextInput(attrs={'type': 'date', 'class':'form-control'}),
            'status': forms.Select(attrs={'placeholder': "Enter years", 'class':'form-control'}),
        }

       
class TestDriveForm(TestDriveBaseForm):
    pass


class TestDriveUpdateForm(TestDriveBaseForm):
    pass
