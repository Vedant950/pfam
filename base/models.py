from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False)

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    add_breed = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=8)
    age = models.IntegerField(null=False)
    dob = models.DateField()
    height = models.DecimalField(max_digits=1000, decimal_places=3)
    weight = models.DecimalField(max_digits=1000, decimal_places=3)
    activity = models.CharField(max_length=100, null=True, blank=True)
    meal = models.CharField(max_length=100, null=True, blank=True)
    dislike = models.CharField(max_length=100, null=True, blank=True)
    allergies = models.CharField(max_length=100, null=True, blank=True)
    prefer_food = models.CharField(max_length=100, null=True, blank=True)
    help_required = models.CharField(max_length=100, null=True, blank=True)

TASK_CHOICES = [
    ('w', 'walk'),
    ('p', 'play'),
    ('f', 'food'),
    ('s', 'sleep'),
    ('b', 'bath'),
]

class TimeSchedule(models.Model):
    m0 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)
    m3 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)
    m6 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)
    m9 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)
    m12 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)
    m15 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)
    m18 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)
    m21 = models.CharField(max_length=10, choices=TASK_CHOICES, blank=True)

class DaySchedule(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    sun = models.OneToOneField(TimeSchedule, on_delete=models.CASCADE, related_name="sun", blank=True)
    mon = models.OneToOneField(TimeSchedule, on_delete=models.CASCADE, related_name="mon", blank=True)
    tue = models.OneToOneField(TimeSchedule, on_delete=models.CASCADE, related_name="tue", blank=True)
    wed = models.OneToOneField(TimeSchedule, on_delete=models.CASCADE, related_name="wed", blank=True)
    thr = models.OneToOneField(TimeSchedule, on_delete=models.CASCADE, related_name="thr", blank=True)
    fri = models.OneToOneField(TimeSchedule, on_delete=models.CASCADE, related_name="fri", blank=True)
    sat = models.OneToOneField(TimeSchedule, on_delete=models.CASCADE, related_name="sat", blank=True)