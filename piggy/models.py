from django.db import models

# Create your models here.

class Scholar(models.Model):
    name = models.CharField(max_length=50)
    parentName = models.CharField(max_length=100)
    parentNumber = models.CharField(max_length= 10)
    dateOfBirth = models.DateField(max_length = 6)
    teacherName = models.CharField(max_length = 20)
    gradeLevel = models.CharField(max_length = 4)
    roomNumber = models.CharField(max_length = 4)
    pickupMethod = models.CharField(max_length = 20)
    photo_url= models.TextField()

    def __str__(self):
        return self.name

class Parent(models.Model):
    scholar = models.ForeignKey(
                        Scholar,
                        on_delete=models.CASCADE,
                        related_name='parents',
                        )

    






 