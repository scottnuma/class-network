from django.urls import path

from . import views

app_name = 'graph'
urlpatterns = [
    path('', views.index, name='index'),
    path('department/<int:pk>/', views.DepartmentView.as_view(), name='department'),
    path('course/<int:pk>/', views.CourseView.as_view(), name='course'),
    path('user/<int:pk>/', views.UserView.as_view(), name='user'),
    path('enrollment/<int:pk>/', views.EnrollmentView.as_view(), name='enrollment'),
]
