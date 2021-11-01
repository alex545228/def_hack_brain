from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20)


class Group(models.Model):
    category = models.CharField(max_length=20)
    vk_id = models.IntegerField(null=True)


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    rating = models.IntegerField()


class PersonalData(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=20)
    social_id_1 = models.CharField(max_length=50)
    social_id_2 = models.CharField(max_length=50)
    social_id_3 = models.CharField(max_length=50)
    social_id_4 = models.CharField(max_length=50)