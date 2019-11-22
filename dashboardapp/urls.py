from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    url(r'^$',views.page,name = 'page'),
    url(r'^learn$',views.learn,name = 'learn'),
    url(r'^profile$',views.profile,name = 'profile'),
    # url(r'^homePage$',views.homePage,name='homePage'),
    url(r'^home$',views.home,name='home'),
    # url(r'^question/$',views.questions, name = 'question'),
    url(r'^new/questions$',views.post_question,name='questions'),
    url(r'^search/$',views.search_question, name = 'search'),
    url(r'^cate/(\d+)/$', views.question_category, name='cate'),
    url(r'^answer/(\d+)$', views.post_answer, name='answer'),
    url(r'^q_answer/(\d+)/$', views.question_answer, name='q_answer'),
        # url(r'stage/1/(?P<op>\w+)/(?P<id>\d+)$
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)