from django.contrib import admin

from .models import FriendRequest, Weapons

admin.site.register(Weapons)

@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'to_user']