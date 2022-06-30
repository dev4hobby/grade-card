from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}: {self.description[:16]}..."


class GradeCard(models.Model):
    name = models.CharField(max_length=100)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField('Question')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Question(models.Model):
    image_url = models.URLField(blank=True)
    level = models.IntegerField(default=1)
    type_a = models.CharField(max_length=100)
    type_b = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.image_url} {self.type_a} {self.type_b} {self.answer}"


