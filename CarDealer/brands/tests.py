# from django.core.exceptions import ValidationError
# from django.test import TestCase
# from CarDealer.brands.models import Brands
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.test import Client
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# class BrandsModelTest(TestCase):
    
#     def test_create_brand(self):
#         """Test creating a brand with valid data."""
#         brand = Brands.objects.create(
#             name="Toyota",
#             year_established=1937
#         )
#         self.assertEqual(brand.name, "Toyota")
#         self.assertEqual(brand.year_established, 1937)

#     def test_unique_name(self):
#         """Test that brand names are unique."""
#         Brands.objects.create(
#             name="Honda",
#             year_established=1948
#         )
        
#         with self.assertRaises(Exception):
#             Brands.objects.create(
#                 name="Honda",  # Duplicate name should raise an error
#                 year_established=1960
#             )
    
#     def test_string_representation(self):
#         """Test the string representation of the Brand."""
#         brand = Brands.objects.create(
#             name="BMW",
#             year_established=1916
#         )
#         self.assertEqual(str(brand), "BMW")

#     def test_year_established_validation(self):
#         """Test that year_established cannot be null."""
#         # Here, we try creating a brand with no year_established (which should fail)
#         with self.assertRaises(ValidationError):
#             brand = Brands(name="Mercedes")  # Missing year_established
#             brand.full_clean()  # This will raise a ValidationError because year_established is required


# class BrandViewsTest(TestCase):

#     def setUp(self):
#         """Setup data for testing."""
#         # Create test users
#         self.admin_user = get_user_model().objects.create_user(
#             username="randi",
#             password="Berani123.",
#             is_staff=True,  # Admin or Staff users should have is_staff=True
#         )

#         self.staff_user = get_user_model().objects.create_user(
#             username="sdf",
#             password="sdfsdf123",
#             is_staff=True
#         )

#         self.regular_user = get_user_model().objects.create_user(
#             username="repa",
#             password="repot123"
#         )

#         # Create test brand
#         self.brand = Brands.objects.create(
#             name="Toyota",
#             year_established=1937
#         )

#     def test_add_brand_view_for_admin(self):
#         # Login sebagai admin
#         self.client.login(username='randi', password='Berani123.')
#         response = self.client.get(reverse('add_brand'))
#         self.assertEqual(response.status_code, 200)  # Admin seharusnya bisa mengakses


#     def test_add_brand_view_for_regular_user(self):
#         """Test that a regular user cannot access the AddBrand view."""
#         self.client.login(username="repa", password="repot123")
#         response = self.client.get(reverse('add_brand'))
#         self.assertEqual(response.status_code, 403)

#     def test_edit_brand_view_for_admin(self):
#         """Test that an admin can access the EditBrand view."""
#         self.client.login(username="randi", password="Berani123.")
#         response = self.client.get(reverse('edit_brand', args=[self.brand.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'brands/edit_brand.html')

#     def test_edit_brand_view_for_regular_user(self):
#         """Test that a regular user cannot access the EditBrand view."""
#         self.client.login(username="repa", password="repot123")
#         response = self.client.get(reverse('edit_brand', args=[self.brand.id]))
#         self.assertEqual(response.status_code, 403)

#     def test_delete_brand_view_for_admin(self):
#         """Test that an admin can access the DeleteBrand view."""
#         self.client.login(username="randi", password="Berani123.")
#         response = self.client.get(reverse('delete_brand', args=[self.brand.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'brands/delete_brand.html')

#     def test_delete_brand_view_for_regular_user(self):
#         """Test that a regular user cannot access the DeleteBrand view."""
#         self.client.login(username="repa", password="repot123")
#         response = self.client.get(reverse('delete_brand', args=[self.brand.id]))
#         self.assertEqual(response.status_code, 403)

#     def test_brand_list_view(self):
#         """Test that the BrandList view returns the correct context."""
#         self.client.login(username="randi", password="Berani123.")
#         response = self.client.get(reverse('brands_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'brands/brands_list.html')
#         self.assertIn('brands', response.context)
#         self.assertEqual(len(response.context['brands']), 1)

#     def test_add_brand_post_valid(self):
#         """Test that a POST request to add a brand works."""
#         self.client.login(username="randi", password="Berani123.")
#         data = {
#             'name': 'Honda',
#             'year_established': 1948
#         }
#         response = self.client.post(reverse('add_brand'), data)
#         self.assertEqual(response.status_code, 302)  # Should redirect
#         self.assertRedirects(response, reverse('brands_list'))
#         self.assertEqual(Brands.objects.count(), 2)

#     def test_add_brand_post_invalid(self):
#         """Test that a POST request with invalid data fails."""
#         self.client.login(username="randi", password="Berani123.")
#         data = {
#             'name': '',  # Invalid because name is required
#             'year_established': 1948
#         }
#         response = self.client.post(reverse('add_brand'), data)
#         self.assertEqual(response.status_code, 200)  # Should return to the same page
#         self.assertFormError(response, 'form', 'name', 'This field is required.')


