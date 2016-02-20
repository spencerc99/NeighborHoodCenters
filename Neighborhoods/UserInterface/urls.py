from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mat-view/', views.mat_view, name='mat_view'),
    url(r'^mat/', views.preferences, name='preferences_view')
]