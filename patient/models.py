from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'others'),
)

AGE_CHOICES = zip( range(1,150) ,range(1,150) )
class Person(models.Model):
    name = models.CharField(max_length=150)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField(choices=AGE_CHOICES)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    height =models.FloatField(validators= [MinValueValidator(1)])
    weight =models.FloatField(validators= [MinValueValidator(1)])
    blood_pressure = models.CharField(max_length=7)
    admit_date = models.DateTimeField("date of admission",auto_now_add=True)

    def __str__(self):
        return self.name
    

class Records(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    reports = models.FileField()