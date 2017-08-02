from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField()
    phone_number=models.CharField(blank=True)
    college=College.ForeignKey(to=College.related_name="departments")