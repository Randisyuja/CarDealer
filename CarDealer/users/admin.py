from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from CarDealer.users.models import User
from CarDealer.users.choices import RoleChoice
from django.core.exceptions import PermissionDenied


class UsersAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Role & Permissions', {'fields': ('role', 'is_staff', 'is_superuser', 'is_active', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'groups'),
        }),
    )
    

    # Fields displayed in the user list
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'role']
    ordering = ['username']

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        if obj:
            return [
                (None, {'fields': ('username', 'password')}),
                ('Personal info', {'fields': ('email',)}),
                ('Role & Permissions', {'fields': ('is_active',)}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            ]
        else:
            return [
                (None, {'fields': ('username', 'password1', 'password2', 'email')}),
                ('Role & Permissions', {'fields': ('role',)}),
            ]

    def save_model(self, request, obj, form, change):
        if 'role' in form.changed_data and not request.user.is_superuser:
            raise PermissionError("You are not allowed to modify user roles.")
        super().save_model(request, obj, form, change)


    def get_readonly_fields(self, request, obj=None):
        # Hanya superuser yang bisa mengedit role
        if not request.user.is_superuser:
            return ['role']
        return []


    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False  # Pengguna biasa tidak bisa mengubah superuser
        return super().has_change_permission(request, obj)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(is_superuser=False)


# Register the customized UserAdmin
admin.site.register(User, UsersAdmin)
