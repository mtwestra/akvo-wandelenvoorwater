from django.conf.urls.defaults import *
from django.views.static import serve
from W4W.models import school, inschrijving,steunpunt
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

info_dict_list_scholen = {
    'queryset': school.objects.all().order_by('NAAM_VOLLEDIG'),
    'paginate_by': 20,
    'extra_context':{'order_by':'nd'}
}


result=inschrijving.objects.filter(ACTIEF=True).order_by('-id')
numschools=len(result)
info_dict_list_inschrijvingen = {
    'queryset': result,
    'paginate_by': 20,
    'extra_context':{'order_by':'id','numschools':numschools}
}

info_dict_list_steunpunten = {
    'queryset': steunpunt.objects.filter(ACTIEF=True).exclude(NAAM__contains='onbekend').order_by('id'),
    'paginate_by': 20,
    'extra_context':{'order_by':'id'}
}

info_dict_detail={
    'queryset': school.objects.all(),
}

urlpatterns = patterns('', 
    (r'^scholen/$', 'django.views.generic.list_detail.object_list', info_dict_list_scholen),
    (r'^inschrijvingen/$', 'django.views.generic.list_detail.object_list', info_dict_list_inschrijvingen),
    (r'^steunpunten/$', 'django.views.generic.list_detail.object_list', info_dict_list_steunpunten),
    (r'^scholen/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict_detail),
    (r'^scholen/query/$', 'W4W.views.query_school'),
    (r'^inschrijvingen/query/$', 'W4W.views.query_inschrijving'),
    (r'^steunpunten/query/$', 'W4W.views.query_steunpunt'),
    (r'^inschrijf/$', 'W4W.views.inschrijf'),
    (r'^admin/', include(admin.site.urls)),
    (r'^scholen/export/$','W4W.views.export_to_excel_school' ),
    (r'^inschrijvingen/export/$','W4W.views.export_to_excel_inschrijf' ),
    (r'^WvW_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
)

