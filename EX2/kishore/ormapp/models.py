from django.db import models
from django.contrib import admin 
class Car (models.Model):
    eid=models.CharField(max_length=20,help_text="Car")
    model=models.CharField(max_length=100)
    version=models.IntegerField()
    price=models.IntegerField()
    speed=models.IntegerField()




class Caradmin(admin.ModelAdmin):
    list_display=('eid','model','version','price','speed')
    
