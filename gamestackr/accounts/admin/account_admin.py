from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from gamestackr.accounts.models import Account


class AccountAdmin(UserAdmin):
    model = Account
    list_display = (
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
        'last_login',
        'date_joined',
    )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Avatar'), {'fields': ['image']}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions')
        }
    ),)
    ordering = ('email',)


admin.site.register(Account, AccountAdmin)
