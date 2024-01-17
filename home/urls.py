from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name= "contact"),
    path('register/', views.register, name= "register"),
    path('login/', LoginView.as_view(), {'template_name': 'pages/login.html'}, name='login'),
    # path('logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('logout/',views.logoutCustom,name='logout'),
    
    path('gotoRegister/',views.gotoRegister,name='gotoRegister'),
    
    
    path('customer/',views.addCustomer,name='addCustomer'),
    path('add_customer_url/', views.addCustomerxx, name='add_customer_url'),
    
    
]

