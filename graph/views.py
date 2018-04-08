from django.http import HttpResponse
from django.views import generic

from .models import Department, Course, User, Enrollment

class DepartmentView(generic.DetailView):
    model = Department
    template_name = 'graph/department.html'

class CourseView(generic.DetailView):
    model = Course
    template_name = 'graph/course.html'

class UserView(generic.DetailView):
    model = User
    template_name = 'graph/user.html'

class EnrollmentView(generic.DetailView):
    model = Enrollment
    template_name = 'graph/enrollment.html'

def index(request):
    return HttpResponse("Hello, world. You're at the graph index.")
