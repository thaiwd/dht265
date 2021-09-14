from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    educator = models.CharField(max_length=100)
    description = models.TextField()
    sub_description = models.CharField(max_length=300)
    num_lesson = models.PositiveSmallIntegerField(default=0)
    picture = models.ImageField(upload_to='course_picture')

    def __str__(self):
        return self.name
