from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug_title', 'is_active')
    list_filter = ('title', 'slug_title')
    search_fields = ('title', 'slug_title')

#admin.site.register(Content, ContentAdmin)
