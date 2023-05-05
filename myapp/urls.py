from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name='about'),
    path('form',views.forme,name='form'),
    path('products',views.products,name='products'),
    path('phone',views.phone,name='phone'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product'),
    path('register',views.register,name='register'),
    path('signup',views.signup,name='signup'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('change_password',auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='change_password'),
    path("password_change_done", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
   

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 