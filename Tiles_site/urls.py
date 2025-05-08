from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from showroom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
   path('contact/', views.contact_view, name='contact'),
   path('location/', views.location_view, name='location'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
   
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    