from django.contrib import admin
from redirect.models import Redirect

class RedirectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = fields = ("key", "url", "active")
    list_filter = ("active",)
admin.site.register(Redirect, RedirectAdmin)
