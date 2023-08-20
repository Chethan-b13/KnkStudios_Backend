from django.db import models
import accounts.models as AccountModel
from django.contrib.auth import get_user_model

# Create your models here.
class Workshop(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    duration = models.CharField(max_length=20)
    location_url = models.URLField(max_length=200)
    cover_image = models.URLField(max_length=200)
    premium = models.BooleanField(default=False)
    dance_instructor = models.ManyToManyField(AccountModel.Profile, verbose_name="dance_instructors")
    dance_style = models.ManyToManyField(AccountModel.Style)
    original_price = models.IntegerField(blank=True)
    offer_price = models.IntegerField(blank=True)
