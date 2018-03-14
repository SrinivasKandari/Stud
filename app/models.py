from django.db import models

# Create your models here.
class reg(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    gender_choices = (
                      ('M','Male'),
                      ('F','Female'),
                      ('O','Other'),
                     )
    gender = models.CharField(max_length=1,choices=gender_choices,default='M')
    course_choices = (
    ('ECE','ECE'),
    ('CSE','CSE'),
    ('Mech','Mech'),
    ('Aero','Aero'),
    ('BioTech','BioTech'),
    )
    courses = models.CharField(max_length=10,choices=course_choices,default='CSE')
    def __str__(self):
        return self.first
        
