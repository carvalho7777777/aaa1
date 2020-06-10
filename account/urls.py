from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    #path('login/', views.user_login, name='login'),
    
    # Обработчики входа выхода.
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(),{'template_name': 'registration/logged_out.html'}, 
    #	name='logout'),
    
    # Обработчики смены пароля.
    #path('password_change/', auth_views.PasswordChangeView.as_view(), 
    #	name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), 
    #	name='password_change_done'),
    
    # Обработчики восстановления пароля.
    #path('password_reset/', auth_views.PasswordResetView.as_view(), {'template_name': 'registration/my_password_reset.html'},
    #	name='my_password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), 
    #	name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
    #	name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), 
    #	name='password_reset_complete'), 
    
    # Обработчики выход, выход, сброс пароля
    path('', include('django.contrib.auth.urls')),
    
    # Обработчики регистрации
    path('register/', views.register, name='register'),

    path('edit/', views.edit, name='edit'),

    #path('edit_company/', views.edit, name='edit_company'),
    
    # Страница после регистрации.
    path('', views.dashboard, name='dashboard'),
]
