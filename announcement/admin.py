from django.contrib import admin
from .models import *
# Register your models here.

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('sorting', 'title', 'description', 'image', 'is_active')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')



admin.site.register(Announcement, AnnouncementAdmin)
