from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.createNote, name='create'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    path('detailed/<str:pk>/', views.detailed, name='detailed'),
    path("delete/<str:pk>/", views.deleteNote, name="delete-note"),
    path("update/<str:pk>/", views.updateNote, name="update-note"),
]
