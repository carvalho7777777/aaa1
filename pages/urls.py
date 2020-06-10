from django.urls import path

from . import views

urlpatterns = [
    #path('', views.HomePageView.as_view(), name='home'),
    path('', views.ListPostView.as_view(), name='home'),
    path('post/<int:pk>/', views.DetailPostView.as_view(), name='post_detail'),
]
