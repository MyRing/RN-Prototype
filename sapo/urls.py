from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^theme$', TemplateView.as_view(template_name="ringtheme.html"), name=""),
    url(r'^theme2$', TemplateView.as_view(template_name="ringtheme2.html"), name=""),
#AVI
    url(r'^avi/00$', TemplateView.as_view(template_name="avi/avi-00.html"), name=""),
    url(r'^avi/01$', TemplateView.as_view(template_name="avi/avi-01.html"), name=""),
    url(r'^avi/02$', TemplateView.as_view(template_name="avi/avi-02.html"), name=""),
    url(r'^avi/03$', TemplateView.as_view(template_name="avi/avi-03.html"), name=""),
    url(r'^avi/04$', TemplateView.as_view(template_name="avi/avi-04.html"), name=""),
    url(r'^avi/05$', TemplateView.as_view(template_name="avi/avi-05.html"), name=""),
    url(r'^avi/06$', TemplateView.as_view(template_name="avi/avi-06.html"), name=""),
    url(r'^avi/07$', TemplateView.as_view(template_name="avi/avi-07.html"), name=""),
    url(r'^avi/08$', TemplateView.as_view(template_name="avi/avi-08.html"), name=""),
    url(r'^avi/09$', TemplateView.as_view(template_name="avi/avi-09.html"), name=""),


#PAP
    url(r'^pap/00$', TemplateView.as_view(template_name="pap/pap-00.html"), name=""),
    url(r'^pap/01$', TemplateView.as_view(template_name="pap/pap-01.html"), name=""),
    url(r'^pap/02$', TemplateView.as_view(template_name="pap/pap-02.html"), name=""),
    url(r'^pap/03$', TemplateView.as_view(template_name="pap/pap-03.html"), name=""),
    url(r'^pap/04$', TemplateView.as_view(template_name="pap/pap-04.html"), name=""),
    url(r'^pap/05$', TemplateView.as_view(template_name="pap/pap-05.html"), name=""),
    url(r'^pap/06$', TemplateView.as_view(template_name="pap/pap-06.html"), name=""),
    url(r'^pap/07$', TemplateView.as_view(template_name="pap/pap-07.html"), name=""),
    url(r'^pap/08$', TemplateView.as_view(template_name="pap/pap-08.html"), name=""),
    url(r'^pap/09$', TemplateView.as_view(template_name="pap/pap-09.html"), name=""),
    url(r'^pap/15$', TemplateView.as_view(template_name="pap/pap-15.html"), name=""),


#ORU
    url(r'^oru/00$', TemplateView.as_view(template_name="oru/oru-00.html"), name=""),
    url(r'^oru/01$', TemplateView.as_view(template_name="oru/oru-01.html"), name=""),
    url(r'^oru/02$', TemplateView.as_view(template_name="oru/oru-02.html"), name=""),
    url(r'^oru/03$', TemplateView.as_view(template_name="oru/oru-03.html"), name=""),
    url(r'^oru/04$', TemplateView.as_view(template_name="oru/oru-04.html"), name=""),
    url(r'^oru/05$', TemplateView.as_view(template_name="oru/oru-05.html"), name=""),
    url(r'^oru/06$', TemplateView.as_view(template_name="oru/oru-06.html"), name=""),
    url(r'^oru/07$', TemplateView.as_view(template_name="oru/oru-07.html"), name=""),
    url(r'^oru/08$', TemplateView.as_view(template_name="oru/oru-08.html"), name=""),
    url(r'^oru/09$', TemplateView.as_view(template_name="oru/oru-09.html"), name=""),
    url(r'^oru/10$', TemplateView.as_view(template_name="oru/oru-10.html"), name=""),
    url(r'^oru/11$', TemplateView.as_view(template_name="oru/oru-11.html"), name=""),
    url(r'^oru/12$', TemplateView.as_view(template_name="oru/oru-12.html"), name=""),



#CAT
    url(r'^cat/00$', TemplateView.as_view(template_name="cat/cat-00.html"), name=""),
    url(r'^cat/01$', TemplateView.as_view(template_name="cat/cat-01.html"), name=""),
    url(r'^cat/02$', TemplateView.as_view(template_name="cat/cat-02.html"), name=""),
    url(r'^cat/03$', TemplateView.as_view(template_name="cat/cat-03.html"), name=""),






#OTROS
    url(r'^pricing/$', TemplateView.as_view(template_name="pricing.html"), name="pricing"),
    url(r'^tos/$', TemplateView.as_view(template_name="tos.html"), name="tos"),
    url(r'^privacy/$', TemplateView.as_view(template_name="privacy.html"), name="privacy"),
    url(r'^aup/$', TemplateView.as_view(template_name="aup.html"), name="aup"),
    url(r'^404error\.html$', TemplateView.as_view(template_name="404.html"), name="404"),
    url(r'^admin/', include(admin.site.urls)),
)
