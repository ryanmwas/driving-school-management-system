from celery import shared_task
from django.core.mail import send_mail
from .models import Enrollment

@shared_task
def send_reminder():
    enrollments = Enrollment.objects.all()
    for enrollment in enrollments:
        send_mail(
            'Class Reminder',
            f'Dear {enrollment.student.first_name}, you have an upcoming class: {enrollment.class_schedule.class_name}',
            'from@example.com',
            [enrollment.student.email],
        )