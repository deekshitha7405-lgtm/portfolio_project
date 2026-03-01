from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField()