from django.db import models

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(max_length=26)
  last_name = models.CharField(max_length=26)
  birth_date = models.DateField()
  gpa = models.FloatField()