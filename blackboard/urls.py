from django.urls import path

from . import views

app_name = 'blackboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_session, name='new_session'),
    path('save', views.save_session, name='save_session'),
    path('delete', views.delete_session, name='delete_session'),
]
