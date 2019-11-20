from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.homePage,name='homePage'),
    url(r'^question/$',views.questions, name = 'question'),
    url(r'^new/questions$',views.post_question,name='questions'),
    url(r'^search/$',views.search_question, name = 'search'),
    url(r'^cate/(\d+)/$', views.question_category, name='cate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)