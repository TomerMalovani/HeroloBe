from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^write$', views.write_msg, name='write_msg'),
    url(r'^readall$', views.read_all_msg, name='read_all_msg'),
    url(r'^readunread$', views.read_all_unread_msg, name='read_all_unread_msg'),
    url(r'^deletemsg$', views.delete_msg, name='delete_msg'),
    url(r'^readmsg$', views.read_msg, name='read_msg')

]
