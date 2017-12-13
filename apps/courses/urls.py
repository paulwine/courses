from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^delete/(?P<course_id>\d+)$', views.delete),
    url(r'^del_process$', views.del_process),
    url(r'^go_back$', views.go_back)
    
]