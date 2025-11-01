from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import StudentProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == 'student':
        StudentProfile.objects.create(
            user=instance,
            name=f"{instance.first_name} {instance.last_name}".strip(),
            email=instance.email,
            enrollment_id=f"ENR{instance.id}",
        )

