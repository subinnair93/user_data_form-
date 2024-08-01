from django.db import models

# Create your models here.
class movie_info(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    desc = models.TextField()




class UserData(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)

class form_user_data(models.Model):
    maritial_status_details = [
        ('single','Single'),
        ('married','Married'),
        ('divorced','Divorced'),
        ('widowed','Widowed'),
    ]

    gender_details = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]


    name = models.CharField(max_length=50)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=50, choices=maritial_status_details)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=gender_details)
    language = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
    
