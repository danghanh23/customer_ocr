from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="home_page"),
    path('contact/', views.contact, name= "contact"),
    path('register/', views.register, name= "register"),
    path('login/', LoginView.as_view(), {'template_name': 'pages/login.html'}, name='login'),
    # path('logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('logout/',views.logoutCustom,name='logout'),
    
    path('gotoRegister/',views.gotoRegister,name='gotoRegister'),
    
    
    path('customer/',views.addCustomer,name='addCustomer'),
    path('delete_customer/<int:pk>', views.deleteCustomer, name='delete_customer'),
    
    path('show_customer/<int:pk>', views.showCustomer, name='show_customer'),
    
    path('update_customer/<int:pk>', views.updateCustomer, name='update_customer'),
    
    
    
    
]

