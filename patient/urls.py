from django.urls import path
from .views import *
from . import views
import django.contrib.auth.views as auth_views
app_name = 'patient'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',auth_views.LoginView.as_view(template_name = 'patient/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'patient/logout.html'),name = 'logout'),
    path('register/',views.register,name = 'register'),
    path('settings/',views.settings,name = 'settings'),
    path('update/<int:id>/',views.update,name = 'update'),
    path('home/',views.home,name = 'home'),
    path('delete/<int:id>/',views.delete,name = 'delete'),
    path('addpatient/',views.addpatient,name = 'addpatient'),
    path('addreport/',views.addreport,name = 'addreport'),
]