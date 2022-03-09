from django.contrib import admin
from django.urls import path
from product_app import views

urlpatterns = [
    
    path('create/', views.create),  
    path('view/',views.view),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete),  

]