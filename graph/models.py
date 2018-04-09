from django.db import models
from django.contrib.auth.models import User

import networkx as nx

MAX_TEXT_LENGTH = 256

class Department(models.Model):
    name = models.CharField(max_length=MAX_TEXT_LENGTH, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=MAX_TEXT_LENGTH)
    name = models.CharField(max_length=MAX_TEXT_LENGTH)
    website = models.CharField(max_length=MAX_TEXT_LENGTH)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("department", "code")

    def __str__(self):
        return str(self.department) + " " + str(self.code)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return str(self.user) + " in " + str(self.course)

    def graph():
        """Return a networkx graph of relations."""
        all_edges = Enrollment.objects.all()
        graph = nx.Graph()
        for edge in all_edges:
            graph.add_edge(edge.user, edge.course)
        return graph

    def graph_json():
        """Return a JSON string of the graph of enrollment."""
        return nx.node_link_data(Enrollment.graph())
