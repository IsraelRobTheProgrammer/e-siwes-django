from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# import os
# from uuid import uuid4


# def path_and_rename(path):
#     def wrapper(instance, filename):
#         ext = filename.split(".")[-1]
#         # get filename
#         if instance.pk:
#             filename = "{}.{}".format(instance.pk, ext)
#         else:
#             # set filename as random string
#             filename = "{}.{}".format(uuid4().hex, ext)
#         # return the whole path to the file
#         return os.path.join(path, filename)

#     return wrapper


# Create your models here.


class LogBook(models.Model):
    date = models.DateField(default=now)
    desc = models.TextField(null=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="logbook_imgs")

    def __str__(self):
        return f"logbook_img_{self.date}"

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Logs"
