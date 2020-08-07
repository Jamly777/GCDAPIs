from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=200)
    book_brief=models.CharField(max_length=200)
    series=models.CharField(max_length=200,null=True)

class Chapter(models.Model):
    book_name=models.CharField(max_length=200)
    chapter_name=models.CharField(primary_key=True,max_length=200)
    chapter_path=models.CharField(max_length=200)
    chapter_id=models.IntegerField()
    series = models.CharField(max_length=200, null=True)