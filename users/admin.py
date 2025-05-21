from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'mobile', 'country', 'avatar', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'mobile', 'country')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)
