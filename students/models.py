from django.db import models
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_id = models.CharField(max_length=50, unique=True)
    cgpa = models.FloatField(null=True, blank=True)
    semester_scores = models.JSONField(null=True, blank=True) # example: {"sem1": 8.1, "sem2": 7.9}
    
    preferences = models.JSONField(null=True, blank=True)  # skills/interests field
    resume_file = models.FileField(upload_to="resumes/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
