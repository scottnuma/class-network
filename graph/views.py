from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views import generic
from django.shortcuts import render

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

class SimpleJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        class_list = [User, Course, Enrollment]
        obj_is_a = lambda c: isinstance(obj, c)
        if any([obj_is_a(override_class) for override_class in class_list]):
            return str(obj)
        return super().default(obj)

def graph_json(request):
    result = Enrollment.graph_json()
    return JsonResponse(Enrollment.graph_json(), encoder=SimpleJSONEncoder)

def graph(request):
    return render(request, 'graph/graph.html')

def index(request):
    return render(request, 'graph/index.html')

