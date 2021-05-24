from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('',views.home,name = 'home'),
    path('profile/<int:profile_id>', views.profile, name='profile'),
    path('profile/<int:profile_id>/edit', views.profile_edit, name='profile_edit')
]