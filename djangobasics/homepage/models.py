from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    firstname = models.CharField("First Name",max_length=50)
    lastname = models.CharField("Last name", max_length=50)
    email = models.EmailField()
    file = models.FileField()

    class Meta:
        db_table = "student"