from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'phone',
                                       'state',
                                       'city',
                                       'image',
                                       'bio',)
UserAdmin.fieldsets[2][1]['fields'] = ('is_active',
                                       'is_staff',
                                       'is_superuser',
                                       'groups',
                                       'user_permissions')
UserAdmin.list_display += ('is_superuser',)
admin.site.register(User, UserAdmin)
