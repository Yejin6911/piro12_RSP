from django.urls import path, include
from django.contrib.auth import views as auth_views
from RSP import views

app_name = 'RSP'

urlpatterns = [
    path('',views.main, name='main'),
    path('login/', views.login, name='login'),
    path('list/', views.list, name="list"),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('game/', views.send_friend_request, name='game'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accept/<int:pk>/', views.accept_friend_request, name='accept'),
]
