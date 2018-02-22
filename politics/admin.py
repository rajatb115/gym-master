from django.contrib import admin
from .models import Blog, Category
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    summer_note_fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)