from django.db import models

MAX_TEXT_LENGTH = 256

class Department(models.Model):
    name = models.CharField(max_length=MAX_TEXT_LENGTH)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=MAX_TEXT_LENGTH)
    name = models.CharField(max_length=MAX_TEXT_LENGTH)
    website = models.CharField(max_length=MAX_TEXT_LENGTH)

    def __str__(self):
        return str(self.department) + " " + str(self.code)

class User(models.Model):
    name = models.CharField(max_length=MAX_TEXT_LENGTH)
    email = models.CharField(max_length=MAX_TEXT_LENGTH)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " in " + str(self.course)
