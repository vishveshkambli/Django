from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=300)
    
class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)
    year=models.IntegerField()
    description=models.TextField(max_length=300,default='')
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)
    
    class Meta:
        db_table='account'
        
class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=300)
    
    class Meta:
        db_table='student'