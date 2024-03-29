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
    path('category/<int:pk>', category_books, name='category_books'),
    path('rubric/<int:pk>', rubric_books, name='rubric_books'),
    path('filter/<int:pk>', filter_books, name='filter_books'),
    path('dystantsiyne-navchannya/', dystantsiyne_navchannya),
    path('', library),
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
