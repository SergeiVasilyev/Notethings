from django.contrib import admin

from .models import Note, Category, CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_paid')
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        ('Main information', {'fields': ('username', 'password', 'first_name', 'last_name')}),
        ('Contact information', {'fields': ('email', 'last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'is_paid', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        ('Main information', {
            'classes': ('wide', ),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name')}
        ),
        ('Contact information', {'fields': ('email', 'last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'is_paid', 'groups', 'user_permissions')}),
    )
    list_display_links = ('username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'is_paid')
    ordering = ('username',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')