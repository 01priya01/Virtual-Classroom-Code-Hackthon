from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='enrolled_classes')

class Unit(models.Model):
    class_room = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='units')
    title = models.CharField(max_length=200)

class Session(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=200)

class Lecture(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=200)
    content = models.TextField()

class Comment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
