from django.contrib import admin
from django.urls import path
from product_app import views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import urls
from django.views.static import serve

urlpatterns = [
    
    path('create/', views.create),  
    path('view/',views.view),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete),  

]
if settings.DEBUG:
    # urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

