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
    path('news/', newss_list),
    path('news/<int:pk>', article_detail, name='article_detail'),
    path('about', about),
    path('leadership', leadership),
    path('pravyla', pravyla_pryiomu),
    path('public', public),
    path('contact', contact),
    path('navchalna/', navchalna_robota),
    path('vykhovna/', vykhovna_robota),
    path('metodychna/', metodychna_robota),
    path('rozklad/', rozklad_urokiv),
    path('struktura/', struktura_nr),
    path('zabezpechennya/', stypendialne_zabezpechennya),
    path('zvit/', zvit_director),
    path('plans/', plans),
    path('profession/', profession),
    # path('gallery/', gallery),
    path('rubric/<int:pk>', rubric_newss_list, name='rubric_newss_list'),
    path('trainingcenter/<int:pk>', trainingcenter_detal, name='trainingcenter_detal'),
    path('gallery/<int:pk>', gallery, name='gallery'),
    path('oldplans/<int:pk>', old_plans_list, name='old_plans_list'),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    path('', home),
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
