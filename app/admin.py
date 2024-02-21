from django.contrib import admin
from django.db import models

# Register your models here.
class Admin(admin.ModelAdmin):
    usr = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.usr + self.password
    
    
    
    