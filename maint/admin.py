from django.contrib import admin

from .models import Manual

class ManualAdmin(admin.ModelAdmin):
    list_display = ['overview',]

admin.site.register(Manual, ManualAdmin)
