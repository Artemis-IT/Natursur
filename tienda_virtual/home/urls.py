from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.products_list, name='products_list'),
    path('citas/', views.appointments_list, name='citas_list'),
    path('citas/nueva/', views.appointment_create, name='citas_create'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
