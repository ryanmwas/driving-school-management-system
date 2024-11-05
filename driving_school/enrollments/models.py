from django.db import models # provides base classes for defining models

# Creating my models here
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(unique=True) # ensures each email in database is unique
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ClassSchedule(models.Model): # class schedule model rep schedule in database
    class_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.class_name

class Enrollment(models.Model): # enrollment model rep enrollment in database
    # Defines field that creates foreign key relationship to student model
    # on_delete=models.CASCADE ensures that if student is deleted, all enrollments are deleted
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # Defines field that creates foreign key relationship to class schedule model
    # on_delete=models.CASCADE ensures that if class schedule is deleted the corresponding enrollment is deleted
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.class_schedule}"