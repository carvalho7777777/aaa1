from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.index, name='index'),
    #path('', profiles_list, name='profiles_list_url'),
    #path('<str:slug>', profile_detail, name='profile_detail_url'),
    path('edit/', views.edit, name='edit'),
]
