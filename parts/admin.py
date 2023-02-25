from django.contrib import admin

from .models import Category, Part

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['code', 'title', 'parent',]

admin.site.register(Category, CategoryAdmin)

class PartAdmin(admin.ModelAdmin):
    list_display = ['category', 'position_on_drawing', 'references', 'part_number', 'quantity', 'part_replacement_number', 'designation', 'info', 'note']
    list_filter = ['category']  

admin.site.register(Part, PartAdmin)