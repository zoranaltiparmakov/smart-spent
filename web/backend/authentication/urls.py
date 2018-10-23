from django.urls import path, include
from authentication import views

urlpatterns = [
    path('login', views.ObtainAuthToken.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('register', views.RegistrationView.as_view()),
    path('', include('rest_auth.urls')),
]