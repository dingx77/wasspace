from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

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
