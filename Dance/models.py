from django.db import models



class Application(models.Model):

    EXPERIENCE_CHOICES  = [
        ('Beginner','Beginner'),
        ('Intermediate','Intermediate'),
        ('Advanced','Advanced')
    ]
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=400)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
    preferred_dance_style = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50,choices=EXPERIENCE_CHOICES,default='Beginner')
    preferred_class_time = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=12)
    photo = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.full_name
    