from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^theme$', TemplateView.as_view(template_name="ringtheme.html"), name=""),
    url(r'^theme2$', TemplateView.as_view(template_name="ringtheme2.html"), name=""),
#AVI
    url(r'^avispa/00$', TemplateView.as_view(template_name="avispa/avi-00.html"), name=""),
    url(r'^avispa/01$', TemplateView.as_view(template_name="avispa/avi-01.html"), name=""),
    url(r'^avispa/02$', TemplateView.as_view(template_name="avispa/avi-02.html"), name=""),
    url(r'^avispa/03$', TemplateView.as_view(template_name="avispa/avi-03.html"), name=""),
    url(r'^avispa/04$', TemplateView.as_view(template_name="avispa/avi-04.html"), name=""),
    url(r'^avispa/05$', TemplateView.as_view(template_name="avispa/avi-05.html"), name=""),
    url(r'^avispa/06$', TemplateView.as_view(template_name="avispa/avi-06.html"), name=""),
    url(r'^avispa/07$', TemplateView.as_view(template_name="avispa/avi-07.html"), name=""),
    url(r'^avispa/08$', TemplateView.as_view(template_name="avispa/avi-08.html"), name=""),
    url(r'^avispa/09$', TemplateView.as_view(template_name="avispa/avi-09.html"), name=""),


#PAP
    url(r'^papalotl/00$', TemplateView.as_view(template_name="papalotl/pap-00.html"), name=""),
    url(r'^papalotl/01$', TemplateView.as_view(template_name="papalotl/pap-01.html"), name=""),
    url(r'^papalotl/02$', TemplateView.as_view(template_name="papalotl/pap-02.html"), name=""),
    url(r'^papalotl/03$', TemplateView.as_view(template_name="papalotl/pap-03.html"), name=""),
    url(r'^papalotl/04$', TemplateView.as_view(template_name="papalotl/pap-04.html"), name=""),
    url(r'^papalotl/05$', TemplateView.as_view(template_name="papalotl/pap-05.html"), name=""),
    url(r'^papalotl/06$', TemplateView.as_view(template_name="papalotl/pap-06.html"), name=""),
    url(r'^papalotl/07$', TemplateView.as_view(template_name="papalotl/pap-07.html"), name=""),
    url(r'^papalotl/08$', TemplateView.as_view(template_name="papalotl/pap-08.html"), name=""),
    url(r'^papalotl/09$', TemplateView.as_view(template_name="papalotl/pap-09.html"), name=""),
    url(r'^papalotl/15$', TemplateView.as_view(template_name="papalotl/pap-15.html"), name=""),

#OTROS
    url(r'^pricing/$', TemplateView.as_view(template_name="pricing.html"), name="pricing"),
    url(r'^tos/$', TemplateView.as_view(template_name="tos.html"), name="tos"),
    url(r'^privacy/$', TemplateView.as_view(template_name="privacy.html"), name="privacy"),
    url(r'^aup/$', TemplateView.as_view(template_name="aup.html"), name="aup"),
    url(r'^404error\.html$', TemplateView.as_view(template_name="404.html"), name="404"),
    url(r'^admin/', include(admin.site.urls)),
)
