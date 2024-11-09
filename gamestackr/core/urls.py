from django.contrib import admin
from django.urls import include, path

import gamestackr.accounts.urls

API_PREFIX = 'api/'

urlpatterns = [path('admin/', admin.site.urls), path(API_PREFIX, include(gamestackr.accounts.urls))]
