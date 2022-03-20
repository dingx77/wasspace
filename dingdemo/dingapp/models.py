from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    url = models.URLField()
    dateofbirth = models.DateField()

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name
