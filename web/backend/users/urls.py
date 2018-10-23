from django.urls import path, re_path
from users import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    re_path(r'^user/(?P<pk>\d+)/$', views.SpecificUserDetail.as_view()),
    path('user/me/', views.UserDetail.as_view()),
    path('settings/me/', views.UserSettingsView.as_view()),
]