from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    education_background = models.TextField(null=True, blank=True)
    grade_attained = models.CharField(max_length=100, null=True, blank=True)
    university_attended = models.CharField(max_length=200, null=True, blank=True)
    course_pursued = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
