from django.db import models




# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
        
#         user = self.model(
#             email=email,
#             username=username
#         )
        
#         user.set_password(password)
#         user.save(using=self._db)
#         return user



# class Account(AbstractBaseUser):
#     email = models.EmailField(
#         unique=True,
#         max_length= 20
#         )
#     username = models.CharField(
#         max_length=20
#         )
    

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.email
