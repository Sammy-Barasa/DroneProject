from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from phone_field import PhoneField
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name,middle_name,last_name, email, phone, password=None):
        if first_name is None:
            raise TypeError('Users should have a first name as per government ID')
        if middle_name is None:
            raise TypeError('Users should have a middle name as per government ID')
        if last_name is None:
            raise TypeError('Users should have a last name as per government ID')
        if email is None:
            raise TypeError('Users should have a unique email')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name,middle_name,last_name, email, phone, password):
        if password is None:
            raise TypeError('Users should have password')

        user = self.create_user(first_name,middle_name,last_name, email, phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return 

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    id_number = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
   
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id_number','last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}-{self.email}-ID.NO: {self.id_number}-Phone:{self.phone}"

class DroneUAV(models.Model):
    drone_uid= models.CharField(unique=True)
    user_id = models.ManyToOneRel(to=User)
    condition = models.BooleanField(default=False)
    last_flight_decent_rate = models.FloatField(blank=True)
    last_flight_accent_rate = models.FloatField(blank=True)