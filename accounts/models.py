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
    avatar = models.ImageField(default='',upload_to=f'profile_pics/{user.name}')
    bio = models.TextField()
    style = models.CharField(choices=STYLES, max_length=50,blank=True,null=True)
    team = models.CharField(choices=TEAM_CHOICES, max_length=50,blank=True,default='KalaNidhi')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.user.name

    def get_absolute_url(self):
      return reverse('userProfile', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify([self.user.name,self.style])
      return super().save(*args, **kwargs)