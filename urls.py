from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),                
    path('add/', views.add_user, name='add_user'),     
    path('success/', views.success, name='success'),   
    path('login/', views.login_view, name='login'),  
    path('order/', views.create_order, name='mhp_form'),  
    path('list/', views.order_list, name='order_list'), 
    path('update/<int:id>/', views.update_order, name='update_order'),
    path('delete_order/<int:id>/', views.delete_order, name='delete_order'),
    path('index/', views.item, name='item'),
    path('pro1/',views.pro1, name='boat_realbeat'),
    path('pro2/',views.pro2,name='marshall'),
    path('pro3/',views.pro3,name='redmi_headband'),
    path('pro4/',views.pro4,name='y1_quadmic')
    
]
