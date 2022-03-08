from django.contrib import admin
from django.urls import path
from product_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('homepage', views.homepage),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete),  

]