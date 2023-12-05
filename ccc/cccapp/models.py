from django.db import models

# Create your models here.
from django.db import models

class Grade(models.Model):
        name = models.CharField(max_length=100, blank=True, null=True)
        def __str__(self):
            return self.name
class Subject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
      return self.name


class Book(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
       return self.name


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name