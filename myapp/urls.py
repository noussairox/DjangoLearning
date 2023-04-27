from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name='about'),
    path('form',views.forme,name='form'),
    path('products',views.products,name='products'),
    path('phone',views.phone,name='phone'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product'),
    path('register',views.register,name='register'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 