from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='global'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('buy_ticket/<int:ticket_id>/', views.buy_ticket, name='buy_ticket'),
    path('hotels/', views.hotel_search, name='hotel_search'),
    path('search_tickets/', views.search_tickets, name='search_tickets'),
]

