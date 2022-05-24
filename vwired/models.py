from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")
    passport_number = models.CharField(max_length=500, default="", editable=True)
    date_of_birth = models.DateField(default="2015-12-12", editable=True, blank=True, null=True)
    email = models.EmailField(default="", editable=True)
    phone_number = models.IntegerField(blank=True, default="0123430000", editable=True)
    brief_description = models.TextField(max_length=1000, default="", editable=True)

    def __str__(self):
        return f"{self.last_name}"
