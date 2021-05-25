from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('',views.home,name = 'home'),
    path('user/<int:user_id>', views.userPage, name='user_page'),
    path('account/', views.accountSettings, name='account'),
    path('create_post/', views.createPost, name='create_post'),
]