from django.contrib import admin

from gamestackr.accounts.models import AccountSetting


class AccountSettingAdmin(admin.ModelAdmin):
    model = AccountSetting
    list_display = ('account',)
    fieldsets = ((None, {'fields': ['theme']}))


admin.site.register(AccountSetting)
