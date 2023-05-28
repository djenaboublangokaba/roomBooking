from django.contrib.auth import views as auth_views
from django.urls import path
from .import views
urlpatterns = [
    path('admin', views.admin_page, name='admin'),
    path('employee', views.employee_page, name='employee'),
    path('customer/', views.customer_page, name='customer'),
    
    path('new_booking/', views.booking, name='new_booking'),
    path('booking-list/', views.booking_list, name='booking-list'),
    path('booking-detail/<int:pk>/', views.booking_detail, name='booking-detail'),
    path('booking-update/<int:pk>/', views.booking_update, name='booking-update'),
    path('delete-booking/<int:pk>/', views.delete_booking, name='delete-booking'),

    path('login/', views.login_view, name='login_view' ),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]