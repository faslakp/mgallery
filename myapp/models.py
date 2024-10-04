from django.db import models

# Create your models here.

class GenreChoices(models.TextChoices):

    ACTION='Action','Action'
    FICTION='Fiction','Fiction'
    THRILLER='Thriller','Thriller'

# 2.GENRE_CHOICES=[('Action','Action'),('Fiction','Fiction'),('Thriller','Thriller')]

class Movies(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)
    #2. genre=models.CharField(max_length=200,choices=GENRE_CHOICES)
    # genre=models.CharField(max_length=200)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)



# class Class_Choices(models.IntegerChoices):
#     CLASS1='1','1'
#     CLASS2='2','2'
#     CLASS3='3','3'
#     CLASS4='4','4'
# class Division_Choices(models.TextChoices):
#      DIV1='A','A'
#      DIV2='B','B'
#      DIV3='C','C'

# class Students(models.Model):
#     # null=false// required(ie,not to be null)
#     name=models.CharField(max_length=200,null=False,blank=False)

#     class_=models.CharField(max_length=200,choices=Class_Choices.choices)

#     division=models.CharField(max_length=200,choices=Division_Choices.choices)

#     about_me=models.TextField()



# class Car():
#     price=models.FloatField(max_length=200)
#     stock_sold_soldout=models.BooleanField()
#     date=models.DateField()
#     email=models.EmailField()
#     file=models.FileField()
#     image=models.ImageField()
    
#     web_address=models.URLField()
