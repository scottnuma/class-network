from django.http import HttpResponse
from django.views import generic

from .models import Department, Course, User, Enrollment

class DepartmentsView(generic.ListView):
    template_name = 'graph/departments.html'

    def get_queryset(self):
        """Return all departments"""
        return Department.objects.all()

class DepartmentView(generic.DetailView):
    model = Department
    template_name = 'graph/department.html'

class CoursesView(generic.ListView):
    template_name = 'graph/courses.html'

    def get_queryset(self):
        """Return all courses"""
        return Course.objects.all()

class CourseView(generic.DetailView):
    model = Course
    template_name = 'graph/course.html'

class UserView(generic.DetailView):
    model = User
    template_name = 'graph/user.html'

class EnrollmentsView(generic.ListView):
    template_name = 'graph/enrollments.html'
     
    def get_queryset(self):
        """Return all enrollments"""
        return Enrollment.objects.all()

class EnrollmentView(generic.DetailView):
    model = Enrollment
    template_name = 'graph/enrollment.html'

def index(request):
    return HttpResponse("Hello, world. You're at the graph index.")
