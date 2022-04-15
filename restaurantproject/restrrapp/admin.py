# from django.contrib import admin
#
# # Register your models here.
# from .models import Category,Items1
#
# class Categoryadmin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}
# admin.site.register(Category,Categoryadmin)
#
# class Itemsadmin(admin.ModelAdmin):
#     list_display = ['name','price','updated']
#     list_editable = ['price']
#     prepopulated_fields = {'slug':('name',)}
#     list_per_page = 20
# admin.site.register(Items1,Itemsadmin)
