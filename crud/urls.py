from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fileupload$', views.fileupload, name='fileupload'),
    
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^ajax/ajax$', views.ajax, name='ajaxpost'),
    url(r'^ajax/delete$', views.ajax_delete, name='ajax_delete'),
    url(r'^ajax/getajax$', views.getajax, name='getajax'),
    url(r'^register/$', views.register,name='register'),
    url(r'^register/success/$',views.register_success,name='register_success'),
    url(r'^users/$',views.users,name='users'),
    url(r'^users/delete/(?P<id>\d+)$', views.user_delete, name='user_delete'),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    url(r'^change_password$', views.changePassword, name='changePassword'),

    url(r'^search$', views.search, name='search'),
    url(r'^searchAjax$', views.searchAjax, name='searchAjax'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),

]