from django.db import models

# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=50)
    place_city = models.CharField(max_length=50)

    def __str__(self):
        return self.place_name
    

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    person_place = models.ForeignKey(Place,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    


    
