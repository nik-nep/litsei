from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve
from photologue.sitemaps import GallerySitemap, PhotoSitemap

from .views import *

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    #path('menu/<int:pk>', menu_content, name='menu_content'),
    #path('menu/ch/<int:pk>', menuchild_content, name='menuchild_content'),
    path('', sitecontent),
]


sitemaps = {
    'photologue_galleries': GallerySitemap,
    'photologue_photos': PhotoSitemap,

}

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''

urlpatterns = [
    path('add', NewsCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
'''
