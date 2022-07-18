from django.db import models

# Create your models here.

class Room(models.Model):
    room_number = models.CharField(max_length=4)
    teacher_Name = models.CharField(max_length=100)
    scholar_Name = models.CharField(max_length =100)
    photo_url= models.TextField(default='https://tse3.mm.bing.net/th?id=OIP.sttsR_82WRk0u7zA7lpGPAHaFN&pid=Api&P=0&w=255&h=179')

    def __str__(self):
        return self.room_number

class Scholar(models.Model):
    Room = models.ForeignKey(
                        Room,
                        on_delete=models.CASCADE,
                        related_name='scholar',
                        )
    scholar_name = models.CharField(max_length=50, default='Jon Doe')
    parent_Name = models.CharField(max_length=100, default= 'Jane Doe')
    parent_Number = models.CharField(max_length= 10, default='(516)123-4567')
    date_Of_Birth = models.DateField(max_length = 10, default= '2012-11-12')
    teacher_Name = models.CharField(max_length = 20, default='Ms.Smikle')
    grade_Level = models.CharField(max_length = 4, default='4')
    room_Number = models.CharField(max_length = 4, default='110')
    pickup_Method = models.CharField(max_length = 20, default= 'Bus #280')
    photo_url= models.TextField(default='https://tse2.mm.bing.net/th?id=OIP.C4vvjQgPzPD3IrOHEZsQ7AAAAA&pid=Api&P=0&w=169&h=168')


    def __str__(self):
        return self.scholar_name

class Parent(models.Model):
    scholar = models.ForeignKey(
                        Scholar,
                        on_delete=models.CASCADE,
                        related_name='parent',
                        )
    first_name = models.CharField(max_length=50, default='Jon')
    last_name = models.CharField(max_length=50, default='Doe')
    relation_To_Scholar = models.CharField(max_length= 10, default='father')
    phone_number = models.CharField(max_length= 10, default='(516)123-4567')

    def __str__(self):
        return self.first_name
    




    






 