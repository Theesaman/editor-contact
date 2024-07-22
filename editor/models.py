from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contect = models.TextField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.email}"
    

class Gallery(models.Model):
    img = models.ImageField()
    create_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.img}  {self.create_date}"


