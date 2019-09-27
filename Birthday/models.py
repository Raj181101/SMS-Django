from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Birth(models.Model):
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Phone number must be startwith 6,7,8,9 'and length should be 10 digits allowed.")
    user=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birthday=models.DateTimeField(default="yy-mm-dd (2019-09-29)",auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.user

