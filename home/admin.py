from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

class AboutAdmin(SummernoteModelAdmin):
    summer_note_fields = '__all__'

admin.site.register(About, AboutAdmin)