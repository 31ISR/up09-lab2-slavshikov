from django.urls import path
from . import views

urlpatterns = [
    path('', views.communities_list),
    path('', views.communities_list, name="communities"),
]