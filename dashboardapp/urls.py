from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^homePage/$',views.homePage,name='homePage'),
    url(r'^$',views.signUp,name='signUp'),
    url(r'^login/$', views.logIn, name='logIn'),
    url(r'^logout/$', views.logOut, name='logOut'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)