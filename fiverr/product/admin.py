from django.contrib import admin
from .models import Category, MainProduct

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description',]
    prepopulated_fields = {"slug":("name",)}


class MainProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','categories','for_sale',]
    save_on_top = True
    prepopulated_fields = {"slug":("name",)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(MainProduct, MainProductAdmin)
