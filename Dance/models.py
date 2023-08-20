from django.db import models
import accounts.models as AccountModel



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
    

class Post(models.Model):
    
    style = models.CharField(max_length=50)
    media_type = models.IntegerField()
    shortcode = models.CharField(max_length=50)
    thumbnail = models.URLField()
    comments = models.IntegerField()
    likes = models.IntegerField()
    views = models.IntegerField()
    video_url = models.URLField()
    user = models.ManyToManyField(AccountModel.Profile,blank=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Post_detail", kwargs={"pk": self.pk})
