from django.db import models

# Create your models here.
class Book(models.Model):
    ID = models.IntegerField(primary_key=True) 
    Title = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Edition = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    Price = models.IntegerField()
    def __str__(self):
        return self.Name