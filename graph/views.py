from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.db import IntegrityError

from .models import Department, Course, User, Enrollment
from .forms import DepartmentForm, CourseForm, EnrollmentForm

GOOGLE_LOGIN_URL = "/auth/login/google-oauth2/"

class DepartmentsView(generic.ListView):
    template_name = 'graph/departments.html'

    def get_queryset(self):
        """Return all departments"""
        return Department.objects.all()

class DepartmentView(generic.DetailView):
    model = Department
    template_name = 'graph/department.html'

@login_required(login_url=GOOGLE_LOGIN_URL)
def department_new(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.creator = request.user
            department.save()
            return redirect('graph:department', pk=department.pk)
    else:
        form = DepartmentForm()
    context = {'form':form, 'object':'Department'}
    return render(request, 'graph/object_form.html', context)

class CoursesView(generic.ListView):
    template_name = 'graph/courses.html'

    def get_queryset(self):
        """Return all courses"""
        return Course.objects.all()

def course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    data = {'course':course.id}
    form = EnrollmentForm(initial={'course':course.id})
    enrolled = user_enrolled_in_course(request.user, course)
    context = {'course' : course, 'form':form, 'enrolled':enrolled}
    return render(request, 'graph/course.html', context)

def user_enrolled_in_course(user, course):
    if user.is_anonymous:
        return False
    all_enrollment_records = Enrollment.objects.all()
    return all_enrollment_records.filter(user=user, course=course).exists()
    
@login_required(login_url=GOOGLE_LOGIN_URL)
def course_new(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            course.save()
            return redirect('graph:course', pk=course.pk)
    else:
        form = CourseForm()
    context = {'form':form, 'object':'Course'}
    return render(request, 'graph/object_form.html', context)

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


@login_required(login_url=GOOGLE_LOGIN_URL)
def enrollment_new(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            course = enrollment.course
            enrollment.user = request.user
            try:
                enrollment.save()
            except IntegrityError:
                form.add_error('course', 'Already enrolled')
                context = {'course' : enrollment.course, 'form':form}
                return render(request, 'graph/course.html', context)
            else:
                return redirect('graph:course', pk=course.id)
        else:
            # context = {'course' : form.cleaned_data['course'], 'form':form}
            return render(request, 'graph:index')

@login_required(login_url=GOOGLE_LOGIN_URL)
def enrollment_delete(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form_result = form.save(commit=False)
            course = form_result.course
            enrolled = user_enrolled_in_course(request.user, course)
            context = {
                    'course' : course, 
                    'form':form,
                    'enrolled':enrolled
                    }
            try:
                enrollment = Enrollment.objects.get(course=course.id, user=request.user)
            except Enrollment.DoesNotExist:
                form.add_error('course', 'Not enrolled')
                return render(request, 'graph/course.html', context)
            else:
                enrollment.delete()
                return redirect('graph:course', pk=course.id)
        else:

            import ipdb; ipdb.set_trace()
            course = form.data.get('course', 0)
            data = {'course':course.id}
            form = EnrollmentForm(initial=data)
            context = {'course' : course, 'form':form}
            return render(request, 'graph/course.html', context)
    else:
        return HttpResponse("hmm")

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
