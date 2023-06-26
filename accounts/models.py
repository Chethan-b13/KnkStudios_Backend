from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.urls import reverse
from django.template.defaultfilters import slugify

class UserManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save()

        profile = Profile.objects.create(user=user)
        profile.save()

        return user
    

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserAccount(AbstractBaseUser,PermissionsMixin):
    """
    Custom User Model
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'                               

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    STYLES = [
        ('Dance','Dance'),
        ('Hiphop','Hiphop'),
        ('FreeStyle','FreeStyle'),
        ('Contemporary','Contemporary'),
        ('lock&pop','lock&pop')
    ]
    TEAM_CHOICES = [
        ('Ck6','ck6'),
        ('Kclan','kclan'),
    ]
    user = models.OneToOneField(UserAccount,on_delete=models.CASCADE)
    avatar = models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    style = models.CharField(choices=STYLES, max_length=50,default='Dance')
    team = models.CharField(choices=TEAM_CHOICES, max_length=50,blank=True,default='KalaNidhi')
    slug = models.SlugField(max_length=200,blank=True)

    def __str__(self):
        return self.user.name

    def get_absolute_url(self):
        return reverse('userProfile', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.user.name}-{self.style}")
        return super().save(*args, **kwargs)