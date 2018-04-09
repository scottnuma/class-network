from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'graph'
urlpatterns = [
    path('', views.index, name='index'),
    path('department/', views.DepartmentsView.as_view(), name='departments'),
    path('department/<int:pk>/', views.DepartmentView.as_view(), name='department'),
    path('department/new/', views.department_new, name='department new'),
    path('course/', views.CoursesView.as_view(), name='courses'),
    path('course/<int:pk>/', views.course, name='course'),
    path('course/new/', views.course_new, name='course new'),
    path('user/<int:pk>/', views.UserView.as_view(), name='user'),
    path('enrollment/<int:pk>/', views.EnrollmentView.as_view(), name='enrollment'),
    path('enrollment/', views.EnrollmentsView.as_view(), name='enrollments'),
    path('enrollment/new/', views.enrollment_new, name='enrollment new'),
    path('enrollment/delete/', views.enrollment_delete, name='enrollment delete'),
    path('graph/', views.graph, name='graph'),
    path('graph.json', views.graph_json, name='graph json'),
]
