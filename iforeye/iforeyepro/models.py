from django.db import models

# Create your models here.

class Ngo_details(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)
    email =  models.EmailField(null=True, max_length=255)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    name = models.CharField(max_length=128)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    jonour = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    text_file = models.FileField(upload_to="text_files")

    def __str__(self):
        return self.name


class Recording(models.Model):
    name=models.CharField(max_length=120,primary_key=True)
    audio_file = models.FileField(upload_to="audio_files")
    name = models.ForeignKey(Book, on_delete=models.CASCADE)

class Dbfinalised(models.Model):
    name = models.CharField(max_length=50)
    text_file = models.FileField(upload_to="text_files")
