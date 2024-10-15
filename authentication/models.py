from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    department = models.CharField(max_length=50, null=False)
    mat_no = models.IntegerField(null=False)
    # level = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# class CustomerUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     # def create_staffuser(self, email, password):
#     #     """
#     #     Creates and saves a staff user with the given email and password.
#     #     """
#     #     user = self.create_user(
#     #         email,
#     #         password=password,
#     #     )
#     #     user.staff = True
#     #     user.save(using=self._db)
#     #     return user

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user


# class Student(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name="email address",
#         max_length=255,
#         unique=True,
#     )

#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)  # a admin user; non super-user
#     admin = models.BooleanField(default=False)  # a superuser
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     department = models.CharField(max_length=50)
#     mat_no = models.IntegerField(default=0)

#     # notice the absence of a "Password field", that is built in.

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = [
#         first_name,
#         last_name,
#         department,
#         mat_no,
#     ]  # Email & Password are required by default.

#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin


# # hook in the New Manager to our Model
# class User(AbstractBaseUser):  # from step 2
#     ...
#     objects = CustomerUserManager()
