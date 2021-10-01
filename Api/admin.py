from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Api.models import User


class AccountAdmin(UserAdmin):
    list_display = ('email', 'mobile', 'password', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}))
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('id',)
    filter_horizontal = ()


admin.site.register(User, AccountAdmin)
