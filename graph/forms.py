from django.forms import ModelForm, HiddenInput

from .models import Department, Course, Enrollment

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'code', 'name', 'website']

class EnrollmentForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']
        widgets = {'course': HiddenInput()}

