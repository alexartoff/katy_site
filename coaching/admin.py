from django.contrib import admin

# Register your models here.
from .models import CoachMenu, Category, Post, PostData, PostComments


class CoachMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'post_date', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CoachMenu, CoachMenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostData)
admin.site.register(PostComments)
