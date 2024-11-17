from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class CourseManager(models.Manager):
    def create_course(self, name, description):
        if len(name) < 5:
            raise ValidationError("Course name must be at least 5 characters long.")
        if len(description) < 15:
            raise ValidationError("Description must be at least 15 characters long.")

        course = self.create(name=name)  
        CourseDescription.objects.create(course=course, content=description)  #
        return course


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CourseManager() 



class CourseDescription(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='description')
    content = models.TextField()

