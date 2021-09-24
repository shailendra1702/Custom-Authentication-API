from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Api.models import User


class AccountAdmin(UserAdmin):
    list_display = ('email', 'mobile', 'forget_password',
                    'is_active', 'is_staff')
    search_fields = ('email')
    readonly_fields = ('id',)
