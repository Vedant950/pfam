from django.contrib import admin
from .models import MyUser, Pet, TimeSchedule, DaySchedule

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Pet)
admin.site.register(TimeSchedule)
admin.site.register(DaySchedule)