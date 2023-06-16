from django.urls import path
from . import views
from .views import login_view, registration_view
from .views import logout_view

urlpatterns = [
    path('', views.indx, name='home'),
    path('about', views.about, name='about'),
    path('footer', views.footer_view, name='footer'),
    path('download-cv', views.download_cv, name='download_cv'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.registration_view, name='register'),
]
