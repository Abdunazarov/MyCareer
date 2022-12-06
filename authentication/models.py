from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('User should have an emails')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password=None):
        if email is None:
            raise TypeError('User should have an email')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


ROLES = [
    ('Freelancer', 'freelancer'),
    ('Company', 'company')
]


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    role = models.CharField(max_length=15, choices=ROLES, default='Freelancer')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }



# class Freelancer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     # 1
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)

#     # 2
