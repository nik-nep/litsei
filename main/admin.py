from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'rubric', 'published_date', 'image')
    list_display_links = ('title', 'text')
    search_fields = ('title', 'text', 'autor')



admin.site.register(Article, ArticleAdmin)
admin.site.register(Rubric)
admin.site.register(Tag)
admin.site.register(Department)
admin.site.register(Educationlevel)
admin.site.register(Qualification)
admin.site.register(Staff)
admin.site.register(Metodikfile)
admin.site.register(PravilaPryiomu)
