from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'is_published',
                    'category',
                    'location',
                    'pub_date',
                    'author',
                    'text')
    list_editable = ('location',
                     'category',
                     'is_published')
    search_fields = ('title',
                     'category',
                     'is_published',
                     'location',
                     'author',
                     'text')
    list_filter = ('category',
                   'location',
                   'is_published')


admin.site.register(Post, PostAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
