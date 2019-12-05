from . import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm
from django.contrib.auth import views as authViews
from django.contrib.auth.views import password_reset_confirm
# from django.contrib import admin

urlpatterns = [
    url(r'^login/$', views.logIn, name='logIn'),
    url(r'^signUp/$',views.signUp,name='signUp'),
    url(r'^$',views.page,name = 'page'),
    url(r'^learn$',views.learn,name = 'learn'),
    url(r'^profile$',views.profile,name = 'profile'),
    url(r'^new/questions$',views.post_question,name='questions'),
    url(r'^search/$',views.search_question, name = 'search'),
    url(r'^cate/(\d+)/$', views.question_category, name='cate'),
    url(r'^answer/(\d+)$', views.post_answer, name='answer'),
    url(r'^q_answer/(\d+)/$', views.question_answer, name='q_answer'),
    url(r'^logout/$', views.logOut, name='logOut'),
    url(r'^passwordReset/$', authViews.PasswordResetView.as_view(template_name='auth/password_reset.html'),
    name='passwordReset'),
    url(r'^passwordReset/done/$', authViews.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
    name='password_reset_done'),
    # url(r'^passwordResetConfirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',password_reset_confirm,
    # name='password_reset_confirm'),
    url(r'^passwordResetConfirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',authViews.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
    name='password_reset_confirm'),
    url(r'^passwordResetComplete/$', authViews.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
    name='password_reset_complete'),   
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    # url(r'^profile/(\d+)/$',views.profile,name = 'profile'),
    url(r'^upvote/(\d+)/$',views.upvotes, name = 'upvotes'),
    url(r'^downvote/(\d+)/$',views.downvotes, name = 'downvotes'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)