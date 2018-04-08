from django.contrib import admin

from .models import Department, Course, User, Enrollment

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Enrollment)

