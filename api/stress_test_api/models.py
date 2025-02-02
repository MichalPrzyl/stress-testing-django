from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
    annotations = models.TextField(blank=True, null=True)
    birth_dt = models.DateField()


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    employees = models.ManyToManyField(Person, related_name="companies")


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="projects")
    members = models.ManyToManyField(Person, through="ProjectMembership", related_name="projects")


class ProjectMembership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    joined_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="tasks")
    status = models.CharField(
        max_length=50, choices=[("todo", "To Do"), ("in_progress", "In Progress"), ("done", "Done")]
    )
    dependencies = models.ManyToManyField("self", symmetrical=False, related_name="dependents", blank=True)


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    attendees = models.ManyToManyField(Person, related_name="meetings")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="meetings")
    notes = models.TextField(blank=True, null=True)
