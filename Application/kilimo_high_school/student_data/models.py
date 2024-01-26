from django.db import models

# A model or database to store student information
# the database has student table and classstream table

from django.db import models

class ClassStream(models.Model):
    class_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    class_stream = models.ForeignKey(ClassStream, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"