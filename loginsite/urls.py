from django.urls import path
from . import views


urlpatterns = [
    path('', views.SiteLoginView.as_view(), name='login'),
    path('login_ok/', views.SiteLoginViewOk.as_view(), name='login_ok'),
    path('logout/', views.SiteLogoutView.as_view(), name='logout'),
    path('register/', views.SiteRegister.as_view(), name='register'),
    path('register_ok/', views.SiteRegister_ok.as_view(), name='register_ok'),
    path('profile/', views.ProfileEditView.as_view(), name='profile'),
]
