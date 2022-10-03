from django.db import models


class Books(models.Model):
    status = models.CharField(max_length = 200)

    def __str__(self):
        return self.status


class Library(models.Model):
    ISBN = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    author = models.TextField()
    first_publishing_year = models.CharField(max_length = 200)
    number_of_pages = models.CharField(max_length=200)
    status = models.ForeignKey(Books,blank=False,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
