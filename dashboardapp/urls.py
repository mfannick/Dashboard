from . import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm
from django.contrib.auth import views as authViews
from django.contrib.auth.views import password_reset_confirm

urlpatterns = [
    url(r'^homePage/$',views.homePage,name='homePage'),
    url(r'^$',views.signUp,name='signUp'),
    url(r'^login/$', views.logIn, name='logIn'),
    url(r'^logout/$', views.logOut, name='logOut'),
    # url(r'^passwordReset/$', password_reset,name='passwordReset'),
    # url(r'^passwordReset/done/$', password_reset_done,name='password_reset_done'),
    # url(r'^passwordReset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    # name='password_reset_confirm'),
    url(r'^passwordReset/$', authViews.PasswordResetView.as_view(template_name='auth/password_reset.html'),
    name='passwordReset'),
    url(r'^passwordReset/done/$', authViews.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
    name='password_reset_done'),
    # url(r'^passwordResetConfirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', 
    # authViews.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
    # name='password_reset_confirm'),
    url(r'^passwordResetConfirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',password_reset_confirm,
    name='password_reset_confirm'),

    url(r'^passwordResetComplete/$', authViews.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
    name='password_reset_complete'),
 
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)