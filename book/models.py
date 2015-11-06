from django.db import models
import MySQLdb
# Create your models here.
'''
Book {ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price}
Author {AuthorID (PK), Name, Age, Country}
'''
class Book(models.Model):
    ISBN  = models.CharField(max_length=50,primary_key=True)
    Title = models.CharField(max_length=50)
    AuthorID = models.CharField(max_length=50)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.CharField(max_length=50)
    Price = models.IntegerField()
    
class Author(models.Model):
    AuthorID = models.CharField(max_length=50,primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Country = models.CharField(max_length=50)
    