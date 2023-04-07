from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Profile

admin.site.unregister(User)


class MyProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = (
        ('avatar', 'avatar_img'),
        'birthday',
        'city',
    )

    def avatar_img(self, instance):
        return mark_safe(f'<img src="{instance.avatar.url}" width="200" alt="avatar">')

    avatar_img.short_description = 'view'
    readonly_fields = ('avatar_img',)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'pre_view')
    fieldsets = (
        (None, {'fields': (('username', 'email'), 'password')}),
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Permissions', {'fields': (('is_active', 'is_staff', 'is_superuser'), 'groups', 'user_permissions')}),
        ('Important dates', {'fields': (('last_login', 'date_joined'),)}),
    )

    def pre_view(self, instance):
        return mark_safe(f'<img src="{instance.profile.avatar.url}" width="100" alt="avatar">')

    pre_view.short_description = 'avatar'
    readonly_fields = ('last_login', 'date_joined', 'pre_view')
    inlines = (MyProfileInline, )


# admin.site.register(User, MyUserAdmin)
